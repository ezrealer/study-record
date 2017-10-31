from selenium import webdriver

from scrapy.selector import Selector

browser = webdriver.Chrome(executable_path="/home/pzx/webdriver/chromedriver")
browser.get("https://www.zhihu.com/#signin")
# print(browser.page_source)

#点击登录页面下的“使用密码登录”
browser.find_element_by_css_selector("span.signin-switch-password").click()

#找到登录框然后输入密码和用户名
browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("18164885527")
browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("69615345")

#密码输入完成后点击“登录按钮”
browser.find_element_by_css_selector(".view-signin button.sign-button").click()
# browser.quit()
