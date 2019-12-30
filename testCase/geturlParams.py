#coding=utf-8
from testCase.readConfig import ReadConfig
#定义一个方法，将从配置文件中读取的字段进行拼接
class geturlParams():
    def get_url(self):
        new_url = ReadConfig().get_http('scheme')+'://'+ReadConfig().get_http('baseurl')+\
                  ':8888'+'/login'+'?'
        return new_url

if __name__ == '__main__':
    print(geturlParams().get_url())