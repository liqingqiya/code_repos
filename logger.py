#!/usr/bin/env python
# -*- coding=utf:8 -*-
######################
__all__ = ["logger"]
import logging
#创建日志对象
logger = logging.getLogger("my_logger")
#用自带的一个文件handler，创建handler对象
handler = logging.FileHandler("log.file")
#设置打印日志格式
formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")  
handler.setFormatter(formatter)
#将handler添加到日志对象中
logger.addHandler(handler)
#设置默认打印级别为INFO
logger.setLevel(logging.INFO)