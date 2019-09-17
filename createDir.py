#创建文件夹

import os


def mkdir(folder_name):

    folder = os.path.exists(folder_name)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹

        print("%s不存在，准备生成该文件夹" % folder_name)

        os.makedirs(folder_name)  # makedirs 创建文件时如果路径不存在会创建这个路径

        print("---  OK  ---")

    else:

        pass

