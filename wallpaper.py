
import threading

import requests

from lxml import etree


def wallpaperlist(url, headers):

    """
    根据wallpaperswide网页构造，生成热门壁纸的相对名字路径列表
    :param url: 热门壁纸路径
    :param headers: 请求头
    :return: 返回一个下载路径列表
    """
    response = requests.get(url=url, headers=headers)

    content = etree.HTML(response.text)

    name_list = content.xpath("//div[@class='mini-hud' and @id='hudtitle']/a/@href")

    return name_list


def download(href, header):

    """
    根据传入壁纸路径，下载该壁纸
    :param href:
    :param header:
    :return:
    """

    response = requests.get(href[1], headers=header)

    path = "download/%s.jpg" % href[0]

    write_to_local(path, response)

    print('下载成功:%s.jpg' % href[0])


def write_to_local(path, response):
    """
    将响应内容写入本地
    :param path: 写入路径
    :param response: 响应内容
    :return:
    """
    with open(path, "wb") as f:

        f.write(response.content)


def link(page_num, header):
    """
    生成一个由壁纸名字和路径组成元组的列表
    :param page_num: 页数
    :param header:  请求头
    :return:
    """
    # 最热门壁纸的首页路径
    index_url = 'http://wallpaperswide.com/top_wallpapers/page/'

    list1 = wallpaperlist(index_url+str(page_num), header)

    list2 = []

    for i in list1:

        url = 'http://wallpaperswide.com/download'

        k = i.replace('wallpapers', '1920x1080')

        new_url = url+k

        index = i.find('-')

        list2.append((i[1:index], new_url))

    return list2


def main(start, end, header):

    for i in range(start, end):

        print("开始识别第%d页壁纸路径" % i)

        down_list = link(i, header)

        print("识别完毕，开始下载第%d页壁纸" % i)

        for j in down_list:

            print("开始下载:%s.jpg" % j[0])

            thread_download = threading.Thread(target=download, args=(j, header))

            thread_download.start()


if __name__ == '__main__':

        a = 1

        b = 5

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                              (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            'Cookie': '_ga=GA1.2.1761384977.1568614064; _gid=GA1.2.409143292.1568614064; __gads=ID=b8f347fe9629b571:T=1568614066:S=ALNI_MZf1DuAq9mGzSvHv-vXE_t6_hgnWw; PHPSESSID=16bd3ec1907411f342a53005b6134d07; ae74935a9f5bd890e996f9ae0c7fe805=q5vS1ldKBFw%3D5bsJAoCRxp0%3D5JiQfeVePKY%3Dl4t%2FkEo5S%2Bc%3Daa0wj%2BrGoS4%3DlopdREWA8%2B4%3DquA2PukvyvY%3DQT%2B7MWP5KJ0%3D'
        }

        main(a, b, header)







