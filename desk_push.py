# encoding:utf-8
__author__ = 'gaoqiao'
import requests
import time
import hashlib

'''
app_id	    string	y	小程序ID
name	    string	y	小程序名称
appdata	    string	y	小程序数据
icon        string	n	小程序ICON
summary	    string	n	提示信息
mid	        string	n	按照mid推送时必填。多个mid用逗号分隔
start_time	string	y	开始时间：YYYY-mm-dd HH:ii
end_time	string	y	结束时间：YYYY-mm-dd HH:ii
timestamp	string	y	时间戳
md5	        string	y	签名. md5($appid+ $appdata + $summary + "desk_push" + timestamp)
'''

URL = "http://elephant.browser.360.cn?t=360live&m=desk"
t = str(int(time.time()))
tag = r'(%MidAttr|99240%=="1")||(%MidAttr|100436%=="1")'
#app_id=qh13waury22p7m8bf6
# end_time=2019-05-23+19%3A29
# icon=http%3A%2F%2Fpub-shyc2.s3.addops.soft.360.cn%2Fmini-ico%2F412689037-qh13waury22p7m8bf6-1557918489.ico
# md5=6cbdc4bcbd492e1b415087f8cd5e8d70
# msg_id=1128623760954359809
# name=%E6%B5%8B%E8%AF%95%E5%B0%8F%E7%A8%8B%E5%BA%8F001
# start_time=2019-05-23+19%3A29
# summary=%E6%A1%8C%E9%9D%A2%E6%B6%88%E6%81%AF%E5%86%85%E9%93%BE
# tag=%28%28%25360se_shiping%7C99921%25%3D%3D%221%22%29%29
# timestamp=1557919985
# title=%E6%A1%8C%E9%9D%A2%E6%B6%88%E6%81%AF%E5%86%85%E9%93%BE
# url=https%3A%2F%2Fmp.360.cn%2F%23%2Fmessage%2Ftpl
# url_type=INTERNAL


def desk_push():
    data = {"app_id":"qh6m77e64wckp9eve4",
            "name":"桌面测试test1",
            "msg_id":"33333",
            "title":"桌面消息test2",
            "url_type":"INTERNAL",
            #"url_type":"EXTERNAL",
            "url":"https://www.so.com",
            "summary":"summary",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "tag":"",
            "mid":"cq8hd68m47577ed6e4bw1c8kep29cedvaef4b47890ed65f620",
            #"mid":"9q7h2j5e839zdm7xfs0mew5m28a16132fb469be26cd13c3844",
            #"start_time":"2019-05-17 20:40",
            #"end_time":"2019-05-18 20:40",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_urltypenull():
    '''
    url_type为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "name":"王15811275036",
            "msg_id":"",
            "title":"桌面消息test",
            "url":"https://www.so.com",
            "summary":"brewrewqweqwew",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "mid":"5d24d4c250def55030efc04512461abb",
            "tag":tag,
            "start_time":"2019-04-24 22:00",
            "end_time":"2019-04-27 22:01",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_noappid():
    '''
    appid为空
    :return:
    '''
    data = {"app_id":"",
            "name":"王15811275036",
            "msg_id":"",
            "title":"桌面消息test",
            "url":"https://www.so.com",
            "summary":"brewrewqweqwew",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "mid":"5d24d4c250def55030efc04512461abb",
            "tag":tag,
            "start_time":"2019-04-24 22:00",
            "end_time":"2019-04-27 22:01",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_notitle():
    '''
    标题不能为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "name":"王15811275036",
            "msg_id":"",
            "title":"",
            "url":"https://www.so.com",
            "summary":"brewrewqweqwew",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "mid":"5d24d4c250def55030efc04512461abb",
            "tag":tag,
            "start_time":"2019-04-24 22:00",
            "end_time":"2019-04-27 22:01",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_noname():
    '''
    name或summary、icon不传，按空传
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "name":"",
            "msg_id":"",
            "title":"桌面消息test",
            "url":"https://www.so.com",
            "summary":"",
            "icon":"",
            "mid":"5d24d4c250def55030efc04512461abb",
            "tag":tag,
            "start_time":"2019-04-24 22:00",
            "end_time":"2019-04-27 22:01",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_notimestamp():
    '''
    timestamp不能为空
    {
    "code": -1,
    "msg": "timestamp不能为空",
    "data": ""
    }
    :return:
    '''
    data = {"app_id":"qhef529w9c721ne9jk",
            "name":"K歌娱乐",
            "msg_id":"",
            "title":"桌面消息test",
            "url_type":"INTERNAL",
            #"url_type":"EXTERNAL",
            "url":"https://www.so.com",
            "summary":"brewrewqweqwew",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "tag":"",
            #"mid":"c8d8457deb18e2cdafb47890ed65f620",
            "start_time":"2019-05-11 22:00",
            "end_time":"2019-05-11 22:01",
            "timestamp":"",
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["url"] + "desk_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def desk_push_md5wrong():
    '''
    签名错误
    {
    "code": -1,
    "msg": "签名错误",
    "data": ""
    }
    :return:
    '''
    data = {"app_id":"qhef529w9c721ne9jk",
            "name":"K歌娱乐",
            "msg_id":"",
            "title":"桌面消息test",
            "url_type":"INTERNAL",
            #"url_type":"EXTERNAL",
            "url":"https://www.so.com",
            "summary":"brewrewqweqwew",
            "icon":"http://p0.qhimg.com/t01eb5bbefa8501bc4d.png",
            "tag":"",
            #"mid":"c8d8457deb18e2cdafb47890ed65f620",
            "start_time":"2019-05-11 22:00",
            "end_time":"2019-05-11 22:01",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["app_id"] + data["title"] + data["summary"] + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

if __name__ == '__main__':
    desk_push()

