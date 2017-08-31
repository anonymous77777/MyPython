import tornado.ioloop
import tornado.web

from application import application

port = 8000

def main():
    application.listen(port)

    print("Development server is running at http://127.0.0.1:%s" % port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()