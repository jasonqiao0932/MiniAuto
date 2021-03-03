# encoding:utf-8
__author__ = 'gaoqiao'
'''
删除单个小程序使用历史
'''
import requests
import random
import time
import hashlib

T = str(int(time.time()))
MID = "5d24d4c250def55030efc04512461abb"
URL = "http://cloud.browser.360.cn/mp/uea"

def mp_uea_pc():
    randstr,sign = checksign()
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhxy48hzcbbd3qpy2e","rand":randstr,"t":T,"sign":sign}
    r = requests.get(URL,data)
    print r.text

def mp_uea_web():
    randstr,sign = checksign()
    header = {"Referer":"mp.360.cn"}
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhk1cpjqv3s3nbashw","rand":randstr,"t":T}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_uea_randEmpty():
    '''
    rand为空
    :return:auth error
    '''
    header = {"Referer":"mp.360.cn"}
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhv3c29xffbj3xvznh","rand":"","t":T}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_uea_TEmpty():
    '''
    t为空
    :return:auth error
    '''
    header = {"Referer":"mp.360.cn"}
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhv3c29xffbj3xvznh","rand":"123123","t":""}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_uea_RefererEmpty():
    '''
    Referer为空
    :return:auth error
    '''
    randstr,sign = checksign()
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhv3c29xffbj3xvznh","rand":randstr,"t":T}
    r = requests.get(URL,data)
    print r.text

def mp_uea_RefererWrong():
    '''
    Referer不是mp.360.cn
    :return:auth error
    '''
    header = {"Referer":"browser.360.cn"}
    randstr,sign = checksign()
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhv3c29xffbj3xvznh","rand":randstr,"t":T}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_uea_signerror():
    '''
    签名错误
    :return: auth error
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qhv7au3a6nkz4s6mf7"}
    r = requests.get(URL,data)
    print r.text

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

def checksign():
    randstr = getrand()
    key = "love_mp_interface"
    md5str = MID + randstr + T + key
    sign = hashlib.md5(md5str).hexdigest()
    #print randstr,sign
    return randstr,sign

if __name__ == '__main__':
    #mp_uea_pc()
    mp_uea_web()
    #mp_uea_RefererWrong()
