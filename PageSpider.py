import os
# import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup#网页解析
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import by as by
'''
步骤 # 1 爬取网页
    # 2 得到指定一个URL的网页内容
    # 3保存数据
'''

# 1 爬取网页
def main(url):
    print('爬取网页保存到文件里')
    savePath = 'Main.html'
    soup = getSoup(url)#soup
    saveData(savePath,soup)
    pass

# 2 得到指定一个URL的网页内容
def getSoup(url):
    print('拿到url:'+url)
    print(1)
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    print(2)
    driver.set_page_load_timeout(200)
    driver.get(url)
    WebDriverWait(driver,20,0.5).until(ec.visibility_of_all_elements_located((by.By.ID,'cp_image')))
    print(3)
    data = driver.page_source
    print(4)
    driver.quit()
    print('关闭浏览器并开始解析网页')
    soup = BeautifulSoup(data, "html.parser")
    print(int(str(soup.find_all('a', class_='chapterpage now'))[-7:-5]))
    return soup

def getPages(soup):
    return int(str(soup.find_all('a', class_='chapterpage now'))[-7:-5])

def saveData(path,soup):
    # time.sleep(5)
    if os.path.exists(path):
        os.remove(path)
        print('移除html')
    file = open(path,'wb')
    print('新建，覆写')
    file.write(bytes(str(soup),encoding='utf-8'))
    file.close()
# main('http://www.xmanhua.com/m11380/#p1')