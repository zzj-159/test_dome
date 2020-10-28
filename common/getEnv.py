# -*- coding: utf-8 -*-
# @Time    : 2020/10/12
# @Author  : yuhong.zhu
# @Fuction : 读取配置文件的环境配置

from config.config import ReadConfig

conf = ReadConfig()
section = 'accountSystem'
class Environment:

    @property
    def Host(self):
        return conf.get_conf(section,'host')
    @property
    def loginUrl(self):
        return conf.get_conf(section, 'login_url')

    @property
    def user(self):
        return conf.get_conf(section, 'user')

    @property
    def password(self):
        return conf.get_conf(section, 'password')

