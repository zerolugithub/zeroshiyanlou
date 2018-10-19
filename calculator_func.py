#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Parameter Error")
    sys.exit()
salDict = {}

for arg in sys.argv[1:]:
    gh,sal = arg.split(":")
    try:
        newSal = int(sal)
    except:
        print("Parameter Error")
        sys.exit()
    salDict[gh]=newSal
def ynssde(ynse,rate,kcs):
    return ynse*rate - kcs
def shSal(gh,newSal):
    if newSal <= 3500:
     	value = newSal*(1-0.165)
    else:
        ynse = newSal*(1-0.165)-3500
        if 0 < ynse <= 1500:
            value = newSal*(1-0.165)-ynssde(ynse,0.03,0)
        elif 1500 < ynse <= 4500:
            value = newSal*(1-0.165)-ynssde(ynse,0.1,105)
        elif 4500 < ynse <= 9000:
            value  = newSal*(1-0.165)-ynssde(ynse,0.2,555)
        elif 9000 < ynse <= 35000:
            value  = newSal*(1-0.165)-ynssde(ynse,0.25,1005)
        elif 35000 < ynse <= 55000:
            value  = newSal*(1-0.165)-ynssde(ynse,0.3,2755)
        elif 55000 < ynse <= 80000:
            value  = newSal*(1-0.165)-ynssde(ynse,0.35,5505)
        else:
            value  = newSal*(1-0.165)-ynssde(ynse,0.45,13505)

    print("{}:{:.2f}".format(gh,value))

for key,value in salDict.items():
    shSal(key,value)
