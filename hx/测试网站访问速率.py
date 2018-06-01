#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 15:26

__author__ = 'Soenr'

import urllib.request
from datetime import *
import time

def Process(url,n):
  minSpan = 10.0
  maxSpan = 0.0
  sumSpan= 0.0
  over1s = 0
  for i in range(n):
    startTime = datetime.now()
    try:
      res = urllib.request.urlopen(url,timeout=10)
    except:
      pass
    endTime = datetime.now()
    span = (endTime-startTime).total_seconds()
    sumSpan = sumSpan + span
    if span < minSpan:
      minSpan = span
    if span > maxSpan:
      maxSpan = span
    #超过一秒的
    if span>1:
      over1s=over1s + 1
    print(u'%s  用时: %s 秒'%(url,span))
  print(u'请求次数:%s 时间,总花费:%s 秒,平均时长:%s 秒, 最大时长:%s 秒,最小时长:%s 秒,超过一秒:%s times'%(n,sumSpan,sumSpan/n,maxSpan,minSpan,over1s))
  print('\n')

if __name__=='__main__':
  Process('http://eam-dev.hollo.cn',10)