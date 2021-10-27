#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/22 10:08
    @Describe 
    @Version 1.0
"""
import re
import random
import json

import requests


class Dytt:
    def __init__(self):
        self.url = "https://www.kuaidaili.com/free/inha/{}/"
        self.headers = [
            {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                           "AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
            {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                           "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        ]
        self.datas = []
        self.urlList = []
        self.z = 1

    def getResponse(self, url):
        random_index = random.randint(0, len(self.headers) - 1)
        return requests.get(url, self.headers[random_index]).content.decode("gbk")

    def parseHtml(self, context):
        pattern = '<img.*?(.*?)<img'
        result = re.compile(pattern, re.S).findall(context)
        result_01 = result[0].split("<br />")
        result_02 = []
        # 简单清洗数据
        for i in result_01:
            if i != '':
                result_02.append(i.replace(u'\u3000',u'').replace('◎',''))


        data = dict()
        for index,d in enumerate(result_02):
            if d[0:2]=='片名':
                data['片名'] = d[2:]
            if d[0:4]=='豆瓣评分':
                data['评分'] = d[3:]
            if d[0:2]=='类别':
                data['类别'] = d[2:]
            if d[0:2]=='片长':
                data['时长'] = d[2:]
            if d[0:2]=='导演':
                data['导演'] = d[2:]
            if d[0:2]=='产地':
                data['产地'] = d[2:]
            if d[0:2]=='主演':
                str01 = d[2:-1]
                for index01,i in enumerate(result_02):
                    if index01>index:
                        str01 = str01 + ''.join(i)
                    if i =='简介':
                        break
                data['主演'] = str01

        # 处理下载链接
        pattern = '<div class=player_list.*?<a href=(.*?)>'
        href01 = re.compile(pattern,re.S).findall(context)
        # print(href01)
        data['本站下载地址'] = href01

        pattern = '<p.*?id="downlist_info".*?<a href=(.*?)>'
        href02 = re.compile(pattern,re.S).findall(context)
        data['迅雷下载地址'] = href02

        self.datas.append(data)
        print(f"正在下载第{self.z}个")
        self.z = self.z + 1

        # print(self.datas)

    def saveFile(self):
        with open('./data/电影天堂.txt','w',encoding='utf-8') as f:
            datas = json.dumps(self.datas,indent=4, ensure_ascii=False)
            f.write(datas)
            print("完成")


    def run(self, page=5):

        # print(self.getResponse('https://www.dy2018.com/i/104422.html'))

        for i in range(page):
            getMain = self.getResponse('https://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(i+2))
            pattern = '<b>.*?<a href=(.*?) class="ulink"'
            urls = re.compile(pattern,re.S).findall(getMain)
            # 获取详细页面的url
            for url in urls:
                url = url.replace('"','')
                endUrl = "https://www.dy2018.com"+url
                html = self.getResponse(endUrl)
                self.parseHtml(html)

        self.saveFile()






if __name__ == '__main__':
    Dytt().run(1)
