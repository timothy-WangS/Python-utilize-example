# -*- coding:utf-8 -*-
import urllib.request
import re  # 正则表达式包


pattern = re.compile('\d+\.\d+')  # 创建正则对象,小数
"""
1 特殊字符：\.^$?+*{}[]()|
　　　　　　以上特殊字符要想使用字面值，必须使用\进行转义
2 字符类
　　　　　   1. 包含在[]中的一个或者多个字符被称为字符类，字符类在匹配时如果没有指定量词则只会匹配其中的一个。
　　　　　　2. 字符类内可以指定范围，比如[a-zA-Z0-9]表示a到z，A到Z，0到9之间的任何一个字符
　　　　　　3. 左方括号后跟随一个^，表示否定一个字符类，比如[^0-9]表示可以匹配一个任意非数字的字符。
　　　　　　4. 字符类内部，除了\之外，其他特殊字符不再具备特殊意义，都表示字面值。
                ^放在第一个位置表示否定，放在其他位置表示^本身，-放在中间表示范围，放在字符类中的第一个字符，则表示-本身。
　　　　　　5. 字符类内部可以使用速记法，比如\d \s \w
            6.用.*?匹配任意
            7.()为取其内部的值
3 速记法
　　　　　　. 可以匹配除换行符之外的任何字符，如果有re.DOTALL标志，则匹配任意字符包括换行
　　　　　　\d 匹配一个Unicode数字，如果带re.ASCII，则匹配0-9
　　　　　　\D 匹配Unicode非数字
　　　　　　\s 匹配Unicode空白，如果带有re.ASCII，则匹配\t\n\r\f\v中的一个
　　　　　　\S 匹配Unicode非空白
　　　　　　\w 匹配Unicode单词字符，如果带有re.ascii,则匹配[a-zA-Z0-9_]中的一个
　　　　　　\W 匹配Unicode非单子字符

　　1.2 量词
　　　　1. ? 匹配前面的字符0次或1次
　　　　2. * 匹配前面的字符0次或多次
　　　　3. + 匹配前面的字符1次或者多次
　　　　4. {m} 匹配前面表达式m次
　　　　5. {m,} 匹配前面表达式至少m次
　　　　6. {,n} 匹配前面的正则表达式最多n次
　　　　7. {m,n} 匹配前面的正则表达式至少m次，最多n次
　　　　注意点：
　　　　　　以上量词都是贪婪模式，会尽可能多的匹配，如果要改为非贪婪模式，通过在量词后面跟随一个?来实现
"""

if __name__ == '__main__':
    filestep = 1  # 文件数偏移量
    urlstep = 50  # 网页末尾值偏移步长，需要找规律

    filename = "F:\program\Python\Spider\FileGet\exp03_html_get0"  # 文件基地址
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

        file.write(str(pattern.findall(text)))  # 写入各自的对应文件
        filestep += 1  #文件数偏移
        file.close()
