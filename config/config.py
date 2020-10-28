import os
from configparser import ConfigParser


class ReadConfig(object):

    def __init__(self):
        filepath =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        confName = os.path.join(filepath,'config/conf.ini')
        self.config = ConfigParser()
        self.config.read(confName)


    '''根据Section以及item参数，获取配置文件中设置的value'''

    def get_conf(self,section,item):
         return self.config.get(section,item)


if __name__ =="__main__":
    conf = ReadConfig()
    print(conf.get_conf("accountSystem","host"))