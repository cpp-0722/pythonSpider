#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/22 9:19
    @Describe 
    @Version 1.0
"""

import re
import time

import requests
import random


class Proxies():
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

    def getResponse(self, url):
        random_index = random.randint(0, len(self.headers) - 1)
        return requests.get(url, self.headers[random_index]).content.decode()

    def parseHtml(self, context):
        pattern = '<tr>.*?<td data-title="IP">(.*?)</td>.*?title="PORT">(.*?)</td>.*?title="类型">(.*?)</td>'
        result = re.compile(pattern, re.S).findall(context)
        for d in result:
            proxies = dict()
            proxies[d[2]] = d[0] + ":" + d[1]
            proxies['count'] = 0
            self.datas.append(proxies)

        print(self.datas)

    def saveFile(self):
        pass

    def run(self, page=5):
        for i in range(page):
            html = self.getResponse(self.url.format(i + 1))
            self.parseHtml(html)
            time.sleep(1)


if __name__ == '__main__':
    Proxies().run()
