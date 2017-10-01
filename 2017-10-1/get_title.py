import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'#假设的网址
total_page = 20 #假设网页有20页

f = open('../txt/text.txt','r')
html = f.read()
f.close()
#寻找标题
title = re.search('<title>(.*?)</title>',html,re.S).group(1)
print(title)