# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# driver.get('http://www.xmanhua.com/m11381/')
# data = driver.page_source
# print(data)
# driver.quit()
# savePath = './Html/Main.html'
# open(savePath,'w')
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://cn.bing.com/')
