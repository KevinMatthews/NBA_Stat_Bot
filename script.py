#!/usr/bin/env python3

import praw
import re
from crawl import StatCrawler
from parser import CommentParser

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

crawler = StatCrawler()
parser = CommentParser("players.txt")

for comment in subreddit.stream.comments():
    name = parser.getPlayerName(comment.body)

    if name:
        crawler.getStats(name)
        comment.reply(crawler.prettify())


        
