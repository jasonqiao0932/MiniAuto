# encoding:utf8
__author__ = 'gaoqiao'
'''
小程序搜索列表
'''

import requests
import redis_clear
import time

searchlist = redis_clear.get_zset("pre_mp_search_key")

URL = "http://cloud.browser.360.cn/mp/keys"
DATA = {"m":"5d24d4c250def55030efc04512461abb","lasttime":"1563445108","cb":"aaaa"}

def mp_keys():
    r = requests.get(URL,DATA)
    print r.text

def mp_keys_all():
    '''
    返回所有支持搜索的小程序列表
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","lasttime":"0","cb":"aaaa"}
    r = requests.get(URL,data)
    print r.text

def mp_keys_greaterthantimestamp():
    '''
    lasttime>timestamp
    请求时间大于小程序更新时间，不会更新
    :return:
    '''
    greatetime,lesstime = changetimestamp()
    data = {"m":"5d24d4c250def55030efc04512461abb","lasttime":greatetime,"cb":"aaaa"}
    r = requests.get(URL,data)
    print r.text

def mp_keys_lessthantimestamp():
    '''
    lasttime<timestamp
    请求时间小于小程序更新时间，返回有变化的搜索小程序
    :return:
    '''
    greatetime,lesstime = changetimestamp()
    data = {"m":"5d24d4c250def55030efc04512461abb","lasttime":lesstime,"cb":"aaaa"}
    r = requests.get(URL,data)
    print r.text

def mp_keys_nomid():
    '''
    mid不满足32位或为空
    aaaa({"errmsg":"参数错误","errno":10010})
    :return:
    '''
    data = {"m":"12312321","lasttime":"0","cb":"aaaa"}
    r = requests.get(URL,data)
    print r.text

def mp_keys_nolasttime():
    '''
    lasttime为空，不影响返回，返回所有搜索列表
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","lasttime":"&","cb":"~!@#$%^&&*"}
    r = requests.get(URL,data)
    print r.text

def timetotimestamp():
    t = "2019-01-01 23:23:23"
    timearray = time.strptime(t,"%Y-%m-%d %H:%M:%S")  #转换为时间数组
    #print timearray
    timestamp = int(time.mktime(timearray))
    print timestamp
    return timestamp

def changetimestamp():
    t = int(time.time())
    #print t
    greatethanNow = t + 10*24*60*60
    print greatethanNow
    lessthacnNow = t - 7*24*60*60
    print lessthacnNow
    return greatethanNow,lessthacnNow

if __name__ == '__main__':
    #mp_keys_nomid()
    #mp_keys_greaterthantimestamp()
    #mp_keys_lessthantimestamp()
    mp_keys_all()

