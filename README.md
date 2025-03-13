# IW_licensing

Scrape licensing data from Isle of Wight council website

Uses license search, then scrapes core info for each response. Potential to scrape more for particular actions.

TO DO:

- parse to pandas df and save as csr for scraper archiving and diffing.
- crontab in github action to run scraper regularly;
- seed csv with historical data eg from start of year for now;
- consider proper db structure with diffrerent tables for different application types etc; a consideration of rows for particular types will strat to suggest what data relates to what license type.