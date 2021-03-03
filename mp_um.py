# encoding:utf-8
__author__ = 'gaoqiao'
'''
桌面快捷方式、push接收状态修改、桌面消息push
m	string	y	用户标识
i	string	n	appId
t	int	y	1--桌面快捷方式；2--push消息；3--桌面push消息；4--侧边栏小程序
v	int	y	1–开启；0--关闭
'''
import requests

URL = "http://cloud.browser.360.cn/mp/um"

def mp_um():
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"3","v":"1","i":""}
    r = requests.get(URL,data)
    print (r.text)


def mp_um_desklink():
    '''
    桌面快捷方式
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"1","v":"1","i":"qh171xvex265trv9uk"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_push():
    '''
    侧边栏push消息
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"2","v":"0","i":"qhbxapxh5jx78hk2qp"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_deskpush():
    '''
    桌面push消息
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"3","v":"1","i":"123123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_sidebarpush():
    '''
    侧边栏小程序
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"4","v":"0","i":"qhef529w9c721ne9jk"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_desklink_return(mid,v,appid):
    '''
    桌面快捷方式开关调用函数
    :return:
    '''
    data = {"m":mid,"t":"1","v":v,"i":appid}
    r = requests.get(URL,data)
    print (r.text)
    result = r.json()
    return result["errno"]


def mp_um_push_return(mid,v,appid):
    '''
    侧边栏push消息调用函数
    :return:
    '''
    data = {"m":mid,"t":"2","v":v,"i":appid}
    r = requests.get(URL,data)
    print (r.text)
    result = r.json()
    return result["errno"]


def mp_um_deskpush_return(mid,v):
    '''
    桌面push消息调用函数
    :return:
    '''
    data = {"m":mid,"t":"3","v":v,"i":"123123"}
    r = requests.get(URL,data)
    print (r.text)
    result = r.json()
    return result["errno"]


def mp_um_nomid():
    '''
    mid不存在,返回10010
    :return:
    '''
    data = {"m":"","t":"2","v":"1","i":"123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_midwrong():
    '''
    mid格式错误,返回10010
    :return:
    '''
    data = {"m":"5d24d4c250de","t":"2","v":"0","i":"123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_vwrong():
    '''
    设置状态不是1/0,返回10010
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"2","v":"33","i":"123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_nov():
    '''
    v不存在,桌面push消息会影响
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"3","i":"123"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_noappid():
    '''
    appid缺失，桌面push消息不影响，push和桌面快捷方式不会写入redis
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"1","v":"1"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_appidwrong():
    '''
    appid长度超过255,10010
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"2","v":"1","i":"4614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160461446175848294016046144617584829401604614461758482940160"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_not():
    '''
    t不存在,不写入redis,返回10010
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","v":"1","i":"111aaa"}
    r = requests.get(URL,data)
    print (r.text)

def mp_um_twrong():
    '''
    t不在取值范围,不写入redis，返回10010
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","t":"11","v":"1","i":"adsadsd"}
    r = requests.get(URL,data)
    print (r.text)

if __name__ == '__main__':
    mp_um_desklink()
    #mp_um_sidebarpush()
    #mp_um_deskpush()
    #mp_um_push()



