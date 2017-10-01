import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'#假设的网址
total_page = 20 #假设网页有20页
for num in range(2,total_page+1):#产生2-20页的链接
    new_url = re.sub('pageNum=\d+','pageNum=%d' % num,old_url,re.S)
    print(new_url)