# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import threading, Queue, time, sys

Qin = Queue.Queue()
Qout = Queue.Queue()
Qerr = Queue.Queue()
Pool = []

def report_error():
  """
  将错误信息放入Qerr, 报告错误
  :return: None
  """
  Qerr.put(sys.exc_info()[:2])

def get_all_from_queue(Q):
  """
  获得队列Q中所有项, 无须等待
  :param Q:
  :return:
  """
  try:
    while True:
      yield Q.get_nowait()
  except Queue.Empty:
    raise StopIteration

def do_work_from_queue():
  """
  工作线程工作
  :return:
  """
  while True:
    command, item = Qin.get()
    if command == "stop":
      break
    try:
      if command =="process":
        result = "new" + item
      else:
        raise ValueError, "Unkown command %r"%command
    except:
      report_error()
    else:
      Qout.put(result)

def make_and_start_thread_pool(number_of_threads_in_pool=5, daemons=True):
  """
  创建一个N线程的池子, 是所有的线程成为守护线程, 启动所有的线程
  :param number_of_threads_in_pool:
  :param daemons:
  :return:
  """
  for i in range(number_of_threads_in_pool):
    new_thread = threading.Thread(target=do_work_from_queue)
    new_thread.setDaemon(daemons)
    Pool.append(new_thread)
    new_thread.start()

def request_work(data, command="process"):
  """
  工作请求在Qin中是形如(command, data)的元组
  :param data:
  :param command:
  :return:
  """
  Qin.put((command, data))

def get_result():
  return Qout.get()

def show_all_results():
  for result in get_all_from_queue(Qout):
    print "Result:", result

def show_all_errors():
  for etyp, err in get_all_from_queue(Qerr):
    print "Error:", etyp, err

def stop_and_free_thread_pool():
  """
  清理线程
  :return:
  """
  for i in range(len(Pool)):
    request_work(None, "stop")

  for existing_thread in Pool:
    existing_thread.join()

  del Pool[:]

if __name__ == "__main__":
  for i in ("_bass", "_be", "_bc"):
    request_work(data=i)

  make_and_start_thread_pool()
  stop_and_free_thread_pool()
  show_all_results()
  show_all_errors()