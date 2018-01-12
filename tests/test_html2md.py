import unittest

from pyhtml2md import html2md


class TestHTML2MD(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_h_tag1(self):
        md = html2md()
        for i in range(5):
            text = 'test'
            test_html = '<h'+str(i+1)+'>'+text+'</h'+str(i+1)+'>'
            converted_md = md.get_md(test_html)
            expected_md = '#'*(i+1)+' '+text
            self.assertEqual(expected_md, converted_md)

    def test_h_tag_with_p_tag(self):
        md = html2md()
        for i in range(5):
            text = 'test'
            test_html = '<p> <h'+str(i+1)+'>'+text+'</h'+str(i+1)+'> </p>'
            converted_md = md.get_md(test_html)
            expected_md = ' ' + '#'*(i+1)+' '+text+' \n\n'
            self.assertEqual(expected_md, converted_md)

    def test_h_tag_p_tag_itelic_and_bold(self):
        md = html2md()
        test_html = '<p>Text attributes <em>italic</em>, <em>italic</em>,' \
                    ' <strong>bold</strong>, <strong>bold</strong>,' \
                    ' <code>monospace</code>.</p>'
        expected_md = 'Text attributes *italic*, *italic*,' \
                      ' **bold**, **bold**, `monospace`.\n\n'
        converted_md = md.get_md(test_html)
        self.assertEqual(expected_md, converted_md)

    def test_img_tag(self):
        md = html2md()
        test_html = "<img src='/images/googlesummerofcode.png' " \
                    "alt='GSoC2017' />"
        expected_md = '![GSoC2017](/images/googlesummerofcode.png)'
        converted_md = md.get_md(test_html)
        self.assertEqual(expected_md, converted_md)


if __name__ == '__main__':
    unittest.main()
