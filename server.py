import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    def post(self):
        body = self.get_argument('body')
        len_body = len(body)

        self.render("result.html",
                    len_body = len_body,
                    )

class HogeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is hoge page!")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/hoge", HogeHandler),
    ],
    template_path=os.path.join(os.getcwd(), "templates"),
    static_path=os.path.join(os.getcwd(), "static"),
)

if __name__ == "__main__":
    application.listen(8888)
    print("Server is up ...")
    tornado.ioloop.IOLoop.instance().start()
