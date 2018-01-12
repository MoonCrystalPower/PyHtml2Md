import unittest

from pyhtml2md.html_tags import *


class TestHtmlTags(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_h_tag(self):
        h1 = HBeginTag(count=1)
        self.assertEqual('# ', h1.getvalue())
        h2 = HBeginTag(count=2)
        self.assertEqual('## ', h2.getvalue())
        h3 = HBeginTag(count=3)
        self.assertEqual('### ', h3.getvalue())
        h4 = HBeginTag(count=4)
        self.assertEqual('#### ', h4.getvalue())
        h5 = HBeginTag(count=5)
        self.assertEqual('##### ', h5.getvalue())
        he = HEndTag()
        self.assertEqual('', he.getvalue())
        with self.assertRaises(TypeError):
            HBeginTag(count='5')
        with self.assertRaises(KeyError):
            HBeginTag()
            HBeginTag(other_key='other_key')

        h_end = HEndTag()
        self.assertEqual('', h_end.getvalue())

    def test_p_tag(self):
        p_begin = PBeginTag()
        self.assertEqual('', p_begin.getvalue())
        p_end = PEndTag()
        self.assertEqual('\n\n', p_end.getvalue())

    def test_b_tag(self):
        b_begin = BBeginTag()
        self.assertEqual('**', b_begin.getvalue())
        b_end = BEndTag()
        self.assertEqual('**', b_end.getvalue())

    def test_li_tag(self):
        li_begin = LIBeginTag()
        self.assertEqual('- ', li_begin.getvalue())
        li_end = LIEndTag()
        self.assertEqual('\n', li_end.getvalue())

    def test_div_tag(self):
        div_begin = DIVBeginTag()
        self.assertEqual('', div_begin.getvalue())
        div_end = DIVEndTag()
        self.assertEqual('', div_end.getvalue())

    def test_data_tag(self):
        data = Data(data='hello world')
        self.assertEqual('hello world', data.getvalue())
        with self.assertRaises(TypeError):
            Data(data=5)
        with self.assertRaises(KeyError):
            Data()
            Data(other_key='asdad')

    def test_em_tag(self):
        em_begin = EMBeginTag()
        self.assertEqual('*', em_begin.getvalue())
        em_end = EMEndTag()
        self.assertEqual('*', em_end.getvalue())

    def test_strong_tag(self):
        strong_begin = StrongBeginTag()
        self.assertEqual('**', strong_begin.getvalue())
        strong_end = StrongEndTag()
        self.assertEqual('**', strong_end.getvalue())

    def test_code_tag(self):
        code_begin = CodeBeginTag()
        self.assertEqual('`', code_begin.getvalue())
        code_end = CodeEndTag()
        self.assertEqual('`', code_end.getvalue())

    def test_strange_tag(self):
        with self.assertRaises(NotImplementedError):
            TagFactory.genTag('strange', None, 'start')

    def test_strange_position(self):
        with self.assertRaises(RuntimeError):
            TagFactory.genTag('h1', None, 'strange')

    def test_img_tag(self):
        with self.assertRaises(KeyError):
            # Avoid coala PyUnusedCodeBear.
            tag = ImgBeginTag()
            tag.getvalue()
