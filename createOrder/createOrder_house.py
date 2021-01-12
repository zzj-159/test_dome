# -*- coding: utf-8 -*-
# @Time    : 2020/11/9
# @Author  : 竹玉红
# @Fuction : 创建房贷订单


#渠道：亿联-80 苏州顺鑫利-81 阿福科贷-82 苏州蓝蝎-83 安居客-86
#大类-房抵贷-1 小类-房抵经营贷-4
#订单来源-基塔石-2
import random

from common.dataVariable import Data_variable, Respont

port = '/order/createOrder'
dav = Data_variable(port)
rep = Respont()
pledgeType = [{"pledgeType":1,"loanRate":"0.112"},{"pledgeType":2,"loanRate":"0.118"}]  #抵押各渠道类型
pledgeType_ajk =[{"pledgeType":1,"loanRate":"0.09"},{"pledgeType":2,"loanRate":"0.0972"}] #抵押安居客渠道数据
class createOrderHouse:

    def create_house_order(self,userId='010000003247',userName=None,dealerCode=rep.commonParam.houseChanneId,
                           operatorId=rep.commonParam.luruId,pledgeType=random.choice(pledgeType),
                           loanType=1,orderType=2,orderSource=2,currOperator=46):
        #userId = rep.commonParam.userID
        '''
        创建锡房贷订单
        :param userId: 用户名id号
        :param dealerCode: 房贷渠道号
        :param operatorId: 录入人员的id号
        :param pledgeType: 抵押类型
        :return: 返回创建成功后的订单
        '''
        rep.Mylog.info(
            "==========================create_house_order-创建锡房贷订单=============================")

        if dealerCode == rep.commonParam.houseChanneId_ajk:
              pledgeType = random.choice(pledgeType_ajk)
        param = {
           "body":{
               "userId": userId,
               "userName": userName,
               "loanType": loanType,    #借款流程类型 1：新增   2：续贷  3：结清再贷'
               "orderType": orderType,   #订单类型 1：授信订单    2：借款订单'
               "productType": 1, #产品大类
               "subProductType": 4, #产品小类
               "pledgeType": pledgeType['pledgeType'],     #抵押情况   1：一抵 2：二抵
               "loanRate": pledgeType['loanRate'], #借款利率(基础利率)
               "orderSource": orderSource,    #订单来源 1:手机银行APP   2：开放平台   3：呼叫中心    4：合作渠道'
               "dealerCode": dealerCode, #房贷渠道号
               # "loanRateSelect": 11.8,
               "operatorId": operatorId, #操作员id
               "currOperator":currOperator
               }
          }
        print(param)
        try:
            rep.Mylog.info("create_house_order-创建锡房贷订单：%s" % (dav.data_url()))
            re = rep.api_Re.post_Req(url=dav.data_url(), json=param, header=dav.data_header())  # 调用request
            res = re.json()
            print(res)
            rep.Mylog.info("测试返回报文%s" % (res))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            rep.Mylog.info("接口请求错误，错误原因：%s" % (e))







if __name__ == "__main__":
     a = createOrderHouse()
     b = a.create_house_order(dealerCode=131,)
     print("www",b)
