# encoding:utf-8
__author__ = 'gaoqiao'
'''
查询小程序详情
i  小程序id
rand  6位的随机数
t  时间戳
sign  签名参数 md5(i + rand + t + "love_mp_interface") ； （客户端必输，web不需要）
decrypt  返回结果是否解密： 0/不传-加密 1-非加密

首先校验decrypt，如果=1，则走新校验逻辑，校验sign或请求中的referer；
=0，兼容旧方式的请求，不校验sign和referer
不传decrypt，默认=0

qywhb2snm23tw8ue94  小游戏
qha3mdtwj2w7a92y5f  小程序
'''
import requests
import public

URL = "http://cloud.browser.360.cn/mp/ai"
T = public.T

def mp_ai_pcold():
    '''
    PC端调用，不需要验证sign
    :return:
    '''
    data = {"i":"qynczj4ybtazcep47q"}
    rand,sign = public.checksign(data["i"])
    data = {"i":"qynczj4ybtazcep47q","rand":rand,"sign":"","t":T,"decrypt":"0"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_pc():
    '''
    PC端调用，需要验证sign
    :return:
    '''
    data = {"i":"qynczj4ybtazcep47q"}
    rand,sign = public.checksign(data["i"])
    data = {"i":"qynczj4ybtazcep47q","rand":rand,"sign":sign,"t":T,"decrypt":"1"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_web():
    '''
    web端调用，验证Referer=mp.360.cn
    :return:
    '''
    data = {"i":"qynczj4ybtazcep47q"}
    rand,sign = public.checksign(data["i"])
    header = {"Referer":"mp.360.cn"}
    data = {"i":"qynczj4ybtazcep47q","rand":rand,"t":T,"decrypt":"1"}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_ai_webRefererWrong():
    '''
    web端调用，Referer!=mp.360.cn
    :return:auth error
    '''
    data = {"i":"qha3mdtwj2w7a92y5f"}
    rand,sign = public.checksign(data["i"])
    #print rand,sign
    header = {"Referer":"111.360.cn"}
    data = {"i":"qha3mdtwj2w7a92y5f","rand":rand,"t":T,"decrypt":"1"}
    r = requests.get(URL,data,headers=header)
    print r.text

def mp_ai_webRefererEmpty():
    '''
    web端调用，Referer为空
    :return:
    '''
    data = {"i":"qha3mdtwj2w7a92y5f"}
    rand,sign = public.checksign(data["i"])
    data = {"i":"qha3mdtwj2w7a92y5f","rand":rand,"t":T,"decrypt":"1"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_appidNotExist():
    '''
    appid不存在或小程序下架
    :return:返回空,web返回{"errmsg":"appid is not exist","errno":41181}
    '''
    data = {"i":"123123"}
    rand,sign = public.checksign(data["i"])
    #print rand,sign
    data = {"i":"123123","rand":rand,"sign":sign,"t":T,"decrypt":"0"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_signWrong():
    '''
    签名验证错误
    :return:auth error
    '''
    data = {"i":"qha3mdtwj2w7a92y5f"}
    rand,sign = public.checksign(data["i"])
    #print rand,sign
    data = {"i":"qha3mdtwj2w7a92y5f","rand":rand,"sign":"123123213","t":T,"decrypt":"1"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_randEmpty():
    '''
    rand随机数为空
    :return:auth error
    '''
    data = {"i":"qha3mdtwj2w7a92y5f"}
    rand,sign = public.checksign(data["i"])
    #print rand,sign
    data = {"i":"qha3mdtwj2w7a92y5f","rand":"","sign":sign,"t":T,"decrypt":"1"}
    r = requests.get(URL,data)
    print r.text

def mp_ai_TEmpty():
    '''
    时间戳为空
    :return:auth error
    '''
    data = {"i":"qha3mdtwj2w7a92y5f"}
    rand,sign = public.checksign(data["i"])
    #print rand,sign
    data = {"i":"qha3mdtwj2w7a92y5f","rand":rand,"sign":sign,"t":"","decrypt":"1"}
    r = requests.get(URL,data)
    print r.text

if __name__ == '__main__':
    mp_ai_pcold()
    mp_ai_pc()
    mp_ai_web()
    #mp_ai_webRefererWrong()
