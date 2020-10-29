# -*- coding: utf-8 -*-
# @Time    : 2020/10/12
# @Author  : yuhong.zhu
# @Fuction : 登录，获取token
import requests
from common.getEnv import Environment
from config.config import ReadConfig

conf = ReadConfig()
Env = Environment()
host = Env.Host
loginUrl = Env.loginUrl
user = Env.user
password = Env.password
class Login:

    def login(self):

        param = {
            'username': user,
            'password': password,
        }
        # print(loginUrl,user,password)
        res = requests.post(loginUrl,json = param)
        assert res.status_code == 200
        # print(res.json())
        return res.json()

    @property
    def token(self):
        return self.login()['result']

    @property
    def header(self):
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            'token':self.token
        }
        return headers

if __name__ == '__main__':
    a = Login()
    header = a.header
    print(header)
    url  = 'http://10.100.0.125:8031/loanorder/order/queryOrderProductByUserId'
    url = url+"?userId=010000003782"
    param = {
    }
    print(param)
    print(url)
    res = requests.post(url,json=param,headers=header)
    # assert res.status_code == 200
    print(res.text)

