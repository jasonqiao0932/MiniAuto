# encoding:utf-8
__author__ = 'gaoqiao'
'''
最近使用历史
小程序使用历史
'''
import requests

URL = "http://cloud.browser.360.cn/mp/uh"

def mp_uh():
    data = {"m":"43df2d47985708fa655ad9efd37fa6c8"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uh_his(mid):
    data = {"m":mid}
    r = requests.get(URL,data)
    try:
        result = r.json()
        #print type(result)
    except Exception as e:
        print (r.text)
    return result


def mp_uh_err_m_10010():
    '''
    mid格式不正确
    :return:
    '''
    data = {"m":"5d24d4c250def550"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uh_err_10010():
    '''
    没有m参数
    :return:
    '''
    #data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL)
    print (r.text)


if __name__ == '__main__':
    mp_uh()

