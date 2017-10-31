from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="/home/pzx/webdriver/chromedriver")
browser.get("https://www.oschina.net/blog")
time.sleep(3)
#鼠标下滑3次，下滑一次截一次图
for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
    browser.get_screenshot_as_file("/home/pzx/图片/博客{0}.png".format(i))
    time.sleep(2)

