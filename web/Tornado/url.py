#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

#import sys
#utf-8,兼容汉字
#from imp import reload
#reload(sys)
#sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.login import LoginHandler
#from handlers.user import UserHandler

url = [
    (r'/index', IndexHandler),
    (r'/', LoginHandler),
#    (r'/user', UserHandler),
]