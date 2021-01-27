import os

import requests
from bs4 import BeautifulSoup#网页解析

import re       #正则表达式，进行文字匹配

def getDate():
    picurl = ""
    soup = BeautifulSoup(open('Main.html',encoding='utf-8'), "html.parser")
    for item in soup.find_all('img',id='cp_image'):
        picurl = "".join(re.findall('''<img id="cp_image" oncontextmenu="return false;" src="(.*?)" style="cursor: pointer; width: auto; height: auto;"/>''',str(item)))
    return picurl

def getPictures(chapter,page,urllist):#chapter 话数   page 页数
    url = urllist
    print(url)
    filename = selectMkdirName('Conment')
    root = './Conment/'+str(filename[chapter])
    path = root + "/%s.png"%page
    print('path='+path)
    try:
        if not os.path.exists(root):  # 判断是否存在文件并下载img
            os.mkdir(root)
        read = requests.get(url)
        with open(path, "wb")as f:
            f.write(read.content)
            f.close()
            print("文件保存成功！")
    except Exception as e:
        print(e.args)
        print("文件爬取失败！")

def selectMkdirName(fileDir):
    listName = []
    for dir in os.listdir(fileDir):
        listName.append(dir)
    return listName

# print(selectMkdirName('Conment')[0])
# getPictures(2,2)