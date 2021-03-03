# encoding:utf-8
__author__ = 'gaoqiao'
import requests

URL = "https://mp.360.cn/miniplatform/open/oauth2/auth_code"
field = ["open_id"]
DATA = {
    "app_id":"qheujs3qzc611fceaf",
    "qid":"4569208",
    "auth_fields":field
}

def auth_code():
    header = {"Content-Type":"application/json","Connection":"close"}
    r = requests.post(URL,json=DATA,headers=header,verify=False)
    print r.text
    result = r.json()
    authcode = result["auth_code"]
    #print authcode
    return authcode,DATA["app_id"]

if __name__ == '__main__':
    auth_code()

