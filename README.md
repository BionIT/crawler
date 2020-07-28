# Django integration with scrapy
Data model:
#Item represents a lego set which has set name, its price, the url source and userId of the person who created the Item
1) Item: {name, price, source, userId} #userId is acquired from request and is needed to create an Iteam

Database:
sqlite

UI Features:
1) Django loginview 
2) simple interface allows user to create Item

Crawler:
run scrapy crawl webcrawler would trigger scrapy spider to crawl pages stored in the source
product(lego set) name and price are acquired through crawling and xpath parsing, and they are saved to sqlite in the pipeline. If price is reduced comparing to saved price, then an email would be sent 

TODO:
- add styling
- integrate with React 
- more features
