#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

from logger import logger

result = ET.parse("test.xml")
# logger.warning(str(result))

root = result.getroot()
# for child in root:
#   logger.info("child.tag=%s,child.attribute=%s"%(child.tag,child.attrib))
for item in root.iter("neighbor"):
	print item.attrib
