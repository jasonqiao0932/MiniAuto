# encoding:utf-8
__author__ = 'gaoqiao'
'''
消息操作(撤销)
'''
import requests
import time
import hashlib

URL = "http://elephant.browser.360.cn?t=360live&m=actionpush"
time = str(int(time.time()))

def msg_delete():
    data = {
        "appid":"qhef529w9c721ne9jk",
        "action":"item/delete",
        "cid":"138778",
        #"isEnforce":"1",
        "timestamp":time,
        "md5":""
    }
    md5 = hashlib.md5((data["appid"] + data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def msg_delete_noappid():
    '''
    appid为空
    :return:
    '''
    data = {
        "appid":"",
        "action":"item/delete",
        "cid":"138743",
        "timestamp":time,
        "md5":""
    }
    md5 = hashlib.md5((data["appid"] + data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def msg_delete_noaction():
    '''
    action为空
    :return:
    '''
    data = {
        "appid":"qhef529w9c721ne9jk",
        "action":"",
        "cid":"138743",
        "timestamp":time,
        "md5":""
    }
    md5 = hashlib.md5((data["appid"] + data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def msg_delete_nocid():
    '''
    cid为空
    :return:
    '''
    data = {
        "appid":"qhef529w9c721ne9jk",
        "action":"item/delete",
        "cid":"",
        "timestamp":time,
        "md5":""
    }
    md5 = hashlib.md5((data["appid"] + data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def msg_delete_notime():
    '''
    time为空
    :return:
    '''
    data = {
        "appid":"qhef529w9c721ne9jk",
        "action":"item/delete",
        "cid":"138743",
        "timestamp":"",
        "md5":""
    }
    md5 = hashlib.md5((data["appid"] + data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def msg_delete_signwrong():
    '''
    sign错误
    :return:
    '''
    data = {
        "appid":"qhef529w9c721ne9jk",
        "action":"item/delete",
        "cid":"138743",
        "timestamp":time,
        "md5":""
    }
    md5 = hashlib.md5((data["cid"] + data["action"] + "action_push_secret" + data["timestamp"])).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

if __name__ == '__main__':
    msg_delete()

