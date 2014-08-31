# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from twisted.internet import defer
from twisted.internet import reactor

def synchronousIsValidUser(user):
    '''
    Return true if user is a valid user, false otherwise
    '''
    return user in ["Alice", "Angus", "Agnes"]

def asynchronousIsValidUser(user):
    d = defer.Deferred()
    reactor.callLater(2, d.callback, user in ["Alice", "Angus", "Agnes"])
    return d

def printResult(result):
    if result:
        print "User is authenticated"
    else:
        print "User is not authenticated"

def authenticateUser(isValidUser, user):
    d = defer.maybeDeferred(isValidUser, user)
    d.addCallback(printResult)

if __name__ == "__main__":
  authenticateUser(asynchronousIsValidUser, "Alice")