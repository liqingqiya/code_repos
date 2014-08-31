# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import os
import fnmatch

def remove_pyc(root=".", pattern="*.pyc"):
  """
  递归删除pyc文件
  :param root:
  :param pattern:
  :return:
  """
  for path, subdir, files in os.walk(root):
    for file_name in files:
      if fnmatch.fnmatch(file_name, pattern):
        file_full_name = os.path.join(path, file_name)
        os.remove(file_full_name)
        # print file_full_name

if __name__ == "__main__":
  remove_pyc(root="/home/liqing/PROJECT/ccooa_sae")
