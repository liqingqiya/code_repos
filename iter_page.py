#!/usr/bin/env python
#-*- coding:utf-8 -*-

def iter_page(current_page):
   left_edge=2
   left_current = 2
   right_current = 5
   right_edge =2
   last = 0
   max_page_num = current_page+right_current
   for num in xrange(1, max_page_num):
     print "the num is :%s"%num
     if (num<=left_edge) or (current_page-left_current-1<num<current_page+right_current) or(num>max_page_num-right_edge):
       if last+1!=num:
         print "yield num:%s, yield:None"%num
         yield None
       print "yield num:%s"%num
       yield num
       print "last:%s, num:%s"%(last, num)
       last=num
       print "\n"

def iter_page_2(current_page, left_edge=2, left_current=2, right_current=5):
    """
    todo
    """
    max_page_num = current_page + right_current
    prior_one = 0
    for num in xrange(1,max_page_num):
        print "the num is :%s"%num
        if (num<=left_edge) or (current_page-left_current<=num<=max_page_num-1):
            if prior_one+1 != num:
                print "yield num:%s, yield:None"%num
                yield None
            print "yield num:%s"%num
            yield num
            print "last:%s, num:%s"%(prior_one, num)
            prior_one = num
            print "\n"

if __name__ == "__main__":
    #print list(iter_page(6))
    print list(iter_page_2(6))  
