# encoding:utf-8
__author__ = 'gaoqiao'
import requests
import time
import hashlib

'''
app_name	Side_Play: 兼容追剧窗口，小程序不需要这个字段
app_id		app_id，小程序用到。老版本追剧忽略。
showtype	样式：1--红点，2--咨询，3-小说，4-视频游戏
theme		弹窗标题
theme_img	弹窗logo
title		标题
abstract	摘要
img		    图片地址
url		    落地页url
tag	        按照tag推送时必填。详见

mid	            按照mid推送时必填。多个mid用逗号分隔
start_time	    开始时间：YYYY-mm-dd HH:ii
end_time	    结束时间：YYYY-mm-dd HH:ii
expire_hours    消息保留时间， 0-立即发送 非0 - 在指定小时内，用户如果上线，而没有发送过，会给他们发送消息
expire_minutes  消息保留时间， 0-立即发送 非0 - 在指定分钟内，用户如果上线，而没有发送过，会给他们发送消息
timestamp	    时间戳
md5	            签名. md5($title + $abstract + $img + $url + 'sd_push' + timestamp)
'''

URL = "http://elephant.browser.360.cn?t=360live&m=sidebar"
t = str(int(time.time()))
tag = r'(%MidAttr|99240%=="1")||(%MidAttr|100436%=="1")'
#&lt; &gt;  \  &amp;  &#39;  &#34;
def sidebar_push():
    data = {"app_id":"qh6m77e64wckp9eve4",
            "app_name":"&lt; &gt;  \  &amp;  &#39;  &#34;",
            "showtype":"2",
            "msg_id":"&lt; &gt;  \  &amp;  &#39;  &#34;",
            "theme":"&lt; &gt;  \  &amp;  &#39;  &#34;",
            #"theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"&lt; &gt;  \  &amp;  &#39;  &#34;弹窗测试超过15个字符或汉字",
            "abstract":"弹窗测试超过15个字符或汉字，展示情况；弹窗测试超过15个字符或汉字，展示情况；弹窗测试超过15个字符或汉字，展示情况；",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png?eweqwewqe&dsadsad!@#@#%$&^*&(*(",
            "btntext":"点击预览",
            "url_type":"INTERNAL",
            #"url_type":"EXTERNAL",
            "url":"http://www.baidu.com",
            #"mid":"c8d8457deb18e2cdafb47890ed65f620",
            #"mid":"9qdh9j9e53bzembx6s5mfwbm8831f1029b26e3814eb85c3242",
            #"tag":tag,
            #"start_time":"2019-05-17 20:01",
            #"end_time":"2019-05-17 22:01",
            #"expire_hours":"1",
            #"expire_minutes":"",
            "m2":"43e66c7c1b8fa0c2d71ce0f61f98be28ad5a65f52bbb",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["img"] + data["url"] + "sd_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def sidebar_push_notitle():
    '''
    标题为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "app_name":"DB",
            "msg_id":"aaaa",
            "showtype":"2",
            "theme":"abcd",
            "theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"",
            "abstract":"aaaaa",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "url_type":"INTERNAL",
            "url":"http://www.baidu.com",
            "tag":"",
            "mid":"c8d8457deb18e2cdafb47890ed65f620",
            "start_time":"",
            "end_time":"2019-04-16 10:01",
            "expire_hours":"1",
            "expire_minutes":"0",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["img"] + data["url"] + "sd_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def sidebar_push_notype():
    '''
    showtype不能为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "app_name":"DB",
            "showtype":"",
            "theme":"abcd",
            "theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"abcd",
            "abstract":"aaaaa",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "url":"http://www.baidu.com",
            "tag":"",
            "mid":"5d24d4c250def55030efc04512461abb",
            "start_time":"2019-04-16 10:00",
            "end_time":"2019-04-16 10:01",
            "expire_hours":"0",
            "expire_minutes":"0",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["img"] + data["url"] + "sd_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def sidebar_push_nourl():
    '''
    url不能为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "app_name":"DB",
            "showtype":"2",
            "theme":"abcd",
            "theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"abcd",
            "abstract":"aaaaa",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "url":"",
            "tag":"",
            "mid":"5d24d4c250def55030efc04512461abb",
            "start_time":"2019-04-16 10:00",
            "end_time":"2019-04-16 10:01",
            "expire_hours":"0",
            "expire_minutes":"0",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["img"] + data["url"] + "sd_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def sidebar_push_notimestamp():
    '''
    时间戳不能为空,timestamp不能为空
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "app_name":"DB",
            "showtype":"2",
            "theme":"abcd",
            "theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"abcd",
            "abstract":"aaaaa",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "url":"http://www.baidu.com",
            "tag":"",
            "mid":"5d24d4c250def55030efc04512461abb",
            "start_time":"2019-04-16 10:00",
            "end_time":"2019-04-16 10:01",
            "expire_hours":"0",
            "expire_minutes":"0",
            "timestamp":"",
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["img"] + data["url"] + "sd_push" + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

def sidebar_push_md5wrong():
    '''
    签名错误
    :return:
    '''
    data = {"app_id":"qhuq8vrnmcpbr3urpm",
            "app_name":"DB",
            "showtype":"2",
            "theme":"abcd",
            "theme_img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "title":"abcd",
            "abstract":"aaaaa",
            "img":"http://p0.qhimg.com/t0148296a34102efb95.png",
            "url":"http://www.baidu.com",
            "tag":"",
            "mid":"5d24d4c250def55030efc04512461abb",
            "start_time":"2019-04-16 10:00",
            "end_time":"2019-04-16 10:01",
            "expire_hours":"0",
            "expire_minutes":"0",
            "timestamp":t,
            "md5":""}
    md5 = hashlib.md5(data["title"] + data["abstract"] + data["url"] + t).hexdigest()
    data["md5"] = md5
    r = requests.post(URL,data)
    print r.text

if __name__ == '__main__':
    sidebar_push()

