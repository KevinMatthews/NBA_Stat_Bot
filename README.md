# NBA_Stat_Bot

This is a bot that automatically scans new comments on the r/NBA subreddit, searching for comments which contain the pattern [Player Name stats]. When a comment with this pattern is found, the bot scrapes the mentioned player's per game stat data from basketball-reference.com using urllib2 and BeautifulSoup, and then replies to the comment on reddit with a nicely formatted table of the player's stats. 
