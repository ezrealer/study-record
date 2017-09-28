# -*- conding:utf-8- *-
import requests
from bs4 import BeautifulSoup as bs
import time
from echarts import Echart,Bar,Axis

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://www.weather.com.cn/textFC/db.shtml',
    'Host': 'www.weather.com.cn'
}

TEMP_list = [ ]
CITY_list = [ ]
C_MIN_list = [ ]

#获取每个省的详细
def get_temprature(url):
    #模拟真实用户浏览，避免反爬虫
    resp = requests.get(url,headers=headers)
    resp.encoding='utf-8'
    #print(resp.text) #输出，测试爬取成功否
    soup = bs(resp.content,'lxml')
    conMid_list1 = soup.find('div',class_='conMidtab')
    conMid_list2 = conMid_list1.find_all('div', class_='conMidtab2')
    #print(conMid_list2)
    
    for x in conMid_list2:
        #print(x)
        tr_list = x.find_all('tr')[2:]
        #print(tr_list)
        #province_tr = tr_list[2]
        #td_list = province_tr.find_all('td')
        #print(td_list)
        #province_td = td_list[0]
        #print(province_td.text.replace('\n',''))
        province = ' '
        for index,tr in enumerate(tr_list):
            if index == 0:
                td_list = tr.find_all('td')
                province = td_list[0].text.replace('\n',' ')
                city = td_list[1].text.replace('\n',' ')
                C_min = td_list[7].text.replace('\n',' ')
                #print(td_list[1].text)
            else:
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n',' ')
                C_min = td_list[6].text.replace('\n',' ')
                #print(city)
            #print('%s,%s,%s°' % (province,city,C_min))
            TEMP_list.append({
                'procince': province,
                'city': city,
                'C_min': C_min
            })
            CITY_list.append(province+city)
            C_MIN_list.append(C_min)
            

#获取所有的地区
url = 'http://www.weather.com.cn/textFC/hb.shtml'
#you_url = input('Please enter you url:')
#url = url.append(you_url)
def get_areas(url):
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    #print(res.text)
    soup = bs(res.text,'lxml')
    #print(soup)
    href_list = [ ]
    for ul in soup.select('.lq_contentboxTab2'):
        for x in range(0,7):
            li_list = ul.find_all('a')[x]['href']
            href = 'http://www.weather.com.cn' + li_list
            #print(href)
            href_list.append(href)
        #print(href_list)
    #给获取详细的函数添加网址
    for url in href_list:
        get_temprature(url)
        time.sleep(2) #设置每爬一次休眠两秒，避免过度占用网站服务资源
get_areas(url)
print(TEMP_list)