# -*- coding: utf-8 -*-
__author__ = 'GQ'

import requests
import json

#uid 就是前段生成的mid，都是内部链接  都是针对mid，base64加密再md5加密
#我这边只能保证我这里写的key和secret对应就能下发成功，是否和mid中包含的app_id对应无法做判断
url="https://mp.360.cn/miniplatform/open/api/msg"
data1={
      "msg_id":"xxxxxxxxx",
      "uid":"cq8hde8f455279dwe9bc1782e12nced9ajfkb47890ed65f620",# 即mid，是通过mid+app_id混合传过来的，所以header里的X-API-KEY和加密前的key（即app_id）和secret（可以根据app_id查）一致
      "title":"小说",
      "digest":"小说",
      "click_url":"/",
}

testdata = json.dumps(data1)
#print testdata
header = {'X-API-SIGN':'3915e1acda3848bf35ca0c455690cd75','X-API-KEY':'qhef529w9c721ne9jk','X-API-TS':'1558352305'}
res = requests.post(url,verify=False,data=testdata,headers = header)

print(res.text)


# click_url=aHR0cHM6Ly93d3cueHh4LmNuL2FhYQ==&digest=aGVsbG8geHh4LCB3ZWxjb21lIHRvIG15IHdvcmxkIQ==&msg_id=MTIzMjQzMjQyMw==&title=5qCH6aKY&uid=OXFkaDlqOWU1M2J6ZW1ieDZzNW1md2JtODgzMWYxMDI5YjI2ZTM4MTRlYjg1YzMyNDI=&key=qhv6nehe97zy7s78h3&secret=b7kf2qvrmbh5skjn9yssb1pp5tfydy6c&ts=1557849600

# 线上
# click_url=SFR0cFM6Ly94eHguY24vYTFhYQ==&digest=c2Rmc2Rm5pGY6KaBMTIzJQ==&msg_id=MTExNDVhc2RmZw==&title=QVBJ5raI5oGv5qCH6aKY&uid=ZnFjaGJ2NzYxbmVlN2g4ZWU5NDcwemF5Njc1czg3ODhkaGEzODYxZGI3ZTBhNWE3NjI=&key=qhv6nehe97zy7s78h3&secret=b7kf2qvrmbh5skjn9yssb1pp5tfydy6c&ts=1558173600