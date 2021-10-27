#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/8 9:01
    @Describe 
    @Version 1.0
"""
# import random
#
# import requests
#
# SORT = {
#     0: "recommend",
#     1: "time",
#     2: "rank"
# }
#
# HEADERS = [
#     {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#      "Cookie":"ll='118194'; bid=mBlFaxGZpKM; __gads=ID=08b0095e22cae01c-2248465e1acb00d7:T=1629876649:RT=1629876649:S=ALNI_MYq8qn6iUyDpzLxHvmJ4QEKKE-fkQ; _vwo_uuid_v2=D56227C4995C0A96AA8933DC1B18E17F4|4ab0008f20e545075808da0b90727a5a; __yadk_uid=vyggnD4fGwkYaQs23G31cFREfyx3X3h3; douban-fav-remind=1; gr_user_id=cbcdd90a-c11e-4e45-97ed-c6ac0c735539; viewed='27591387_27093751'; dbcl2='215769387:q9xlHXY4d0w'; ck=eOlW; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1633655689%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.643324723.1629876648.1632532740.1633655689.7; __utmb=30149280.0.10.1633655689; __utmc=30149280; __utmz=30149280.1633655689.7.6.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.822107377.1629876648.1632532740.1633655689.6; __utmb=223695111.0.10.1633655689; __utmc=223695111; __utmz=223695111.1633655689.6.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=25a26d936debae86.1629876648.6.1633655721.1632532740."},
#
# ]
#
# url = "https://movie.douban.com/j/search_subjects?type=tv&tag=热门" \
#                    "&sort=recommend&page_limit=20&page_start={}"
#
# def get_response( url):
#     """发送请求并获取响应"""
#     return requests.get(url=url, headers=HEADERS[0])
#
#
# if __name__ == '__main__':
#     print(get_response(url).status_code)
# import re
#
# z = ''
# url = "https://careers.tencent.com/jobdesc.html?postId=1304767708239241216"
#
# s = re.findall("\d+",url)[0]
# print(s)

# i= "ad\u3000qw"
# print(i.replace('\\u3000',''))

list01 = [1,2,3,4,5]

for index,i in enumerate(list01):
    print(index)
    print(i)


