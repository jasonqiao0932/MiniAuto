# encoding:utf-8
__author__ = 'gaoqiao'
'''
清空小程序使用历史
'''
import requests

URL = "http://cloud.browser.360.cn/mp/ue"

def mp_ue(mid):
    data = {"m":mid}
    r = requests.get(URL,data)
    #print r.text
    return r.text

def mp_ue_suc():
    data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL,data)
    print (r.text)

def mp_ue_midwrong():
    '''
    mid格式错误
    :return:
    '''
    data = {"m":"5d24d4c250def550"}
    r = requests.get(URL,data)
    print (r.text)

def mp_ue_nomid():
    '''
    没有mid
    :return:
    '''
    r = requests.get(URL)
    print (r.text)

if __name__ == '__main__':
    mp_ue_suc()