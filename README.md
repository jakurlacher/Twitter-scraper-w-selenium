# Twitter-scraper-w-selenium
Twitter scraper without using the Twitter API. 
Determines the word count of frequently used words for twitter users, visualizes the data using matplotlib, and sends the data to an SQL database for easy comparison. 
Uses automation to manually scroll through Twitter. Complies with Twitter Terms and Conditions.

First file to run is scrape.py. This will login to twitter and scrape the data. Next, run scrapevisualize.py. This will visualize the data, clean it, and send it
to a text file. Finally, run scrapedatabase.py. This will send the final data collected to an SQL database. Data from multiple users can be compared by following
the instructions in scrapedatabase.py.
