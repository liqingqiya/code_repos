#!/usr/bin/python
#-*- coding:utf-8 -*-

class FIFO(list):
    """
    由列表实现一个先进先出queue
    """
    def __init__(self):
        self.back = []
        self.append = self.back.append

    def pop(self):
        if not self:
            self.back.reverse()
            self[:] = self.back
            del self.back[:]
        return super(FIFO, self).pop()


if __name__ == "__main__":
    fifo = FIFO()
    fifo.append(12)
    fifo.append(3)
    fifo.append(41)
    print fifo
    print fifo.pop()
    print fifo
