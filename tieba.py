# coding=utf-8

import requests, sys, re

reload(sys)
sys.setdefaultencoding("utf-8")

html = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=gbk')

print html.text