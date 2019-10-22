from selenium import webdriver

url='https://xxjc.pw/auth/login'
dr=webdriver.Chrome()
dr.get(url)

dr.find_element_by_xpath('//*[@id="email"]').send_keys('shangjian2019@outlook.com')
dr.find_element_by_xpath('//*[@id="passwd"]').send_keys('shangjian1997')
dr.find_element_by_xpath('//*[@id="login"]').click()
dr.implicitly_wait(100)
dr.find_element_by_xpath('//*[@id="checkin"]').click()
dr.implicitly_wait(200)
dr.quit()