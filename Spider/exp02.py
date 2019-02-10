# -*- coding:utf-8 -*-
import urllib.request


if __name__ == '__main__':
    filestep = 1  # 文件数偏移量
    urlstep = 50  # 网页末尾值偏移步长，需要找规律

    filename = "F:\program\Python\Spider\FileGet\exp02_html_get0"  # 文件基地址
    urlraw = "http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn="  # 网页基地址
    user_agent = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"

    while filestep <= 3:
        file = open(filename + str(filestep) + ".html", 'w', encoding='utf-8')  # 打开各自的文件地址
        # exp02_html_get01，exp02_html_get02，exp02_html_get03   等
        url = urlraw + str(urlstep * filestep)  # 使用各自的网站地址（基地址+偏移值）
        # ie=utf-8&pn=50，ie=utf-8&pn=100，ie=utf-8&pn=150   等

        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read()
        text = html.decode('UTF-8')

        file.write(text)  # 写入各自的对应文件
        filestep += 1  #文件数偏移
        file.close()
