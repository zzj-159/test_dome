# -*- coding: utf-8 -*-
# @Time    : 2020/10/12
# @Author  : yuhong.zhu
# @Fuction : 获取数据库连接

import pandas
import pymysql

from config.config import ReadConfig

conf = ReadConfig()


class DBConnection():

    def __init__(self, section):
        self.section = section

    def get_connnection(self):
        try:
            db = pymysql.connect(
                host=conf.get_conf(self.section, 'host'),
                user=conf.get_conf(self.section, 'user'),
                passwd=conf.get_conf(self.section, 'password'),
                db=conf.get_conf(self.section, 'database'),
                port=int(conf.get_conf(self.section, 'port')),
                charset='utf8'
                # autocommit = True,
                # use_unicode = True
            )
            return db
        except Exception as e:
            # longger.info
            return None


if __name__ == "__main__":
    db1 = DBConnection('test_automation')
    sql = '''SELECT * FROM api_info WHERE url = '/order/querySecOrder';'''
    df = pandas.read_sql(sql, db1.get_connnection())
    print(df)

