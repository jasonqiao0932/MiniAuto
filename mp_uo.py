# encoding:utf-8
__author__ = 'gaoqiao'
'''
调整侧边栏顺序
调整小程序侧边栏顺序
侧边栏增加、删除、点击强制下发小程序等影响侧边栏小程序数量、顺序的行为都需要把已经添加到侧边栏的小程序按照自上而下的顺序发送到服务端
'''
import requests

URL = "http://cloud.browser.360.cn/mp/uo"

def mp_uo():
    data = {"m":"5d24d4c250def55030efc04512461abb","i":"qhv6nehe97zy7s78h3,qh6846ftpz6akac91z,qheejtaunxfk8pj2p9,qh92jt3rscber1dhtp,qhbxapxh5jx78hk2qp,qheujs3qzc611fceaf"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uo_return(mid,order):
    data = {"m":mid,"i":order}
    r = requests.get(URL,data)
    #print r.text
    return r.text


def mp_uo_midwrong():
    '''
    mid不足32位，校验失败
    :return:
    '''
    data = {"m":"5d24d4c250def5503","i":"123,abcd,qh375fhhuhxrvh96t7,aaaa"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uo_nomid():
    '''
    没有mid
    :return:
    '''
    data = {"i":"abcd1,qh375fhhuhxrvh96t7,aaaa,123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uo_noappid():
    '''
    没有appid
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL,data)
    print (r.text)

def mp_uo_appidwrong():
    '''
    appid超过255位
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","i":"123,abcd,qh375fhhuhxrvh96t7,aaaa,4614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160"}
    r = requests.get(URL,data)
    print (r.text)

if __name__ == '__main__':
    mp_uo()

