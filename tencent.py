#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/8 9:30
    @Describe 
    @Version 1.0
    work["PostURL"]
    https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1633658207461&postId=1304767708239241216&language=zh-cn

    https://careers.tencent.com/jobdesc.html?postId=1304767708239241216

    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1633661333632&countryId=&cityId=&bgIds=&productId=&categoryId=40002001,40002002&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn

    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1633661758847&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn
    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1633661822387&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=3&pageSize=10&language=zh-cn&area=cn
"""
import re

import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Cookie": "pgv_pvid=9528118900; _ga=GA1.2.1736428041.1633498322; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c54165318835-018148a7524d2f-c343365-1382400-17c54165319c3f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%7D%2C%22%24device_id%22%3A%2217c54165318835-018148a7524d2f-c343365-1382400-17c54165319c3f%22%7D; _gcl_au=1.1.1761246979.1633498325"}


def getResponse(url):
    return requests.get(url, headers=HEADERS).content.decode()


def serveData(temp):
    works = json.loads(temp)
    # 2. 遍历数据
    for work in works['Data']["Posts"]:

        s = re.findall("\d+", work["PostURL"])[0]

        drs = json.loads(getResponse('https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1633658207461&postId={}&language=zh-cn'.format(s)))["Data"]
        tem = dict()
        tem['工作岗位'] = drs['RecruitPostName']
        tem['发布时间'] = drs['LastUpdateTime']
        tem['岗位性质'] = drs['CategoryName']
        tem['工作地点'] = drs['LocationName']
        tem['工作要求'] = drs['Responsibility']
        tem['工作职责'] = drs['Requirement']
        datas.append(tem)


        # tem = dict()
        # tem['工作岗位'] = work['RecruitPostName']
        # tem['发布时间'] = work['LastUpdateTime']
        # tem['岗位性质'] = work['CategoryName']
        # tem['工作地点'] = work['LocationName']
        # tem['工作要求'] = work['Responsibility']
        # # tem['工作职责'] = work['Requirement']
        # datas.append(tem)

    return datas


def save_file(data):
    datas = json.dumps(data, indent=4, ensure_ascii=False)
    with open("./data/tencent.txt", "w", encoding="utf-8") as f:
        f.write(datas)


if __name__ == '__main__':
    n = 2
    datas = []

    url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1633656696118&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
    temp = getResponse(url)
    data = serveData(temp)
    save_file(datas)

