# encoding:utf-8
__author__ = 'gaoqiao'
'''
推荐接口(大家都在用)
返回大家都在用数据
'''
import requests

URL = "http://cloud.browser.360.cn/mp/rec"

def mp_rec():
    data = {"cb":"12312312321"}
    r = requests.get(URL,data)
    print r.text

if __name__ == '__main__':
    mp_rec()

