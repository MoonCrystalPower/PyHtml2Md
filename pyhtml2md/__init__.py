import sys
from . html2md import html2md


def assert_supported_version():
    if sys.version_info < (3, 5):
        print('pyhtml2md supports only python 3.5 or later.')
        exit(4)


assert_supported_version()
__version__ = '0.01'
__author__ = ['Dong-hee Na', 'Sanghee Lee']
