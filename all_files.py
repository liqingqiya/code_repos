# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import os, fnmatch

def all_files(root, pattern="*", single_level=False, yield_folders=False):
  """
  将模式从字符串中取出放入列表中.
  :param root:
  :param pattern:
  :param single_level:
  :param yield_folders:
  :return:
  """
  pattern = pattern.split(";")
  for path, subdirs, files in os.walk(root):
    if yield_folders:
      files.extend(subdirs)
    files.sort()
    for name in files:
      for pattern in pattern:
        if fnmatch.fnmatch(name, pattern):
          yield os.path.join(path, name)
          break
    if single_level:
      break

if __name__ == "__main__":
  for itme in all_files("/home/liqing/PROJECT/test", "*.pyc"):
    print itme