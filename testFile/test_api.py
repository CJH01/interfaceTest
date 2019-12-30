#coding = utf-8
import flask
import json
from flask import request

'''flask：web框架，通过flask提供的装饰器@server.router()将普通函数转换为服务'''

_name_ = ""
server = flask.Flask(import_name=_name_);

#创建一个服务，把这个python文件当作一个服务
@server.route('/login',methods=['get','post'])
def  login():
    #获取通过url请求传参的数据
    username = request.values.get('name')
    #获取url请求传参的密码
    pwd = request.values.get('pwd')
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            resu = {'code':200,'message':'登陆成功'}
            return json.dumps(resu,ensure_ascii=False)  #将字典转换成字符串
        else:
            resu = {'code':-1,'message':'账号密码错误'}
            return json.dumps(resu,ensure_ascii=False)
    else:
        resu = {'code':10001,'message':'参数不能为空！'}
        return json.dumps(resu,ensure_ascii=False)

#if _name_ == '_main_':
server.run(debug=True,port=8888,host='127.0.0.1')

