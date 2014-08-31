#!/usr/bin/env python
#-*- coding:utf-8 -*-

#c[i,j] = c[i-1,j-1] + 1 xi==yi
#c[i,j] = max(c[i-1,j], c[i,j-1])

def computer(x,y):
  x_width = len(x) + 1
  y_width = len(y) + 1
  c = [[0 for item_x in range(x_width)] for item_y in range(y_width)]
  for i in range(1, y_width):
    for j in range(1, x_width):
      if x[j-1] == y[i-1]:
        c[i][j] = c[i-1][j-1] + 1
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
      else:
        c[i][j] = c[i][j-1]
  return c


if __name__ == "__main__":
  a = "bacdef"
  b = "abc"
  for i in computer(a, b):
    print i
