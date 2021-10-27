#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/15 9:04
    @Describe 
    @Version 1.0
"""
import requests
import random
import json

if __name__ == '__main__':
    with open("proxies.json", "r", encoding="utf=8") as f:
        content = f.read()

    data = json.loads(content)
    # print(data)

    random_index = random.randint(0, len(data['delegate']) - 1)

    url = "http://www.baidu.com"

    proxies = data['delegate'][random_index]
    response = requests.get(url=url, proxies=proxies)
    proxies['count'] = proxies['count'] + 1
    print(proxies['count'])
