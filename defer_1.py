# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from twisted.internet import reactor, defer

def getDummyData(x):
    """
    This function is a dummy which simulates a delayed result and
    returns a Deferred which will fire with that result. Don't try too
    hard to understand this.
    """
    d = defer.Deferred()
    # simulate a delayed result by asking the reactor to fire the
    # Deferred in 2 seconds time with the result x * 3
    reactor.callLater(2, d.callback, x * 3)
    return d

def printData(d):
    """
    Data handling function to be added as a callback: handles the
    data by printing the result
    """
    print d
print "begin..."
d = getDummyData(3)
print "after d..."
d.addCallback(printData)
print "after callback..."

# manually set up the end of the process by asking the reactor to
# stop itself in 4 seconds time
reactor.callLater(10, reactor.stop)
# start up the Twisted reactor (event loop handler) manually
reactor.run()