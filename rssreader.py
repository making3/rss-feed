import urllib2

class RssReader:
    def read_file(self, file_name):
        file = open(file_name, 'r')
        return file.read()

    # TODO: Implement method to read a rss feed from a url
    def read_url(self, feed_url):
        return urllib2.urlopen(feed_url).read()
