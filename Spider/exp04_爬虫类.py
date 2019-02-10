# -*- coding:utf-8 -*-
import urllib.request
import re  # 正则表达式包


class Spider:
    def __init__(self, argu1, argu2, step=1, start=1, number=1):
        """
        初始化
        :param argu1: 第一段url
        :param argu2: 第二段url
        :param step: 前一页与后一页url标记数改变步长倍数
        :param start: 第一个爬取的url标记数
        :param number: 爬取总页数
        """
        self.argu1 = argu1
        self.argu2 = argu2
        self.step = int(step)
        self.start = int(start)
        self.number = int(number)

        self.pattern = re.compile('<div.*?class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', re.S)
        # 加r让编译器把/与\当普通字符处理

    def load_page(self):
        """
        发送url获得页面源码
        """
        argu1 = self.argu1
        argu2 = self.argu2
        page = self.start

        user_agent = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
        headers = {'User-Agent': user_agent}
        while page <= self.number+self.start-1:
            print("正在爬第%d页" % page)
            req = urllib.request.Request(argu1+str(self.step*page)+argu2, headers=headers)
            response = urllib.request.urlopen(req)
            html = response.read()
            content = self.file_search(html)
            self.file_write(content, page)
            page += 1

    def file_search(self, html):
        text = html.decode('UTF-8')  # 以gbk解码，再以utf8编码
#        return str(text)
        return str(self.pattern.findall(text))

    def file_write(self, content, page):
        filename = "F:\program\Python\Spider\FileGet\exp04_html_get0"
        file = open(filename + str(page) + ".html", 'w', encoding='utf-8')
        final = content.replace("<p>", "").replace("</p>", "").replace("\\n", "\n")
        file.write(final)
        file.close()


if __name__ == '__main__':
    tieba_spider = Spider("http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=", "", 50, 1, 4)
    tieba_spider.load_page()
