#coding=UTF-8
from testCase.readConfig import ReadConfig
import os
import win32com.client as win32
import datetime
import pythoncom

pythoncom.CoInitialize()
#读取邮件主题
subject = ReadConfig().get_email('subject')
app = str(ReadConfig().get_email('app'))
addressee = ReadConfig().get_email('addressee')
cc = ReadConfig().get_email('cc')
main_path = os.path.join("D:/InterfaceTest/result/",'report.html')

class send_email():
    def outlook(self):
        #固定写法
        outlook = win32.Dispatch("%s.Application" % app)#
        #固定写法
        mail = outlook.CreateItem(0)   #0:olMainItem
        #收件人
        mail.To = addressee
        #抄送人
        mail.CC = cc
        #邮件主题
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject
        content = """
        执行测试中完成......
        测试已完成......
        生成报告中......
        报告已生成......
        报告已邮件发送......
        """
        mail.Body = content
        mail.Attachments.Add("D:/InterfaceTest/result/report.html")
        mail.Send()

if __name__ == '__main__':
    send_email().outlook()
    print("send email ok!!!!!!")
