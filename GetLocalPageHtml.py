import re

from bs4 import BeautifulSoup


def getLocalPageHtml():
    nowlist = []
    list = []
    path = 'Main.html'
    soup = BeautifulSoup(open(path, encoding='utf-8'), "html.parser")
    i = 1
    for item in soup.find_all('a', class_='chapterpage'):
        list.append(str(re.findall('''<a class=".*" href="(.*?)" id=".*">''', str(item)))[3:])

    for item in list:
        nowlist.append('http://www.xmanhua.com/'+item[:-3]+'/#p'+str(i))
        i+=1
    # print(nowlist)
    return nowlist
# getLocalPageHtml()