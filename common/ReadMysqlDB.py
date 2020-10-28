import pandas
import pymysql

# from Database.Conf import Config

# mysqlConf = Config()
from config.config import ReadConfig

conf = ReadConfig()
class DBConnection():

   def __init__(self,section):
       self.section = section
   # def  __call__(self, *args, **kwargs):
   #      return self.connection
   #
   # def __getattr__(self, item):
   #     if item in ['connection', ]:
   #         self.connection = self.get_connnection(self.section)
   #         return self.connection

   def get_connnection(self):
       try:
           db = pymysql.connect(
               host = conf.get_conf(self.section,'host'),
               user=conf.get_conf(self.section, 'user'),
               passwd=conf.get_conf(self.section, 'password'),
               db =conf.get_conf(self.section, 'database'),
               port = int(conf.get_conf(self.section, 'port')),
               charset = 'utf8'
               # autocommit = True,
               # use_unicode = True
               )
           return db
       except Exception as e:
           #longger.info
           return  None


if __name__=="__main__":
    db1 = DBConnection('db1')
    sql = '''SELECT * FROM api_info WHERE url = '/api/user/stu_info';'''
    df = pandas.read_sql(sql,db1.get_connnection())
    print(df)