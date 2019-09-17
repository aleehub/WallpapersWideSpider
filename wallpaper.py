
import threading

import requests

from lxml import etree

from createDir import mkdir


def wallpaperlist(url, headers):

    """
    根据wallpaperswide网页构造，生成热门壁纸的相对名字路径列表
    :param url: 热门壁纸路径
    :param headers: 请求头
    :return: 返回一个下载路径列表
    """
    # print(url)

    response = requests.get(url=url, headers=headers)

    content = etree.HTML(response.text)

    name_list = content.xpath("//div[@class='mini-hud' and @id='hudtitle']/a/@href")

    # print(name_list)

    return name_list


def download(href, header, categories_name):

    """
    根据传入壁纸路径，下载该壁纸
    :param href:
    :param header:
    :return:
    """

    response = requests.get(href[1], headers=header)

    mkdir('download/%s' % categories_name)

    path = "download/%s/%s.jpg" % (categories_name, href[0])

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


def link(page_num, header, index_url):
    """
    生成一个由壁纸名字和路径组成元组的列表
    :param page_num: 页数
    :param header:  请求头
    :return:
    """
    # 最热门壁纸的首页路径

    list1 = wallpaperlist(index_url+"/page/"+str(page_num), header)

    list2 = []

    for i in list1:

        url = 'http://wallpaperswide.com/download'

        k = i.replace('wallpapers', '1920x1080')

        new_url = url+k

        index = i.find('-')

        list2.append((i[1:index], new_url))

    return list2


def main(start, end, header, index_info):

    for item in index_info:

        categories_name = item[0]

        index_url = item[1]

        print("开始识别%s分类壁纸" % categories_name)

        for i in range(start, end):

            print("开始识别第%d页壁纸路径" % i)

            # print(index_url)

            down_list = link(i, header, index_url)

            print("识别完毕，开始下载第%d页壁纸" % i)

            # print(down_list)

            for j in down_list:

                print("开始下载:%s.jpg" % j[0])

                # download(j, header, categories_name)

                thread_download = threading.Thread(target=download, args=(j, header, categories_name))

                thread_download.start()




