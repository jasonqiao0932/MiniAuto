# encoding:utf-8
__author__ = 'gaoqiao'
import requests
import auth_code
import json

authcode,appid = auth_code.auth_code()
URL = "https://mp.360.cn/miniplatform/open/app_review/" + appid
usersize =  {
        "enableLargeWindow": True,
        "showRefreshButton": True,
        "windowWidth": 1138,
        "windowHeight": 640,
        "minWindowWidth": 600,
        "minWindowHeight": 600,
        "enableResize": True
    }

filepath = unicode(r"E:\test\xiaochengxu\zip1.zip","utf-8")
appfile = open(filepath,"rb")
#print appfile
file = {"file":appfile}
DATA = {
    "app_version":"aaaaa",
    "release_note":"test",
    "local_conf":"",
    "qid":"4569208",
    "auth_code":auth_code
}
local_conf = json.dumps(usersize)
#print local_conf
DATA["local_conf"] = local_conf

def upload_size():
    r = requests.post(URL,DATA,files=file,verify=False)
    print r.text

if __name__ == '__main__':
    upload_size()

