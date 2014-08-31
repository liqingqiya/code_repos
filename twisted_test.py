# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from twisted.web.client import getPage

from twisted.internet import reactor

def printContents(contents):
    '''
    这就是“callback”函数，被添加到Deferred，当“承诺了一定会有的数据”准备就绪后，
    Deffered会调用它
    '''

    print "Deferred调用了printContents，内容如下："
    print contents

    # 停止Twisted事件处理系统————这通常有更高层的办法
    reactor.stop()

# 调用getPage，它会马上返回一个Deferred————承诺一旦页面内容下载完了，
# 就会把他们传给我们的callback们
# 一旦调用getPage下载页面完成,则立即调用callback对应的函数.即addCallback(printContents)
#  中的printContents函数.
deferred = getPage('http://twistedmatrix.com/')

# 给Deferred添加一个callback————要求它在页面内容下载完后，调用printContents
deferred.addCallback(printContents)

# 启动Twisted事件处理系统，同样，这不是通常的办法
reactor.run()