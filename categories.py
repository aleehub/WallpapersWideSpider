import requests

from lxml import etree


def getCategoriesList(url, header):

    response = requests.get(url, header)

    content= etree.HTML(response.text)

    categoriesHrefList = content.xpath('//ul[contains(@class,"categories")]/li/a/@href')

    categoriesNameList = content.xpath('//ul[contains(@class,"categories")]/li/a/text()')

    return categoriesHrefList, categoriesNameList

