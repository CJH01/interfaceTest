# -*- coding: UTF-8 -*-
import json
import unittest
from testCase.geturlParams import geturlParams
from conf.configHttp import RunMain
import urllib.parse
from testCase.readExcel import readExcel
import paramunittest

#unittest断言

#测试网址
url =  geturlParams().get_url()
#测试数据
login_xls = readExcel().get_xls('userCase.xlsx','login')

@paramunittest.parametrized(*login_xls)   #格式化数据
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        #case_name,path,query,method三个参数和前面定义的元组--对应
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    #描述
    def description(self):
        self.case_name

    #测试准备
    def setUp(self):
        print(self.case_name+"测试开始前准备")

    #测试开始
    def test01case(self):
        self.checkResult()

    #测试结束
    def tearDown(self):
        print("测试结束，输出log完结\n")

    #断言
    def checkResult(self):
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        print(new_url)
        #将完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'xxx'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        #根据method调用run_main进行request请求，并拿到响应
        info = RunMain().run_main(self.method,url,data1)
        #将响应结果转换成字典格式
        ss = json.loads(info)
        print(ss)
        if self.case_name == 'login':
            # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'],200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],-10001)

if __name__ == '__main__':
    testUserLogin().test01case()