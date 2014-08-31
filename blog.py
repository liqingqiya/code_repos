#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

result = requests.get("http://www.baidu.com",params = {"value":123456})
print result.url