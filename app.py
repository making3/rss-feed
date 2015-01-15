from rssparser import RssParser
from rssreader import RssReader
import sys

reader = RssReader()
article_list = []
feed_list = open('feedlist', 'r')

for feed in feed_list:
    if feed:
        feed_result = reader.read_url(feed)
        parser = RssParser(feed_result)

        while parser.EOF() == False:
            article_list.append(parser.get_next_article())

for article in article_list:
    print article
