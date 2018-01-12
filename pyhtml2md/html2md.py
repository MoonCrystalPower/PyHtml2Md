from . Html2MdParser import Html2MdParser


class html2md(object):

    def _run(self, html: str) -> str:
        try:
            parser = Html2MdParser()
            parser.feed(html)
            md = parser.get_md()
        finally:
            parser.close()
        return md

    def get_md(self, html: str) -> str:
        md = self._run(html)
        return md
