# IW_licensing

Scrape licensing data from Isle of Wight council website

Uses license search, then scrapes core info for each response. Potential to scrape more for particular actions.

TO DO:

- parse to pandas df and save as csv for scraper archiving and diffing.
- crontab in github action to run scraper regularly;
- seed csv with historical data eg from start of year for now;
- consider proper db structure with diffrerent tables for different application types etc; a consideration of rows for particular types will strat to suggest what data relates to what license type.
- if an application is a renewal, there are likely to be previous cases with a staus of "Licence Superseded"