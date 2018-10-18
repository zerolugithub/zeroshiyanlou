#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Parameter Error")
    sys.exit()

try:
    global salary
    salary = int(sys.argv[1])
except:
    print("Parameter Error")
    sys.exit()
ynsje = salary - 3500
def nS(ys,rate,kouchushu):
    return ys* rate -kouchushu
    
if ynsje <= 1500:
    ns = nS(ynsje,0.03,0)
elif 1500 < ynsje <= 4500:
    ns = nS(ynsje,0.1,105)
elif 4500 < ynsje <= 9000:
    ns = nS(ynsje,0.2,555)
elif 9000 < ynsje <= 35000:
    ns = nS(ynsje,0.25,1005)
elif 35000 < ynsje <= 55000:
    ns = nS(ynsje,0.3,2755)
elif 55000 < ynsje <= 80000:
    ns = nS(ynsje,0.35,5505)
else:
    ns = nS(ynsje,0.45,13505)

print("{:.2f}".format(ns))
