#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 9:35
# @Author  : zero
# @File    : challenge3_4.py.py
# @Software: PyCharm
import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   r'\[(.+)\]\s'  # 时间
                   r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   r'(\d+)\s'  # 状态码
                   r'(\d+)\s'  # 数据大小
                   r'"(.+)"\s'  # 请求头
                   r'"(.+)"'  # 客户端信息
                   )

        parsers = re.findall(pattern,logfile.read())
    return parsers

def main():
    ip_dicts = {}
    ip_dict = {}
    url_dicts = {}
    url_dict = {}
    parsers = open("nginx.log")
    for parser in parsers:
        allList = parser.split(" ")
        logTime = datetime.strptime(allList[3].
                                split("[")[1],"%d/%b/%Y:%H:%M:%S").strftime("%Y%m%d")
        if "20170111" == logTime:
            # allList[5].split("\"")[1] == "GET"
            if allList[5] == "\"GET":
                if allList[0] in ip_dicts.keys():
                    ip_dicts[allList[0]] += 1
                else:
                    ip_dicts[allList[0]] = 1
    # print(ip_dicts)
    # print(max(ip_dicts,key=ip_dicts.get),ip_dicts[max(ip_dicts,key=ip_dicts.get)])

        if allList[5].split("\"")[1] == "GET" and  allList[8] == "404":
            if allList[6] in url_dicts.keys():
                url_dicts[allList[6]] += 1
            else:
                url_dicts[allList[6]] = 1
    url_dict[max(url_dicts, key=url_dicts.get)] =url_dicts[max(url_dicts, key=url_dicts.get)]
    ip_dict[max(ip_dicts, key=ip_dicts.get)] = ip_dicts[max(ip_dicts, key=ip_dicts.get)]
    return ip_dict,url_dict

if __name__ == "__main__":
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
