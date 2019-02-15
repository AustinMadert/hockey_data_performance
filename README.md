# NHL Hockey Draft Preference vs. Performance

The aim of this study was to answer the question, "Does preference for certain types of players in the preseason NHL draft result in a difference in team performance during the season?" 

Performance in this study is examined using wins and the difference in performance is the win percent change YoY. Additionally, each player has one of three main play positions: forward, defenseman, and goalie. Favored players are picked earlier in the draft, and so if a team picks a certain type of position earlier, it is said to prefer that position.

In order to answer this question draft data and performance data were gathered and a chi-squared test was run to understand any potential relationship that may exist between draft preference and performance. This study consisted of three main components:

- **Web Scraping**
    - *Information Sourcing*
    - *Created Webscraper Script*
    - *AWS EC2*
    - *NoSQL: Mongodb*

- **Data Munging**
    - *Cleaning in Pandas*
    - *Groupby and Merge*

- **Statistical Analysis**
    - *Histogram*
    - *Chi-Squared Test*

##Web Scraping

Data was sourced from http://www.nhl.com/ice/draftsearch.htm?year=&team=&position=&round=1 and https://www.hockey-reference.com/leagues/NHL_1998.html 




