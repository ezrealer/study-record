#-*-  conding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup as bs

tags = []
url ='https://movie.douban.com/j/search_tags?type=movie&source='
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read())
tags = result['tags']
#print(len(tags))
#for item in tags:
    #print(item)
movies = []
for tag in tags:
    limit = 0
    while 1:
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(limit)
        print url
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=200)
        result = json.loads(response.read())
        result = result['subjects']
        if(len(result)==0):
            break
        limit +=20
        for item in result:
            movies.append(item)
        break
    break
    
for x in range(0, len(movies)):
    item = movies[x]
    request = urllib2.Request(url=item['url'])
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    html = bs(result, 'html.parser')
    title = html.select('h1')[0].select('span')[0].get_text()
    #print title
    movies[x]['title'] = title

fw = open('/home/pzx/douban.txt', 'w')
for item in movies:
    tmp=''
    for key,value in item.items():
        #print(str(value))
        tmp += str(value) + ','
    fw.write(tmp[:-1] + '\n')
fw.close()