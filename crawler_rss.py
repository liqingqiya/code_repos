#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import json
import time
import requests

def strip_space(string):
  """
  去掉字符串两端空白字符
  """
  return string.strip()

def get_web_page_by_url(url):
    """
    获得html文件
    """
    raw_data = requests.get(url=url).content
    soup = BeautifulSoup(raw_data.read())

    #进行utf-8编码
    return soup.prettify().encode("utf-8")

def load_and_parse(page):
    """
    传入，加载html文件对象 | 或者字符串
    并解析
    最后返回一系列json数据包
    """
    soup = BeautifulSoup(page)
    item_list = soup.find_all("item")
    for item in item_list:
        json_data = json.dumps(dict(
            title=item.div.h6.a["title"],
            link=item.div.h6.a["href"],
            datetime=strip_space(string=item.div.p.span.get_text()),
            download_time=time.time()
        ))
    yield json_data

if __name__=="__main__":
    url = "http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wpa/MRSS/newreleases/limit=300/rss.xml"
    page = get_web_page_by_url(url)
    load_and_parse(page)
    print "success"