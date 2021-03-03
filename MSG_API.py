# encoding:utf-8
__author__ = 'gaoqiao'
import requests
import hashlib
import base64
import json
import time
import collections

URL = "https://mp.360.cn/miniplatform/open/api/msg"
DATA = {
      "msg_id":"43412312312",
      "uid":"cq8hde8f455279dwe9bc1782e12nced9ajfkb47890ed65f620",# 即mid，是通过mid+app_id混合传过来的，所以header里的X-API-KEY和加密前的key（即app_id）和secret（可以根据app_id查）一致
      "title":"小说",
      "digest":"小说",
      "click_url":"   index.html   ",
}
APPID = "qhef529w9c721ne9jk"
t = str(int(time.time()))
SECRET = "d8m3sp2hevah7z843pehs4fcutfx57rk"

def msg_api():
    data_base_t = sorted(DATA.items(),key=lambda x:x[0])
    data_base = collections.OrderedDict(data_base_t)
    for key,value in DATA.items():
        data_base[key] = base64.b64encode(value)
    sign = checkpost(data_base)
    header = {"X-API-SIGN":sign,"X-API-KEY":APPID,"X-API-TS":t}
    r = requests.post(URL,json=DATA,headers=header,verify=False)
    print r.text

def checkpost(data):
    l1 = []
    for key in data:
        poststr = key + "=" + data[key]
        l1.append(poststr)
    post_data = "&".join(l1)
    post_data = post_data + "&key=" + APPID + "&secret=" + SECRET + "&ts=" + t
    print post_data
    post_data = hashlib.md5(post_data).hexdigest()
    return post_data

if __name__ == '__main__':
    msg_api()

