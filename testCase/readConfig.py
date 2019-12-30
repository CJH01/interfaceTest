#encoding=utf-8
import os
import configparser
import re
from testCase import getpathInfo

#获取绝对路径
path = getpathInfo.get_Path()
#拼接路径得到当前文件的绝对路径的字符串
config_path = os.path.join(path,'config.ini')

#去掉配置文件开头的BOM字节
def remove_BOM(path):
    fo = open(path, 'r')
    content = fo.read()
    content = re.sub(r"\xfe\xff","",content)
    content = re.sub(r"\xff\xfe","",content)
    content = re.sub(r"\xef\xbb\xbf","",content)
    open(config_path,'w+').write(content)
    fo.close()
    print(0)


# 读取配置文件的方法
config = configparser.ConfigParser()
#remove_BOM(config_path)
config.read(config_path,'utf-8')

#写一个类封装：读取配置文件指定内容
class ReadConfig():
    #读取http配置
    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    #读取邮箱配置
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    #读取数据库配置
    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value

if __name__ == '__main__':
    print('HTTP中baseurl值为：',ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：',ReadConfig().get_email('on_off'))




