from bs4 import BeautifulSoup#网页解析

import urllib.request,urllib.error  #指定url，获取网页数据

import re       #正则表达式，进行文字匹配


# 1 爬取网页
# def main():
#     baseurl="http://www.xmanhua.com/91xm/"
#     urllist = getDate(baseurl)#链接
#     pass

# 2 得到指定一个URL
def getDate():
    urllist = []#小链接
    URLlist = []#整合成长连接
    # 保存获取到的网页源码
    # html = askUrl(url)
    print('Start to soup the url')
    # 2逐一解析数据
    soup = BeautifulSoup(open('./Html/Main.html',encoding='utf-8'), "html.parser")
    # print(str(re.findall('''<a class="detail-list-form-item" href="(.*?)" target="_blank" title.*?>''',str(soup))))
    for item in soup.find_all('a',class_='detail-list-form-item'):
        urllist.append(str(re.findall('''<a class="detail-list-form-item" href="(.*?)" target="_blank" title.*?>''',str(item))))
        urllist.append(str(re.findall('''<a class="detail-list-form-item hide" href="(.*?)" target="_blank" title.*?>''',str(item))))
    # 拿到每一话的链接
    for item in urllist:
        # print(item[3:len(item)-3])
        if(item[3:len(item)-3]!=""):
            URLlist.append('http://www.xmanhua.com/'+item[3:len(item)-2])
    # print(URLlist)
    # print(len(URLlist))
    print('getUrlList Success')
    return URLlist


def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    # 用户代理，表示告诉网站我们是什么类型的机器，
    request = urllib.request.Request(url, headers=head)  # 请求数据
    html = ''
    try:
        response = urllib.request.urlopen(request)  # 响应
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html

# getDate('http://www.xmanhua.com/91xm')