#!/usr/bin/env Python
# coding=utf-8

from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),

# cookie_secret 的值，常常用下面的方式生成（这是一个随机的字符串）：
# >>> import base64, uuid
# >>> base64.b64encode(uuid.uuid4().bytes)
# 如果嫌弃上面的签名短，可以用base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes) 获取。这里得到
# 的是一个随机字符串，用它作为 cookie_secret 值。
    cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies = True,    # 开启 XSRF 保护 P527
    login_url = '/',    # 如果用户不合法，根据这个设置，会返回到首页。当然，如果有单独的登录界面，比如是/login ，也可以login_url = '/login' 。 P533
#    handler_path = os.path.join(os.path.dirname(__file__), "handlers")
)

application = tornado.web.Application(
    url,
    **settings
)