from enum import Enum


class Tags(Enum):
    CODE = 'code'
    EM = 'em'
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    DIV = 'div'
    b = 'b'
    li = 'li'
    IMG = 'img'
    P = 'p'
    STRONG = 'strong'
    DATA = 'data'
    NONE = None


class TagFactory(object):

    @staticmethod
    def genTag(tag: str, attrs: str, position: str):
        begin_map = {
            'h1': HBeginTag(count=1),
            'h2': HBeginTag(count=2),
            'h3': HBeginTag(count=3),
            'h4': HBeginTag(count=4),
            'h5': HBeginTag(count=5),
            'div': DIVBeginTag(),
            'b': BBeginTag(),
            'li': LIBeginTag(),
            'img': ImgBeginTag(attrs=attrs),
            'p': PBeginTag(),
            'em': EMBeginTag(),
            'strong': StrongBeginTag(),
            'code': CodeBeginTag(),
        }
        end_map = {
            'h1': HEndTag(count=1),
            'h2': HEndTag(count=2),
            'h3': HEndTag(count=3),
            'h4': HEndTag(count=4),
            'h5': HEndTag(count=5),
            'div': DIVEndTag(),
            'b': BEndTag(),
            'li': LIEndTag(),
            'img': ImgEndTag(),
            'p': PEndTag(),
            'em': EMEndTag(),
            'strong': StrongEndTag(),
            'code': CodeEndTag(),
        }
        tag_map = {'start': begin_map, 'end': end_map}

        if position not in tag_map.keys():
            raise RuntimeError('Wrong position: {}'.format(position))

        if tag not in tag_map[position].keys():
            raise NotImplementedError('Not implemented for {} yet.'.format(tag))

        return tag_map[position][tag]

    @staticmethod
    def genData(data: str):
        return Data(data=data)


class BaseTag(object):

    def __init__(self, **kwargs):
        pass

    def getvalue(self):
        pass


class CodeBeginTag(BaseTag):

    def getvalue(self)->str:
        return '`'


class CodeEndTag(BaseTag):

    def getvalue(self)->str:
        return '`'


class EMBeginTag(BaseTag):

    def getvalue(self)-> str:
        return '*'


class EMEndTag(BaseTag):

    def getvalue(self)-> str:
        return '*'


class BBeginTag(BaseTag):

    def getvalue(self)-> str:
        return '**'


class BEndTag(BaseTag):

    def getvalue(self)-> str:
        return '**'


class DIVBeginTag(BaseTag):

    def getvalue(self)-> str:
        return ''


class DIVEndTag(BaseTag):

    def getvalue(self)-> str:
        return ''


class HBeginTag(BaseTag):

    def __init__(self, **kwargs):
        if 'count' not in kwargs:
            raise KeyError('count should be passed for ' +
                           type(self).__name__)

        if type(kwargs['count']) is not int:
            raise TypeError('count should be int type.')

        self._cnt = kwargs['count']

    def getvalue(self):
        return '#'*self._cnt + ' '


class ImgBeginTag(BaseTag):
    def __init__(self, **kwargs):
        if 'attrs' not in kwargs:
            raise KeyError('attrs should be passed for ' +
                           type(self).__name__)
        self.attrs = kwargs['attrs']

    def getvalue(self) ->str:
        alt = ''
        src = ''
        for attr in self.attrs:
            if attr[0] == 'src':
                src = attr[1]
            elif attr[0] == 'alt':
                alt = attr[1]
        return '![{}]({})'.format(alt, src)


class ImgEndTag(BaseTag):

    def getvalue(self):
        return ''


class HEndTag(BaseTag):

    def getvalue(self):
        return ''


class LIBeginTag(BaseTag):

    def getvalue(self):
        return '- '


class LIEndTag(BaseTag):

    def getvalue(self):
        return '\n'


class PBeginTag(BaseTag):

    def getvalue(self):
        return ''


class PEndTag(BaseTag):

    def getvalue(self):
        return '\n\n'


class StrongBeginTag(BaseTag):

    def getvalue(self)-> str:
        return '**'


class StrongEndTag(BaseTag):

    def getvalue(self)-> str:
        return '**'


class Data(BaseTag):

    def __init__(self, **kwargs):
        if 'data' not in kwargs:
            raise KeyError('data should be passed for ' + type(self).__name__)
        data = kwargs['data']
        if type(data) is not str:
            raise TypeError('data should be str type')

        self._data = data

    def getvalue(self):
        return self._data
