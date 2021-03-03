# encoding:utf-8
__author__ = 'gaoqiao'
'''
小程序模糊查询
'''
import requests

URL = "http://cloud.browser.360.cn/mp/q"

def mp_q():
    data = {"m":"c8d8457deb18e2cdafb47890ed65f620","q":"测试"}
    r = requests.get(URL,data)
    print r.text

def mp_q_err_():
    '''
    m参数格式不正确
    :return:
    '''
    data = {"m":"5d24d4c250def55030","q":""}
    r = requests.get(URL,data)
    print r.text

def mp_q_err():
    '''
    m参数不存在
    :return:
    '''
    data = {"q":""}
    r = requests.get(URL,data)
    print r.text

if __name__ == '__main__':
    mp_q()
