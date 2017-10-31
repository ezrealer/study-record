from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/pzx/webdriver/chromedriver")
browser.implicitly_wait(10)
browser.get("https://www.weibo.com/login.php")
browser.find_element_by_id("loginname").clear()
browser.find_element_by_id("loginname").send_keys("ezreal_pzx@sina.com")
browser.find_element_by_name("password").send_keys("pzx,5201314")
browser.find_element_by_css_selector(".W_btn_a.btn_32px").click()

#登录结果截图保存
browser.get_screenshot_as_file("/home/pzx/图片/新浪.png")
browser.quit()