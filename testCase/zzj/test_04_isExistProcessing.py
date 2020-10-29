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
userid = "1000000342"
accountNo="6236435330000004614"
body = '/order/isExistProcessingOrderByUserIdAndAcctNo?userId=%s&accountNo=%s'%(userid,accountNo)
conf = ReadConfig()
Env = Environment()
host = Env.Host  # 获取前置url
url = host + body  # url 拼装
api = API_Info(port)  # 调用数据库中信息
apiType = api.api_type  # 接口类型
a = Login()
header = a.header  # 获取header
api_Re = API_Reponse()
loger = MyLog

@allure.description(" /order/isExistProcessingOrderByUserIdAndAcctNo 接口用例")
@allure.testcase("/order/isExistProcessingOrderByUserIdAndAcctNo", "测试用例地址 👇")
@pytest.mark.filterwarnings
def test_04_OrderQuery_用户userId为空字符串时查询未完成订单():
    loger.info("=================test_04_用户userId为空字符串时查询未完成订单====================")
    body = {
        "userId": "",
        "accountNo": None
    }
    # url = url + "?userId=1000000342&accountNo=6236435330000004614"
    loger.info("请求报文：%s" % (body))
    body = json.dumps(body)
    res = API_Reponse().post_Req(url=url, json=body, header=header)
    loger.info("返回报文：%s" % (res.text))
    assert res.status_code == 200
    loger.info("test_04_用户userId为空字符串时查询未完成订单==============断言开始")
    try:
        assert res.json()["message"] == ""
    except Environment as e:
        loger.error("test_04_用户userId为空字符串时查询未完成订单==========断言异常")

