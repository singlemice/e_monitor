# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'

import  tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port",default=8000,help="run on the port ")

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query=self.get_argument('q')
        #client=tornado.httpclient.HTTPClient()
        client=tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://127.0.0.1:8999/query?" + urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}), callback=self.on_response)
        #print "====",response.body
        #body=json.loads(response.body)
        #print "================"
        #print body
        #result_count=len(body['result'])
        #now=datetime.datetime.utcnow()
        #self.write("now:%s" %(now) )
    def on_response(self,response):
        body=json.loads(response.body)
        print "================"
        print body
        result_count=len(body['result'])
        now=datetime.datetime.utcnow()
        self.write("now:%s" %(now) )
        self.finish()
if __name__ =="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[
        (r"/query",IndexHandler)
    ])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()