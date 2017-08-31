• handlers:我准备在这个文件夹中放前面所说的后端 Python 程序,主要处理来自前端的请求,并且操作数据库。
• methods:这里准备放一些函数或者类,比如用的最多的读写数据库的函数,这些函数被 handlers 里面的程序使用。
• statics:这里准备放一些静态文件,比如图片,css 和 javascript 文件等。
• templates:这里放模板文件,都是以 html 为扩展名的,它们将直接面对用户。

url.py 文件主要是设置网站的目录结构。

application.py 这个文件完成了对网站系统的基本配置,建立网站的请求处理集合。
from url import url 是将 url.py 中设定的目录引用过来。
setting 引用了一个字典对象,里面约定了模板和静态文件的路径,即声明已经建立的文件夹"templates"和"statics"分别为模板目录和静态文件目录。
接下来的 application 就是一个请求处理集合对象。请注意 tornado.web.Application() 的参数设置:
tornado.web.Application(handlers=None, default_host='', transforms=None, **settings)
关于 settings 的设置,不仅仅是文件中的两个,还有其它,比如,如果填上 debug = True 就表示出于调试模式。调试模式的好处就在于有利于开发调试,但是,在正式部署的时候,最好不要用调试模式。其它更多的 settings 可以参看官方文档:tornado.web-RequestHandler and Application classes

server.py 这个文件的作用是将 tornado 服务器运行起来,并且囊括前面两个文件中的对象属性设置。

P20 模板继承
