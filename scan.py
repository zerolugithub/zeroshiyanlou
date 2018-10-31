#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:32
# @Author  : zero
# @File    : scan.py
# @Software: PyCharm

import socket
import sys

if len(sys.argv) != 5:
    print("Parameter Error")
    sys.exit()
portList = []
try :
    host = sys.argv[sys.argv.index("--host") + 1]
    port = sys.argv[sys.argv.index("--port") + 1]
    if len(host.split(".")) != 4:
        raise Exception
except:
    print("Parameter Error")
    sys.exit()
if port.endswith("-") or port.startswith("-"):
    print("Parameter Error")
    sys.exit()
if port.find("-") != -1:
    ports = port.split("-")
    try:
        for i in range(int(ports[0]), int(ports[1]) + 1):
            portList.append(i)
    except:
        print("Paramter Error")
        sys.exit()
else:
    try:
        portList.append(int(port))
    except:
        print("Parameter Error")
        sys.exit()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for port in portList:
        try:
            s.connect((host, port))
            s.settimeout(0.1)
            print("{} open {}".format(host,port))
        except TimeoutError:
            print("{} closed {}".format(host, port))
    s.close()