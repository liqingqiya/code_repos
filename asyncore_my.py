# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import asyncore, socket
import os
import mimetypes
import collections

from httplib import responses

class async_http(asyncore.dispatcher):
  """
  todo
  """
  def __init__(self, port):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.bind(("", port))
    self.listen(5)

  def handle_accept(self):
    client, addr = self.accept()
    return async_http_handler(client)

class async_http_handler(asyncore.dispatcher):
  """
  todo
  """
  def __init__(self, sock=None):
    asyncore.dispatcher.__init__(self, sock)
    self.got_request = False
    self.request_data = b""
    self.write_queue = collections.deque()
    self.responding = False

  def readable(self):
    return not self.got_request

  #读入传入请求
  def handle_read(self):
    chunk = self.recv(8192)
    self.request_data += chunk
    if b"\r\n\r\n" in self.request_data:
      self.handle_request()

  #处理传入请求
  def handle_request(self):
    self.got_request = True
    header_data = self.request_data[:self.request_data.find(b"\r\n\r\n")]
    header_text = header_data.decode("latin-1")
    header_lines = header_text.splitlines()
    request = header_lines[0].split()
    op = request[0]
    url = request[1][1:]
    self.process_request(op, url)

  #处理请求
  def process_request(self, op, url):
    self.responding = True
    if op == "GET":
      if not os.path.exists(url):
        self.send_error(404, "File %s not found \r\n"%url)
      else:
        type, encoding = mimetypes.guess_type(url)
        size = os.path.getsize(url)
        self.push_text("HTTP/1.0 200 OK\r\n")
        self.push_text("Content-length:%d\r\n"%size)
        self.push_text("Content-type:%s\r\n"%type)
        self.push_text("\r\n")
        self.push_text(open(url, "rb").read())
    else:
      self.send_error(501, "%s method not implement"%self.op)

  def send_error(self, code, message):
    self.push_text("HTTP/1.0 %s %s\r\n"%(code, responses[code]))
    self.push_text("Content-type:text/plain\r\n")
    self.push_text("\r\n")
    self.push_text(message)

  #将二进制数据添加到输出队列
  def push(self, data):
    self.write_queue.append(data)

  #将文本数据添加到输出队列
  def push_text(self, text):
    self.push(text.encode("latin-1"))

  #进在相应准备好的时候才能写入
  def writable(self):
    return self.responding and self.write_queue

  #写入相应数据
  def handle_write(self):
    chunk = self.write_queue.popleft()
    bytes_sent = self.send(chunk)
    if bytes_sent != len(chunk):
      self.write_queue.appendleft(chunk[bytes_sent:])
      if not self.write_queue:
        self.close()

#创建服务器
a = async_http(8080)

#持续轮询
asyncore.loop()
