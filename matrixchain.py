#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

def matrixchain_iter(p):
  n = len(p) -1
  m = [[0 for i in range(n+1)] for j in range(n+1)]
  s = [[0 for i in range(n+1)] for j in range(n+1)]

  for l in range(2, n+1):
    for i in range(1, n-l+2):
      j = i + l -1
      m[i][j] = sys.maxint
      for k in range(i, j):
        q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
        if q < m[i][j]:
          m[i][j] = q
          s[i][j] = k
  return m, s

def showmatrixchain(s,i,j):
  if i==j:
    print "A%d"%(i),
  else:
    print "(",
    showmatrixchain(s,i,s[i][j])
    showmatrixchain(s,s[i][j]+1,j)
    print ")",

p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrixchain_iter(p)
print (m[1][6])
showmatrixchain(s, 1, 6)
