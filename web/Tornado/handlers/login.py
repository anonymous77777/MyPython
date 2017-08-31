#!/usr/bin/env Python
# coding=utf-8

#import tornado.web
import methods.db as mrd

import tornado.escape
import tornado.gen
from handlers.base import BaseHandler
#import methods.readdb as mrd

class LoginHandler(BaseHandler):    # 继承 base.py 中的类 BaseHandler
    @tornado.gen.coroutine
    def get(self):
#        self.render("login.html")
        usernames = mrd.select_columns(table="users",column="username")
        one_user = usernames[0][0]
        self.render("login.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
#                self.set_cookie(username, db_pwd)   # 设置 cookie
#                self.set_secure_cookie('user', username)   # 以加密方式设置 cookie 密钥在 application.py 中定义
#                self.set_secure_cookie('user', username, httponly=True, secure=True)   # 以加密方式设置 cookie 密钥在 application.py 中定义 P525
                self.set_current_user(username) # 将当前用户名写入 cookie，方法见下面 (531)
                self.write(username)
#                self.write("welcome you: " + username)
            else:
                self.write("~")
#                self.write("your password was not right.")
        else:
            self.write("#")
#            self.write("There is no this user.")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user), expires_days=None) #注意这里使用了 tornado.escape.json_encode()
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler): #增加了一个专门用来显示错误的页面
    def get(self): #但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")