# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'

import tornado.ioloop
import tornado.web
from tornado.options import define,options
import tornado.options
import os
import time
import json
from tornado import httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('html/index.html')


class ChartsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('html/charts.html')

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(1)
        result={'result':{'res':"success",'status':200}}
        print type(result)
        js=json.dumps(result,ensure_ascii=False)
        print js
        self.write(js)

if __name__=="__main__":
    define("port", default=8999, help="run on the given port", type=int)
    define("debug", default=0, help="debug mode", type=int)
    css_path = os.path.join(os.getcwd(),'html/css')
    print css_path
    server_settings = {'debug' : options.debug}
    handles = [
        (r"/", MainHandler),
        (r"/css/(.*)",tornado.web.StaticFileHandler,{'path':css_path}),
        (r"/js/(.*)", tornado.web.StaticFileHandler,{'path': os.path.join(os.getcwd(),'html/js')}),
        (r"/font-awesome-4.1.0/(.*)", tornado.web.StaticFileHandler,{'path': os.path.join(os.getcwd(),'html/font-awesome-4.1.0')}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler,{'path': os.path.join(os.getcwd(),'html/fonts')}),
        (r"/charts.html",ChartsHandler),
        (r"/query",QueryHandler)

    ]
    tornado.options.parse_command_line()
    application = tornado.web.Application(handles, **server_settings)
    application.listen(options.port,address="0.0.0.0")
    tornado.ioloop.IOLoop.instance().start()