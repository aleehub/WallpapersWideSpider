from wallpaper import main

from categories import getCategoriesList


if __name__ == '__main__':

    # 爬取开始页数
    a = 1

    # 爬取截止页数
    b = 6

    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                              (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            'Cookie': '_ga=GA1.2.1761384977.1568614064; _gid=GA1.2.409143292.1568614064; __gads=ID=b8f347fe9629b571:T=1568614066:S=ALNI_MZf1DuAq9mGzSvHv-vXE_t6_hgnWw; PHPSESSID=16bd3ec1907411f342a53005b6134d07; ae74935a9f5bd890e996f9ae0c7fe805=q5vS1ldKBFw%3D5bsJAoCRxp0%3D5JiQfeVePKY%3Dl4t%2FkEo5S%2Bc%3Daa0wj%2BrGoS4%3DlopdREWA8%2B4%3DquA2PukvyvY%3DQT%2B7MWP5KJ0%3D'
        }

    index_url = 'http://wallpaperswide.com'

    index_href_list, index_name_list = getCategoriesList(index_url, header)

    index_info_list = []

    for i in range(len(index_href_list)):

        new_href = index_url+index_href_list[i]

        index_info_list.append((index_name_list[i], new_href))

    print(index_info_list)

    main(a, b, header, index_info_list)

