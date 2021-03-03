# encoding:utf8
__author__ = 'gaoqiao'
'''
    def __init__(self, host='localhost', port=6379, db=0, password=None,
                 socket_timeout=None, socket_connect_timeout=None,
                 socket_keepalive=False, socket_keepalive_options=None,
                 socket_type=0, retry_on_timeout=False, encoding='utf-8',
                 encoding_errors='strict', decode_responses=False,
                 parser_class=DefaultParser, socket_read_size=65536):
'''
import redis

pool = redis.ConnectionPool(host="10.202.5.231",port=5584,password="0b7559bf692926aa",decode_responses=True)
r = redis.Redis(connection_pool=pool)

def get_string(key):
    try:
        result = r.get(key)
    except Exception,e:
        print e
    return result

def clear(key):
    try:
        r.delete(key)
    except Exception,e:
        print e
    if get_string(key) == None or get_zset(key) == None:
        print "clear success"
    else:
        print "false"

def get_zset(key):
    try:
        num = r.zcard(key)
        result = r.zrange(key,0,num,withscores=True)
        print result
    except Exception,e:
        print e
    return result

if __name__ == '__main__':
    #m = "5d24d4c250def55030efc04512461abb"
    #m = "c8d8457deb18e2cdafb47890ed65f620"
    #m = "972589d7f0e52a63f49be26cd13c3844"
    m = "fcb71e78e40a6588da861db7e0a5a762"
    key_push = "udp:" + m
    key_us = "uap:" + m
    key_uh = "uh:" + m

    clear(key_push)
    clear(key_us)
    clear(key_uh)

