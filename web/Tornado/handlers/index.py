#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.escape
import tornado.gen
import methods.db as mrd
from handlers.base import BaseHandler

class IndexHandler(BaseHandler):
#    @tornado.web.authenticated  # 这是一个装饰器，它的作用就是完成 tornado 的认证功能，即能够得到当前合法用户。 P532
    @tornado.gen.coroutine
    def get(self):
        if not self.current_user:
            self.redirect("/")
            return
#        username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
#        UN = self.get_secure_cookie('user')
#        print(UN)
        self.render("index.html", users=user_infos)

    def post(self):
#        print(self.get_argument("type"))
        print(self.get_argument("id"))
        self.clear_cookie('user')
        self.redirect("/")
#        self.render("login.html")
        return

        # if val: # 所有验证通过 文件上传
        #     obj.fafafa.save(self)
        # self.render('home.html',error_message = None)