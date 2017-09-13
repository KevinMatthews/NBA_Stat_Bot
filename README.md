# NBA_Stat_Bot

This is a bot that automatically scans new comments on the r/NBA subreddit, searching for comments which contain the pattern [Player Name stats]. When a comment with this pattern is found, the bot scrapes the mentioned player's per game stat data from basketball-reference.com using urllib2 and BeautifulSoup, and then replies to the comment on reddit with a nicely formatted table of the player's stats. 

This bot was intended to make it easier for reddit users to find a given player's stats, allowing them to avoid looking up the player's stats online by simply
typing their name into a comment and having the bot do the rest of the work. Hopefully this will facilitate discussions on the r/NBA subreddit by allowing easy
access to player stats. 
