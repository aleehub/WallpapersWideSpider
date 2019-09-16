import urllib

import threading

import multiprocessing

import requests

from lxml import etree


def wallpaperlist(url, headers):

    response = requests.get(url=url, headers=headers)

    content = etree.HTML(response.text)

    href = content.xpath("//div[@class='mini-hud' and @id='hudtitle']/a/@href")

    return href


def download(href,headers):

    print(href)

    response = requests.get(href[1], headers=headers)

    path = "download/%s.jpg"%href[0]

    write_to_html(path, response)

    print('下载成功:', href[0])



def write_to_html(path, response):

        with open(path, "wb") as f:

            f.write(response.content)

def main(pageNum):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                          (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Cookie': '_ga=GA1.2.1761384977.1568614064; _gid=GA1.2.409143292.1568614064; __gads=ID=b8f347fe9629b571:T=1568614066:S=ALNI_MZf1DuAq9mGzSvHv-vXE_t6_hgnWw; PHPSESSID=16bd3ec1907411f342a53005b6134d07; ae74935a9f5bd890e996f9ae0c7fe805=q5vS1ldKBFw%3D5bsJAoCRxp0%3D5JiQfeVePKY%3Dl4t%2FkEo5S%2Bc%3Daa0wj%2BrGoS4%3DlopdREWA8%2B4%3DquA2PukvyvY%3DQT%2B7MWP5KJ0%3D'
    }

    indexurl = 'http://wallpaperswide.com/top_wallpapers/page/'

    list1 = wallpaperlist(indexurl+str(pageNum), headers)

    list2 = []

    for i in list1:

        url = 'http://wallpaperswide.com/download'

        index = i.find('-')



        k = i.replace('wallpapers', '1920x1080')

        newurl = url+k

        list2.append((i[1:index], newurl))

    return list2

if __name__ == '__main__':

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                          (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Cookie': '_ga=GA1.2.1761384977.1568614064; _gid=GA1.2.409143292.1568614064; __gads=ID=b8f347fe9629b571:T=1568614066:S=ALNI_MZf1DuAq9mGzSvHv-vXE_t6_hgnWw; PHPSESSID=16bd3ec1907411f342a53005b6134d07; ae74935a9f5bd890e996f9ae0c7fe805=q5vS1ldKBFw%3D5bsJAoCRxp0%3D5JiQfeVePKY%3Dl4t%2FkEo5S%2Bc%3Daa0wj%2BrGoS4%3DlopdREWA8%2B4%3DquA2PukvyvY%3DQT%2B7MWP5KJ0%3D'
    }

    for i in range(11, 100):

        downlist = main(i)


        for i in downlist:


            # download(i, headers)

            thread_download = threading.Thread(target=download, args=(i,headers))

            thread_download.start()









