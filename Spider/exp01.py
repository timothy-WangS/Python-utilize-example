# -*- coding:utf-8 -*-
import urllib.request
# urllib2在py3拆为为urllib.request和urllib.error，urllib.urlopen->urllib.request.urlopen;urllib2.Request->urllib.request.Request


filename01 = "F:\program\Python\Spider\FileGet\exp01_html_get01.html"  # 要写入的文件名
file01 = open(filename01, 'w', encoding='utf-8')  # 指定写入模式w,编码方式utf8
filename02 = "F:\program\Python\Spider\FileGet\exp01_html_get02.html"
file02 = open(filename02, 'w', encoding='utf-8')

response = urllib.request.urlopen("http://www.bilibili.com")  # 直接给请求(不推荐，有些网站会屏蔽恶意请求)
html = response.read()
text = html.decode('UTF-8')
file01.write(text)
file01.close()
# print(text)

url = "http://www.baidu.com"  # 指定链接地址
user_agent = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"  # 模仿浏览器请求头
# 请求头见https://blog.csdn.net/u012175089/article/details/61199238
headers = {'User-Agent': user_agent}  # 配置请求头

req = urllib.request.Request(url, headers=headers)  # 和请求头一起发送请求
response = urllib.request.urlopen(req)  # 接收传回的报文
html = response.read()  # 读取报文的字节格式
text = html.decode('UTF-8')  # 指定字节解码方式并保存到字符串形式
# print(text)
file02.write(text)  # 写入文件(之前已经指定了编码方式utf8，否则为gbk)
file02.close()
