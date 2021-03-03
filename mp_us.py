#coding=utf-8
__author__ = 'gaoqiao'
import requests
import pytest

URL = "http://cloud.browser.360.cn/mp/us"

def mp_us_client():
    data = {"m":"43df2d47985708fa655ad9efd37fa6c8","f":"1"}
    r = requests.get(URL,data,verify=False)
    print (r.text)

def mp_us_page():
    data = {"m":"43df2d47985708fa655ad9efd37fa6c8","f":"2"}
    r = requests.get(URL,data,verify=False)
    #print r.text
    if r.status_code == 200:
        result = r.json()
        assert result["errno"] == 0
    else:
        print (r.status_code)
    #print result
    #print type(result["list"][0]["windowHeight"])

def mp_us_sesvc():
    data = {"m":"43df2d47985708fa655ad9efd37fa6c8","f":"3"}
    r = requests.get(URL,data,verify=False)
    print (r.text)

def mp_us_page_return(mid):
    data = {"m":mid,"f":"2"}
    r = requests.get(URL,data,verify=False)
    #print (r.text)
    result = r.json()
    return result

def mp_us_fwrong():
    '''
    {"errno":10010}
    :return:
    '''
    data = {"m":"5d24d4c250def55030efc04512461abb","f":"332"}
    r = requests.get(URL,data)
    #print r.text
    if r.status_code == 200:
        result = r.json()
        assert result["errno"] == 10010
    else:
        print (r.status_code)

def mp_us_nof():
    data = {"m":"5d24d4c250def55030efc04512461abb"}
    r = requests.get(URL,data)
    #print r.text
    if r.status_code == 200:
        result = r.json()
        assert result["errno"] == 10010
    else:
        print (r.status_code)

def mp_us_nomid():
    data = {"f":"2"}
    r = requests.get(URL,data)
    #print r.text
    if r.status_code == 200:
        result = r.json()
        assert result["errno"] == 10010
    else:
        print (r.status_code)

def mp_us_midwrong():
    data = {"m":"5d24d4c250def55030e","f":"2"}
    r = requests.get(URL,data)
    #print r.text
    if r.status_code == 200:
        result = r.json()
        assert result["errno"] == 10010
    else:
        print (r.status_code)

if __name__ == '__main__':
    #pytest.main()
    #pytest.main(['-s','-q','--alluredir','report/result'])
    #os.system("C:/Python27/Lib/site-packages/allure-2.8.0/bin/allure.bat " "generate " "E:/auto/Pytest/mini program/test/reportresult " "-o " "E:/auto/Pytest/mini program/test/report/html")
    #os.system("dir")
    mp_us_page_return("5d24d4c250def55030efc04512461abb")
