# encoding:utf-8
__author__ = 'gaoqiao'
'''
上报小程序使用历史
客户端打开小程序时，上报小程序使用历史
m	string	y	用户标识
a	string	y	appId
'''
import requests

URL = "http://cloud.browser.360.cn/mp/uu"

def mp_uu():
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"qheujs3qzc611fceaf"}
    r = requests.get(URL,data)
    print (r.text)
    #result = r.json()
    #return result[""]

def mp_uu_his(mid,appid):
    data = {"m":mid,"a":appid}
    r = requests.get(URL,data)
    #print r.text
    return r.text

def mp_uu_nomid():
    '''
    mid参数不存在
    :return:
    '''
    data = {"a":"123123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uu_noappid():
    '''
    appid参数不存在
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uu_midwrong():
    '''
    mid格式错误，不是32位
    :return:
    '''
    data = {"m":"5d24d4c250def550","a":"123123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uu_appidwrong():
    '''
    appid格式错误,大于255
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","a":"4614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160"}
    r = requests.get(URL,data)
    print (r.text)

if __name__ == '__main__':
    mp_uu()

