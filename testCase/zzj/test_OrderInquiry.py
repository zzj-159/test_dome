# -*- coding: utf-8 -*-
# @Time    : 2020/10/27
# @Author  : 张正杰
# @Fuction : 测试获取最新的第二笔订单

import warnings
from common.getAPIResponse import API_Reponse
from common.getAPI_Info import API_Info
from common.Log import MyLog
from config.config import ReadConfig
from common.getEnv import Environment
from common.login import Login
import allure
import pytest


port = '/loanLog/list'  # 接口后置
conf = ReadConfig()
Env = Environment()
host = Env.Host  # 获取前置url
# url = conf.get_conf("accountSystem", "host")
url = host + port  # url 拼装
api = API_Info(port)  # 调用数据库中信息
apiType = api.api_type  # 接口类型
print(apiType)
a = Login()
header = a.header  # 获取header
print(header)
api_Re = API_Reponse()
loger = MyLog
import json


@allure.description("测试 /order/querySecOrder 接口用例")
@allure.testcase("/order/querySecOrder", "测试用例地址 👇")
@pytest.mark.filterwarnings
def test_01_querySecOrder_正确报文获取最新的第二笔订单():
    """
    获取完整的正确的最新的第二笔订单
    :return:
    """
    loger.info(
        "==============================test_asarchRepayList_01_放款流水查询接口测试======================================")
    param = {
        "endDate": None,
        "startDate": None,
        "status": 6,
        "loanId": None,
        "page": 1,
        "pageSize": 10
    }
    # print(type(param))
    param = json.dumps(param)  # 数据类型转换为json
    loger.info("test_01_放款流水查询——测试开始——测试地址：%s" % (url))
    res = api_Re.post_Req(url=url, json=param, header=header)  # 调用request
    a = res.json()  # 返回报文转json
    loger.info("测试返回报文%s" % (a))
    try:
        assert res.status_code == 200  # 返回值断言
    except Environment as e:
        loger.info("判断结果异常：%s" % (e))


@allure.description("测试 /order/querySecOrder 接口用例")
@allure.testcase("/order/querySecOrder", "测试用例地址 👇")
@pytest.mark.filterwarnings
def test_02_querySecOrder_获取内容失败():
    """
    获取内容失败
    :return:
    """
    loger.info(
        "==============================test_asarchRepayList_01_放款流水查询接口测试======================================")
    param = {
        "endDate": None,
        "startDate": None,
        "status": 6,
        "loanId": None,
        "page": 1,
        "pageSize": 10
    }
    # print(type(param))
    param = json.dumps(param)  # 数据类型转换为json
    loger.info("test_01_放款流水查询——测试开始——测试地址：%s" % (url))
    res = api_Re.post_Req(url=url, json=param, header=header)  # 调用request
    a = res.json()  # 返回报文转json
    loger.info("测试返回报文%s" % (a))
    try:
        assert res.status_code == 200  # 返回值断言
    except Environment as e:
        loger.info("判断结果：%s" % (e))

@allure.description("测试 /order/querySecOrder 接口用例")
@allure.testcase("/order/querySecOrder", "测试用例地址 👇")
@pytest.mark.filterwarnings
def test_03_querySecOrder_报文内容中为空为空字符串时接口给出正确的错误提示():
    """
    报文内容中为空为空字符串时接口给出正确的错误提示
    :return:
    """
    loger.info(
        "================================================测试开始test_03_querySecOrder_报文内容中为空为空字符串时接口给出正确的错误提示=====================================")
    bady = {

    }
    bady = json.dumps(bady)
    loger.info("测试开始:测试url%s----测试dody%s" % (url, bady))
    res = api_Re.post_Req(url=url, json=bady, header=header)
    print(res.text)
    try:
        print(res.json()["code"])
        body = res.json()
        assert body["code"] == 9999
    except Environment as e:
        loger.info("断言错误%s" % (e))
