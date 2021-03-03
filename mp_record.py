# encoding:utf-8
__author__ = 'gaoqiao'
'''
记录用户url访问历史&创建快捷方式

请求参数:
m	string	y	用户标识, mid
u	string	y	加密后的 url
appid	string	y	appid
cb	string	n	jsonp标识, 不传则返回json数据

返回：
appid	小程序id
logo	小程序logo 地址
v_ret	状态 0-无效url 1-有效url且首次保存 2-有效url但用户已保存过
ani_switch	动画开关 0, 1
cre_desk	桌面快捷方式:0-不创建 1-提示确认后创建 2-直接创建
desk_icon	桌面快捷方式图标地址
desk_ani	桌面快捷方式动画资源地址
desk_id     桌面快捷方式id
desk_png    桌面快捷方式PNG资源
desk_title	桌面快捷方式文件名
desk_content	桌面快捷方式点击动画时访问的URL
ani_content	桌面快捷方式的内容
'''
import requests

URL = "http://cloud.browser.360.cn/mp/record"
'''
http://cloud.browser.360.cn/mp/record?u=G2OHxu3VXTLdQPPsQxj5ATx%2bBEw3wOQCH2JgwEPh0XsXOBnQMGXk%2fLSqOT31zAmb&m=5d24d4c250def55030efc04512461abb&appid=qh4brnqw7ecend3byt
'''

def mp_record():
    data = {"m":"5d24d4c250def55030efc04512461abb","u":"4F2Ou9kv+crOu4N4iCsXGw==","appid":"qhbxapxh5jx78hk2qp"}
    r = requests.get(URL,data)
    print (r.text)

def mp_record_return(mid,url,appid):
    data = {"m":mid,"u":url,"appid":appid}
    r = requests.get(URL,data)
    #print r.text
    result = r.json()
    return result["appid"]

def mp_record_succ_1():
    data = {"m":"5d24d4c250def55030efc04512461abb","u":"xWLdU2hmXKfvPLiIknthuEtF2c7sEyn/","appid":"qhed99vkse1v2zzw67"}
    r = requests.get(URL,data)
    print (r.text)

def mp_record_succ_2():
    data = {"m":"5d24d4c250def55030efc04512461abb","u":"xWLdU2hmXKdBseHPoWOxE6OZOuDkGo+x","appid":"qhacr52yzpkp4wcy3u"}
    r = requests.get(URL,data)
    print (r.text)

def mp_record_mwrong():
    '''
    mid格式不对，没有匹配上
    :return:
    '''
    data = {"m":"5d24d4c250def55030e","u":"G2OHxu3VXTLdQPPsQxj5ATx+BEw3wOQCH2JgwEPh0XsXOBnQMGXk/LSqOT31zAmb","appid":"qh4brnqw7ecend3byt"}
    r = requests.get(URL,data)
    print (r.text)

def mp_record_urlwrong():
    '''
    url没有匹配上
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","u":"G2OHxu3VXTLdQPPsQxj5ATx+BEw3wOQCH2Jg","appid":"qh4brnqw7ecend3byt"}
    r = requests.get(URL,data)
    print (r.text)

def mp_record_appidwrong():
    '''
    appid没有匹配上
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","u":"G2OHxu3VXTLdQPPsQxj5ATx+BEw3wOQCH2JgwEPh0XsXOBnQMGXk/LSqOT31zAmb","appid":"123123213"}
    r = requests.get(URL,data)
    print (r.text)

if __name__ == '__main__':
    mp_record()

