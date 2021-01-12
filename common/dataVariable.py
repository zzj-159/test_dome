# -*- coding: utf-8 -*-
# @Time    : 2020/10/28
# @Author  : 张正杰
# @Fuction : 配置传参
from common.getAPIResponse import API_Reponse
from common.getAPI_Info import API_Info
from common.getCommonParam import param
from common.getEnv import environment
from common.login import Login
from common.Log import MyLog
from common.ReadMysqlDB import MysqlDb
from common.sql_summary import SQL_Summary


class Data_variable():
    def __init__(self, port):
        self.port = port

    def data_header(self):
        login = Login(self.port)
        self.header = login.header  # 获取header
        return self.header

    def data_url(self):
        Env = environment()
        host = Env.Host  # 获取前置url

        self.url = host + self.port  # url 拼装
        return self.url

    def api(self):
       return API_Info()

class Respont():
    @property
    def api_Re(self):
        return API_Reponse()

    @property
    def Mylog(self):
        return MyLog()

    @property
    def Mysql(self):
        return MysqlDb

    @property
    def SQL(self):
        return SQL_Summary()

    @property
    def ENV(self):
        return environment()

    @property
    def commonParam(self):
        return param()

if __name__ == "__main__":
    a = Respont()
    # a.api_Re.post_Req()
    ab = a.Mysql('jtsDB_SIT')
    sql = "SELECT user_id FROM `credit_info`WHERE outstanding_loan_balance > 0.00 and user_id ='010000003152';"
    print(ab.select_db(sql=sql))

