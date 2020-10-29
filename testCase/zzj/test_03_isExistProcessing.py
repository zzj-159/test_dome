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
def test_03_OrderQuery_用户userId为空查询未完成订单():
    loger.info("=============test_03_用户userId为空查询未完成订单,根据银行卡查询内容==================")
    param = {
    }
    # url = url + "?userId=1000000342&accountNo=6236435330000004614"
    param = json.dumps(param)
    loger.info("测试发送报文：%s" % (param))
    res = api_Re.post_Req(url=url, json=param, header=header)
    loger.info("接口返回报文：%s" % (res.text))
    assert res.status_code == 200
    try:
        assert res.json()['message'] == ""
        loger.info("test_03_用户userId为空查询未完成订单,根据银行卡查询内容============断言正确")
    except Environment as e:
        loger.error("断言异常结果%s" % (e))

