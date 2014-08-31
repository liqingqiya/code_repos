#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup 

url = "http://music.baidu.com"
source = requests.get(url).content
soup = BeautifulSoup(source)
# print soup
# print soup.title
# print soup.title.name
print soup.title.string
# print soup.title.parent.name