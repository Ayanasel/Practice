from bs4 import BeautifulSoup


def getLocalSoup():
    path = 'Main.html'
    soup = BeautifulSoup(open(path,encoding='utf-8'), "html.parser")
    return soup