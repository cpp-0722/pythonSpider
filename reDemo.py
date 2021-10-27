#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/15 10:13
    @Describe 
    @Version 1.0
"""
import re

if __name__ == '__main__':
    # pattern = '1[356789]\d{9}'
    # reInput = input("请输入：")
    #
    # result = re.search(pattern, reInput)
    #
    # if result is None:
    #     print("输入错误")
    # else:
    #     print(result.group())

    # 假设存在以下网页结构
    html = '''
        <html>
            <div class="book" id="app">
                <book><p>c语言</p></book>
                <book><p>python从入门到入坟</p></book>
                <book><p>mongoDB精选</p></book>
            </div>
        </html>
    '''

    # 1. 匹配所有的书籍
    # pattern = '<p>\w+</p>'
    # result = re.compile(pattern, flags=re.S).findall(html)
    # # 字符串的切片处理
    # result_1 = [x[3:-4] for x in result]
    # print(result_1)

    # 2. 匹配所有的书籍
    # .  匹配任意字符，除换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符串
    # 贪婪匹配  -> 在一次匹配中尽可能的多匹配
    # 2.1 从根节点出发开始匹配
    # pattern = '<div.*<book><p>(.*)</p>'                               # [mongoDB精选]
    # pattern = '<div.*<book><p>(.*)</p>.*<p>(.*)</p>.*<p>(.*)</p>'     # [(c语言, python从入门到入坟, mongoDB精选)]
    pattern = '<book><p>(.*)</p>.*<p>(.*)</p>.*<p>(.*)</p>'           # [(c语言, python从入门到入坟, mongoDB精选)]
    result = re.compile(pattern, flags=re.S).findall(html)
    print(result)

