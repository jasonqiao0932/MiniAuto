# encoding:utf-8
__author__ = 'gaoqiao'
'''
获取桌面消息开关状态
'''
import requests

URL = "http://cloud.browser.360.cn/mp/ups"

def mp_ups():
    data = {"m":"c8d8457deb18e2cdafb47890ed65f620"}
    r = requests.get(URL,data)
    print (r.text)

def mp_ups_return(mid):
    data = {"m":mid}
    r = requests.get(URL,data)
    print (r.text)
    result = r.json()
    return result

def mp_ups_midwrong():
    '''
    mid不满足32位，默认返回关闭状态
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc"}
    r = requests.get(URL,data)
    print (r.text)

def mp_ups_nomid():
    '''
    不传mid，默认返回关闭状态
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL)
    print (r.text)

if __name__ == '__main__':
    mp_ups()

