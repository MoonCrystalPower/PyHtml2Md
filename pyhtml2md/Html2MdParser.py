from io import StringIO
from html.parser import HTMLParser

from . html_tags import TagFactory


class Html2MdParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_lists = []

    def handle_starttag(self, tag, attrs):
        tag_data = TagFactory.genTag(tag, attrs, 'start')
        self.tag_lists.append(tag_data)

    def handle_data(self, data):
        tag_data = TagFactory.genData(data)
        self.tag_lists.append(tag_data)

    def handle_endtag(self, tag):
        tag_data = TagFactory.genTag(tag, None, 'end')
        self.tag_lists.append(tag_data)

    def get_md(self) -> str:
        self.converted_md = StringIO()
        for tag in self.tag_lists:
            self.converted_md.write(tag.getvalue())
        md = self.converted_md.getvalue()
        self.converted_md.close()
        return md
