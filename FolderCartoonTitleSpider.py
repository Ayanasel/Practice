import json
import os

# 1 爬取一个页面的图片
def CreateMkDir():
    datalist = getDate()#标题
    mkdir('Conment/000 短篇')  # 创建文件夹
    for item in datalist:
        mkdir('Conment/'+item)#创建文件夹

# 2 得到指定标题
def getDate():
    data = []
    data3 = json.load(open('json.json', 'r', encoding='UTF-8'));
    for i in range(0, 122):
        data.append(data3['data']['ep_list'][i]['short_title'] + "话 " + data3['data']['ep_list'][i]['title'])
    return data

def mkdir(path):
    folder = os.path.exists(path)

    if  not  folder  :
        os.makedirs(path)
    else:
        pass





