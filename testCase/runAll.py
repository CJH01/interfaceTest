#coding=utf-8
import os
import unittest
from testCase import getpathInfo
from testCase import readConfig
import common.HTMLTestRunner as HTMLTestRunner   #生成报告
import pythoncom
from conf.configEmail import send_email    #发送邮件
from logs.log import Logger     #打印log

path = getpathInfo.get_Path()
report_path = os.path.join(path,'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = Logger().get_logger()

class ALLTest():
    #初始化一些参数和数据
    def __init__(self):
        #全局参数
        global resultPath
        resultPath = os.path.join("D:/InterfaceTest/result/","report.html")
        self.caseListFile = os.path.join("D:/InterfaceTest/testFile/","caselist.txt")
        self.caseFile = path
        self.caseList = []

        log.debug('debug mesage')
        log.info('info message')
        log.warning("this is a waring log")
        log.error('error message')
        log.info(str.format("%s %s","resultPath",resultPath))

    #读取caselist.txt文件中的用例名称，添加到caselist数组
    def set_case_list(self):
        #打开文件
        fb = open(self.caseListFile,"r")
        for value in fb.readlines():
            data = str(value)
            #data非空且不以#开头
            if data != '' and not data.startswith("#"):
                #去掉每行数据的换行符
                self.caseList.append(data.replace("\n",""))
        fb.close()

    def set_case_siute(self):
        #通过set_case_list()拿到caseList数组
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            #通过split函数将aaa/bbb分割，-1取后面，0取前面
            case_name = case.split("/")[-1]
            #打印取出来的名称
            print(case_name+".py")

            #批量加载用例，第一个为用例路径，第二个为文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile,pattern=case_name+'.py',top_level_dir=None)
            suite_module.append(discover)

        #判断suite_module是否为空
        if len(suite_module)>0:
            #取出数组内容
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite

    def run(self):
        try:
            #调用set_case_siute获取test_suite
            suit = self.set_case_siute()
            print('try')
            print(str(suit))
            if suit is not None:
                print('if-suit')
                #打开result/report.html测试报告，如果不存在就创建
                with open(resultPath,'wb') as fp:
                   #调用HTMLTestRunner
                   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='Test Description')
                   runner.run(suit)
            else:
                print("没有测试用例")
        except Exception as ex:
            print(str(ex))
        finally:
            print("*******TEST END********")

        #发邮件
        if on_off == 'on':
            send_email().outlook()
        else:
            print("邮件发送开关配置关闭，请打开后自动发送测试报告")

if __name__ == '__main__':
    ALLTest().run()