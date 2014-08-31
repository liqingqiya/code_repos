#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class TestHandler(RequestHandler):
  def get(self):
    import pdb
    pdb.set_trace()
    self.write("hello world!\n")

settings = {"static_path":os.path.join(os.path.dirname(__file__), "static")}

application = Application([(r"/", TestHandler)],**settings)

if __name__ == "__main__":
  server = HTTPServer(application)
  print "success"
  server.listen(8000)
  IOLoop.instance().start()
