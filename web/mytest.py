#!/usr/bin/env Python
# coding=utf-8
import urllib.request
def go(a,b,c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print("%.2f%%" % per)

url = "http://youxi.66wz.com/uploads/1046/1321/11410192.90d133701b06f0cc2826c3e5ac34c620.jpg"
url = "http://www.sylu.edu.cn/sylusite/d/file/slgyw/2017-05-16/2d5093976d47164e3538c8fbd2873a9e.jpg"
local = "g.jpg"
urllib.request.urlretrieve(url, local, go)