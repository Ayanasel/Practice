
import GetLocalPageHtml as localHtml
import FolderCartoonTitleSpider as MkDir
import HtmlSpider as FromHtml
import PageSpider as Page
import PicturesSpider as pic
import GetLocalSoup as local

def main():
    MkDir.CreateMkDir()                                 #创建文件夹
    url = FromHtml.getDate()    #获取漫画主页中每一话的链接
    url.reverse()       #反序
    chapter = 1         #话数
    print(url)
    start = int(input('请输入开始的话数'))
    url = url[start:]
    chapter = start
    # print(url)
    for item in url:    #遍历每条链接
        print('开始遍历')
        urllist = item
        Page.main(urllist) #取到漫画详情页面的源码并保存到main.html中
        print('准备获取网页源码')
        soup = local.getLocalSoup() #取得上一步拿到的网页源码
        Pages = Page.getPages(soup) #取得该话页数
        getPic(chapter,Pages)       #调用方法获取每一页的图片
        chapter += 1
    print('success over')                                                     #获取所有图片
                                                        #保存在相应的文件夹里
def getPic(chapter,Pages):
    num = 1
    if Pages > 10:
        for url in localHtml.getLocalPageHtml():
            print(url)
            Page.main(url)
            urllist = pic.getDate()
            pic.getPictures(chapter, num,urllist)
            num += 1

if __name__ == '__main__':
    main()