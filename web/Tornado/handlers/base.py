#! /usr/bin/env python
# coding=utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):  # 可以将数据库连接写到这个类的初始化__init__() 方法中 P530
    def get_current_user(self):
        return self.get_secure_cookie("user")
