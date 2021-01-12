# -*- coding: utf-8 -*-
# @Time    : 2020/11/3
# @Author  : 张正杰
# @Fuction : 从数据库中提取断言数据


from common.ReadMysqlDB import MysqlDb
from common.getEnv import environment

env = environment()
mysql = MysqlDb('jtsDB_SIT')

class Data:
    def getdata(self, sql):
        """
        获取相应的断言内容
        :param sql:需要获取的数据
        :return:
        """
        df = mysql.select_db(sql)
        return df


if __name__ == "__main__":
    data = Data()
    sql = "SELECT * FROM `credit_info`WHERE user_id ='010000003152';"
    a = data.getdata(sql)
    print(a)
