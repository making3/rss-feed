from xml.dom.minidom import parseString

class RssParser:
    def __init__(self, xml):
        # Load the xml for later use.
        self.xml_doc = parseString(xml)
        self.article_list = self.xml_doc.getElementsByTagName('item')
        self.cursor = 0

    def print_next(self):
        article = self.article_list[self.cursor]
        print self.get_tag(article, 'title')
        print self.get_tag(article, 'link')
        print self.get_tag(article, 'description')
        self.cursor += 1

    def EOF(self):
        return self.cursor >= len(self.article_list)

    def get_tag(self, article, tag):
        return article.getElementsByTagName(tag)[0].firstChild.nodeValue
