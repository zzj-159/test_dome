# -*- coding: utf-8 -*-
# @Time    : 2020/10/12
# @Author  : yuhong.zhu
# @Fuction : 读取数据库相关接口的信息

import pandas as pd
from common.getDBConnect import DBConnection

db = DBConnection('test_automation')
table = 'api_info'
class API_Info:
     def __init__(self,url):
         self.url = url
     def getDBInfo(self):
        '''
         查询数据库存放的接口信息
         :return: 返回一行接口信息
        '''
        sql = '''select * from {} where url = '{}';'''.format(table,self.url)
        df = pd.read_sql(sql,db.get_connnection())
        df_dict = df.to_dict(orient='record')
        return df_dict[0]

     @property
     def api_url(self):
         return self.url
     @property
     def apiInfo(self):
         return self.getDBInfo()

     @property
     def api_type(self):
         return self.apiInfo['type']
     @property
     def api_function(self):
         return self.apiInfo['assertFuction']


if __name__ =='__main__':
    url = '/loanLog/list'
    api = API_Info(url)

    apiType = api.api_type
    print(api.getDBInfo())