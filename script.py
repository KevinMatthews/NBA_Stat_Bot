#!/usr/bin/env python3

import praw
import re
from crawl import StatCrawler
from parser import CommentParser

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

crawler = StatCrawler()
parser = CommentParser("players.txt")

#for comment in subreddit.stream.comments():
for comment in ["[Chris Paul stats]", "[Michael Jordan stats]"]:
    #name = parser.getPlayerName(comment.body)
    name = parser.getPlayerName(comment)

    if name:
        crawler.getStats(name)
        print(crawler.prettify())
        #comment.reply(crawler.prettify())


        
