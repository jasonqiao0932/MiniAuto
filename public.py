# encoding:utf-8
__author__ = 'gaoqiao'
import random
import hashlib
import time

T = str(int(time.time()))
MID = "5d24d4c250def55030efc04512461abb"

def getrand():
    l = []
    while(len(l)<7):
        x = random.randrange(0,9)
        if x not in l:
            l.append(x)
    #print l
    randstr = "".join(str(i) for i in l)
    #print randstr
    return randstr

def checksign(param):
    randstr = getrand()
    key = "love_mp_interface"
    md5str = param + randstr + T + key
    sign = hashlib.md5(md5str).hexdigest()
    #print randstr,sign
    return randstr,sign

#if __name__ == '__main__':


