# -*- coding: utf-8 -*-

import requests
from http import cookiejar
from bs4 import BeautifulSoup as bs
import time

# 获取session
session = requests.session()
# 获取cookies
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
# 获取cookie，如果之前登录成功，并且已经cookie，则可以获取到
try:
    session.cookies.load(ignore_discard=True)
except:
    print ("cookie未能加载")

# 设置请求头
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Host': 'www.zhihu.com',
    "Referer": "https://www.zhihu.com/",
}

# 获取xsrf
def get_xsrf():
    res = session.get('https://www.zhihu.com', headers=header)
    soup = bs(res.text,'html.parser')
    crsf = soup.select('input[name="_xsrf"]')[0]['value']
    print(soup.select('input[name="_xsrf"]')[0]['value'])
    return crsf

# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    print(captcha_url)
    response = session.get(captcha_url, headers=header)
    with open('captcha.gif', 'wb') as f:
        f.write(response.content)
        f.close()
    from PIL import Image
    try:
        im = Image.open('captcha.gif')
        im.show()
        im.close()
    except:
        pass

    captcha = input('请输入验证码: ')
    return captcha
#下载登录页面
def get_index():
    response = session.get('https://www.zhihu.com', headers = header)
    with open("index.html", "wb") as f:
        f.write(response.text.encode('utf-8'))
    print("写完了")

# 判断是否登录成功
def is_login():
    inbox_url = 'https://www.zhihu.com/inbox'
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        print('登录成功')
    else:
        print('登录失败')

# 登录方法
def zhihu_login(username, passwd):
    login_url = 'https://www.zhihu.com/login/phone_num'
    login_data = {
        '_xsrf': get_xsrf(),
        'phone_num': username,
        'password': passwd,
        'captcha': get_captcha()
    }
    response = session.post(login_url, data=login_data, headers=header)
    print(response.text)
    session.cookies.save() # 保存cookie



#get_captcha()
#get_xsrf()
#zhihu_login('18164885527','69615345')
is_login()
get_index()