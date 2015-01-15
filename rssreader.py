import urllib2

class RssReader:
    def read_file(self, file_name):
        file = open(file_name, 'r')
        return file.read()

    def read_url(self, feed_url):
        return urllib2.urlopen(feed_url).read()
