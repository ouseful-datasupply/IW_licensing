import requests
from bs4 import BeautifulSoup
import time
import urllib.parse
import random
from datetime import datetime, date
import calendar
import pandas as pd
import sys

class IWlicensingAPI:
    BASE_URL = "https://publicaccess.iow.gov.uk"

    def __init__(self):
        # Create a session object - this automatically stores cookies
        self.session = requests.Session()
        self.last_request_time = 0

        self.jsession_id = None
        self.csrf_token = None

    def get_month_dates(self, month_num, year, formatted=True):
        first_day = date(year, month_num, 1)
        last_day = date(year, month_num, calendar.monthrange(year, month_num)[1])
        if formatted:
            return self.format_date_to_string(first_day), self.format_date_to_string(
                last_day
            )

        return first_day, last_day

    # Via claude.ai
    def format_date_to_string(self, date_input):
        """
        Convert various date formats to a string in the format "DD/MM/YYYY".

        Args:
            date_input: Can be a datetime object, date object, string, timestamp, or pandas Timestamp

        Returns:
            String in format "DD/MM/YYYY"
        """
        if not date_input:
            return ""

        # Handle different input types
        if isinstance(date_input, (datetime, date)):
            # Already a datetime or date object
            return date_input.strftime("%d/%m/%Y")

        elif isinstance(date_input, str):
            try:
                # Try to parse the string as a date
                parsed_date = pd.to_datetime(date_input, dayfirst=True)
                return parsed_date.strftime("%d/%m/%Y")
            except:
                pass
                # raise ValueError(f"Could not parse date string: {date_input}")

        elif isinstance(date_input, pd.Timestamp):
            # Pandas Timestamp object
            return date_input.strftime("%d/%m/%Y")

        else:
            try:
                # Try to convert other types (like timestamps)
                parsed_date = pd.to_datetime(date_input, dayfirst=True)
                return parsed_date.strftime("%d/%m/%Y")
            except:
                pass
                # raise ValueError(f"Unsupported date format or type: {type(date_input)}")

    def get_csrf_credentials(self, typ="LicencingApplication"):
        # LicencingApplication or Licencing
        if typ == "LicencingApplication":
            SEARCHPAGE_URL = f"{self.BASE_URL}/online-applications/search.do?action=advanced&searchType=LicencingApplication"
        else:
            SEARCHPAGE_URL = f"{self.BASE_URL}/online-applications/search.do?action=advanced&searchType=Licencing"

        # Make an initial request that will set cookies
        response = self.session.get(SEARCHPAGE_URL)

        print(f"Session cookies: {self.session.cookies.get_dict()}")
        self.jsession_id = self.session.cookies.get_dict()["JSESSIONID"]
        print(f"JSESSIONID cookie: {self.jsession_id}")

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the form and extract the CSRF token
        csrf_input = soup.find("input", {"name": "_csrf"})
        self.csrf_token = csrf_input["value"] if csrf_input else None

        print(f"CSRF Token: {self.csrf_token}")

        return self.jsession_id, self.csrf_token

    def make_request(
        self,
        params=None,
        jsession_id=None,
        csrf_token=None,
        url=None,
        attempts=2,
        minwait=0.1,
    ):
        # typ: LicencingApplication or Licencing
        if not jsession_id or not csrf_token:
            if not self.jsession_id or not self.csrf_token:
                jsession_id, csrf_token = self.get_csrf_credentials()
            else:
                jsession_id, csrf_token = self.jsession_id, self.csrf_token

        url = (
            f"{self.BASE_URL}/online-applications/advancedSearchResults.do?action=firstPage"
            if url is None
            else url
        )
        url = f"{self.BASE_URL}/{url}" if url.startswith("/") else url

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua-platform": '"macOS"',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

        cookies = {"JSESSIONID": jsession_id}

        # if not params, return an example?
        use_params = params and (set(params.keys()) - {"searchType"})
        if not use_params:
            data = f"_csrf={csrf_token}&date%28receivedStart%29=13%2F02%2F2024&date%28receivedEnd%29=13%2F04%2F2024&searchType=Licencing"
            # print(f"QUERY: using example params; params sent were {params}")
        else:
            encoded_params = urllib.parse.urlencode(params)
            data = f"_csrf={csrf_token}&{encoded_params}"
            # print(f"QUERY: using data args: {data}; params sent were {params}")
            # For now, I am going to add parameter support
            # for things I want to use in scraping.
            # The scraper will work daily,
            # but to bootstrap the database, we might want to scrape
            # a month at a time, for example.

        # print(f"URL is {url}; data is {data}")
        # Be nice
        current_time = time.time()
        elapsed_time = current_time - self.last_request_time
        # THis could be expeirmented with...
        wait = random.uniform(minwait, minwait + 0.5)
        if elapsed_time < wait:
            wait_time = wait - elapsed_time
            # print(f"Waiting {wait_time:.4f} seconds to respect rate limit...")
            if wait_time > 0:
                time.sleep(wait_time)
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        # Update last request time
        self.last_request_time = time.time()

        if response.status_code != 200 and attempts>0:
            print("Trying again")
            attempts = attempts - 1
            self.make_request(url=url, params=params, attempts = attempts)

        print(response.status_code)

        return response

    def parse_messy_table(self, html_text, table_id="", table_class=""):
        """
        Scrapes key-value pairs from complex HTML tables with rowspans, colspans, and multiple values.

        Args:
            html_content: String containing HTML content
            table_class: Optional class of the specific table to scrape

        Returns:
            Dictionary with key-value pairs, where values can be either strings or lists of strings
        """
        soup = BeautifulSoup(html_text, "html.parser")

        # Find the target table
        if table_id:
            table = soup.find("table", id=table_id)
        elif table_class:
            table = soup.find("table", class_=table_class)
        else:
            table = soup.find("table")

        if not table:
            return {}

        result = {}
        current_key = None
        current_rowspan = 0

        # Process all rows
        for row in table.find_all("tr"):
            cells = row.find_all(["th", "td"])

            # Track position in the row
            cell_index = 0

            # Process all cells in this row
            for cell in cells:
                # Check if this is a header cell (potential key)
                if (
                    cell.name == "th"
                    and "scope" in cell.attrs
                    and cell.attrs["scope"] == "row"
                ):
                    # This is a key cell
                    current_key = cell.get_text(strip=True)
                    # Check if rowspan exists
                    if "rowspan" in cell.attrs:
                        current_rowspan = int(cell.attrs["rowspan"]) - 1
                    else:
                        current_rowspan = 0
                elif current_key and cell.name == "td":
                    # This is a value cell
                    colspan = int(cell.attrs.get("colspan", 1))
                    value = cell.get_text(strip=True)

                    # Skip if value is empty
                    if not value:
                        continue

                    # Add or append the value to the appropriate key
                    if current_key not in result:
                        result[current_key] = value
                    elif isinstance(result[current_key], list):
                        result[current_key].append(value)
                    else:
                        # Convert to list if we have multiple values
                        result[current_key] = [result[current_key], value]

                cell_index += 1

            # Handle rowspan for the next row
            if current_rowspan > 0:
                current_rowspan -= 1

        # Clean up any nested lists if needed
        for key, value in result.items():
            if isinstance(value, list) and len(value) == 1:
                result[key] = value[0]

        return result

    def _parse_summary_record(self, html_text, tableId="simpleDetailsTable"):
        soup = BeautifulSoup(html_text, "html.parser")
        table = soup.find("table", {"id": tableId})
        data = {}

        for row in table.find_all("tr"):
            key = row.find("th").get_text(strip=True)
            value = row.find("td").get_text(strip=True).strip("\n\r |")
            data[key] = value

        return data

    def _parse_response(self, response):
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        applications = []
        for li in soup.find_all("li", class_="searchresult"):
            title = (
                li.find("div", class_="summaryLinkTextClamp").get_text(strip=True)
                if li.find("div", class_="summaryLinkTextClamp")
                else "N/A"
            )
            link = (
                li.find("a", class_="summaryLink")["href"]
                if li.find("a", class_="summaryLink")
                else "N/A"
            )
            address = (
                li.find("p", class_="address").get_text(strip=True)
                if li.find("p", class_="address")
                else "N/A"
            )
            meta_info = (
                li.find("p", class_="metaInfo").get_text(strip=True)
                if li.find("p", class_="metaInfo")
                else ""
            )

            ref_no = "N/A"
            status = "N/A"
            applicant_name = "N/A"

            if "Ref. No:" in meta_info and "Status:" in meta_info:
                ref_no = (
                    meta_info.split("Ref. No:")[1].split("Status:")[0].strip("\n\r |")
                )
            if "Status:" in meta_info and "Applicant Name:" in meta_info:
                status = (
                    meta_info.split("Status:")[1]
                    .split("Applicant Name:")[0]
                    .strip("\n\r |")
                )
            if "Applicant Name:" in meta_info:
                applicant_name = (
                    meta_info.split("Applicant Name:")[1].strip("\n\r |")
                )

            applications.append(
                {
                    "title": title,
                    "link": link,
                    "address": address,
                    "ref_no": ref_no,
                    "status": status,
                    "applicant_name": applicant_name,
                }
            )

        # Check for next page link
        next_page_link = None
        next_page_anchor = soup.find_all("a", class_="next")
        if next_page_anchor:
            next_page_link = next_page_anchor[0]["href"]

        # for app in applications:
        #    print(app)

        if next_page_link:
            print("Next page URL:", next_page_link)

        return applications, next_page_link

    def parse_response(self, response, params=None, firstpageonly=True, getSummary=False):
        applications, next_page_link = self._parse_response(response)
        if not firstpageonly:
            while next_page_link:
                print("Getting next page...")
                response = self.make_request(url=next_page_link, params=params)
                _applications, next_page_link = self._parse_response(response)
                applications.extend(_applications)

        if getSummary:
            print(f"Getting summary data {len(applications)} records to collect...")
            for app in applications:
                link = app.get("link", "")
                if link:
                    response = self.session.get(f"{self.BASE_URL}{link}")
                    record = self._parse_summary_record(response.text)
                    # Add these items to the application dict
                    app.update({f"summary.{k}": v for k, v in record.items()})
                    # Are there any notice details?
                    record = self.parse_messy_table(
                        response.text, table_class="noticeDetails"
                    )
                    app.update({f"notice.{k}": v for k, v in record.items()})
                    # Are there any notice details?

        return applications

    def licensing_params_from_date_startend(self, start="", end="", typ="Licencing"):
        # LicencingApplication or Licencing

        if typ.lower() == "Licencing".lower():

            params = {
                "date(issuedStart)": self.format_date_to_string(start),
                "date(issuedEnd)": self.format_date_to_string(end),
                "searchType": "Licencing",
            }

        else:
            params = {
                "date(receivedStart)": self.format_date_to_string(start),
                "date(receivedEnd)": self.format_date_to_string(end),
                "searchType": "LicencingApplication",
            }
        return params

    def scrape_licenses(
        self,
        params=None,
        typ="LicencingApplication",
        firstpageonly=True,
        getSummary=False,
    ):
        # The firstpageonly setting is a defence

        # We make an assumption about the typ, if required
        if params and "searchType" not in params:
            params["searchType"] = typ
            # Could also check and maybe choose other typ
            # based on validating params keys

        # typ: LicencingApplication or Licencing
        self.get_csrf_credentials(typ)
        response = self.make_request(params)
        applications = self.parse_response(
            response, params, firstpageonly=firstpageonly, getSummary=getSummary
        )

        return applications
