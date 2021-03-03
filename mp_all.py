# encoding:utf-8
__author__ = 'gaoqiao'
import requests

URL = "http://cloud.browser.360.cn/mp/all"
DATA = {"m":"5d24d4c250def55030efc04512461abb","page":"1","per_page":"100"}

def mp_all():
    r = requests.get(URL,DATA,verify=False)
    print r.text

def mp_all_page():
    data = {"m":"5d24d4c250def55030efc04512461abb","page":"3","per_page":"1"}
    r = requests.get(URL,data)
    print r.text

def mp_all_nom():
    '''
    mid为空，返回10010，参数错误
    :return:
    '''
    data = {"page":"3","per_page":"1"}
    r = requests.get(URL,data)
    print r.text


def mp_all_mwrong():
    '''
    mid错误，返回10010，参数错误
    :return:
    '''
    data = {"m":"132132","page":"3","per_page":"1"}
    r = requests.get(URL,data)
    print r.text


if __name__ == '__main__':
    mp_all()

