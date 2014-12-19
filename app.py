from rssparser import RssParser
from rssreader import RssReader

reader = RssReader()
#feed = reader.read_file('example.xml')
feed = reader.read_url('http://rss.cnn.com/rss/cnn_tech.rss')
parser = RssParser(feed)

while parser.EOF() == False:
    parser.print_next()
    print '' # Print empty space.
