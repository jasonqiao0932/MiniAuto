# encoding:utf-8
__author__ = 'GQ'
import redis

'''
tag机制验证
redis列表：
        "0":{"10.202.4.252:5831","05820776546b0eaa"},
		"R:0":{"10.202.4.79:5831","05820776546b0eaa"},
		"1":{"10.202.4.251:5832","05823a23546ae957"},
		"R:1":{"10.202.4.79:5832","05823a23546ae957"},
		"2":{"10.202.4.252:5833","05823d1c546ae450"},
		"R:2":{"10.202.4.251:5833","05823d1c546ae450"},
		"3":{"10.202.4.251:5835","058232ba546ae1ee"},
		"R:3":{"10.202.5.163:5835","058232ba546ae1ee"},
		"4":{"10.202.4.252:5836","05823597546adccb"},
		"R:4":{"10.202.4.79:5836","05823597546adccb"},
		"5":{"10.202.4.251:5841","058552f354630c58"},
		"R:5":{"10.202.4.79:5841","058552f354630c58"},
		"6":{"10.202.4.251:5842","05854f3c5462fea1"},
		"R:6":{"10.202.4.79:5842","05854f3c5462fea1"},
		"7":{"10.202.4.252:5843","05854c795462fdde"},
		"R:7":{"10.202.5.163:5843","05854c795462fdde"},
		"8":{"10.202.4.252:5844","05854942546300a7"},
		"R:8":{"10.202.4.79:5844","05854942546300a7"},
		"9":{"10.202.4.251:5845","0585478f5462f6f4"},
		"R:9":{"10.202.5.163:5845","0585478f5462f6f4"},
'''

user_redis = {
    "0":"10.202.4.252,5831,05820776546b0eaa",
    "1":"10.202.4.251,5832,05823a23546ae957",
    "2":"10.202.4.252,5833,05823d1c546ae450",
    "3":"10.202.4.251,5835,058232ba546ae1ee",
    "4":"10.202.4.252,5836,05823597546adccb",
    "5":"10.202.4.251,5841,058552f354630c58",
    "6":"10.202.4.251,5842,05854f3c5462fea1",
    "7":"10.202.4.252,5843,05854c795462fdde",
    "8":"10.202.4.252,5844:05854942546300a7",
    "9":"10.202.4.251,5845,0585478f5462f6f4"
}


def redis_conn(ip,port,password):
    try:
        pool = redis.ConnectionPool(host=ip,port=port,password=password)
        r = redis.Redis(connection_pool=pool)
        return r
    except Exception,e:
        print e

def getredis(mid):
    list1 = list(mid)
    mp = (ord(list1[0]) + ord(list1[1])) % 10
    for key in user_redis:
        #print key
        if mp == int(key):
            red_config = user_redis[key].split(",")
            red_config_list = list(red_config)
            #print red_config_list
            r = redis_conn(red_config_list[0],red_config_list[1],red_config_list[2])
            return r

def hgetall(mid):
    r = getredis(mid)
    value = r.hgetall(mid)
    #print value
    print value['channel_8']


def hset(mid,key,value):
    r = getredis(mid)
    try:
        r.hset(mid,key,value)
        value = r.hgetall(mid)
        #print value
        print value['channel_8']
    except Exception,e:
        print e

if __name__ == '__main__':
    m = "5d24d4c250def55030efc04512461abb"
    #m = "972589d7f0e52a63f49be26cd13c3844"
    m_an = "9d995beb65fb83f092e3814eb85c3242"
    m_lcq = "674999ca0cc670650a907edde953eee6"
    m_wyn = "cb0fccdef3f363af23245b04c3635551"
    m1 = "fcb71e78e40a6588da861db7e0a5a762"
    hgetall(m1)
    #hset(m,"channel_8","运动户外,箱包,服饰鞋帽,手表首饰,家居建材,小说,sports,王者荣耀,视屏,动漫美图,股票,家居建材,视屏,小程序安安")
    #hset(m,"channel_8","股票,家居建材,视屏,汽车用品,视屏,通用购物")