# -*- coding: utf-8 -*-
# @Time    : 2020/10/28
# @Author  : 张正杰
# @Fuction : 根据用户与还款账号判断是否有未完成的订单

import warnings
from common.getAPIResponse import API_Reponse
from common.getAPI_Info import API_Info
from common.Log import MyLog
from config.config import ReadConfig
from common.getEnv import Environment
from common.login import Login
import allure
import pytest
import json

port = '/order/isExistProcessingOrderByUserIdAndAcctNo'  # 接口后置
conf = ReadConfig()
Env = Environment()
host = Env.Host  # 获取前置url
url = host + port  # url 拼装
api = API_Info(port)  # 调用数据库中信息
apiType = api.api_type  # 接口类型
# print(apiType)
a = Login()
header = a.header  # 获取header
# print(header)
api_Re = API_Reponse()
loger = MyLog



@allure.description("测试 /order/isExistProcessingOrderByUserIdAndAcctNo 接口用例")
@allure.testcase("/order/isExistProcessingOrderByUserIdAndAcctNo", "测试用例地址 👇")
@pytest.mark.filterwarnings
def test_01_OrderQuery_用户userId存在未完成订单_正确查询出相应的信息():
    """
    用户userId存在未完成订单_正确查询出相应的信息
    :return:assert
    """
    loger.info(
        "==============================test_01_用户存在未完成的订单，正确查询出相应的信息======================================")
    param = {
        "userId": None,
        "accountNo": None
    }
    # print(type(param))
    param = json.dumps(param)  # 数据类型转换为json
    loger.info("test_01_放款流水查询——测试开始——测试地址：%s" % (url))
    res = api_Re.post_Req(url=url, json=param, header=header)  # 调用request
    a = res.json()  # 返回报文转json
    loger.info("测试返回报文%s" % (a))
    try:
        assert a["result"] == 'true'  # 返回值断言
    except Environment as e:
        loger.info("判断结果异常： %s" % (e))

