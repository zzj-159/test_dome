# -*- coding: utf-8 -*-
# @Time    : 2020/11/09
# @Author  : 张正杰
# @Fuction : 创建订单保存内容相关接口——机贷
import json
from common.getAPIResponse import API_Reponse
from common.getEnv import environment
from common.login import Login
from common.Log import MyLog


Env = environment()
host = Env.Host  # 获取前置url
loger = MyLog
port = '/order/createOrder'
repuest = API_Reponse()
db_jst = Env.db_jts


class CreatOrder_machine:

    def createOrder_machine(self, name=None, userId=None, productType="2", subProductType="2", orderSource="2",
                        dealerCode="4"):
        """
        创建订单
        /order/createOrder
        :param way: 1----数据库中获取数据；2——根据自己判断
        :param name: 客户姓名
        :param userId: 客户编号
        :param productType: 产品类型 1：房贷  2：易起投   3：车贷  4：信用贷'
         """
        self.port = '/order/createOrder'  # 接口后置
        login = Login(port)
        header = login.header  # 获取header
        url = host + self.port  # url 拼装
        loger.info("===========创建订单接口开始运行===========")
        param = {
            "body": {
                "userId": userId,
                "userName": name,
                "loanType": "1",
                "orderType": "2",
                "productType": productType,
                "subProductType": subProductType,
                "orderSource": orderSource,
                "dealerCode": dealerCode,
                "operatorId": "119"
            }
        }
        param = json.dumps(param)
        try:
            loger.info("========创建订单接口bata=============%s" % (param))
            res = repuest.post_Req(url=url, header=header, data=param)
            # res_json_loanId = res.json()["result"]
            loger.info("=============创建订单接口运行成功================")
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("接口请求错误，错误原因：%s" % (e))
