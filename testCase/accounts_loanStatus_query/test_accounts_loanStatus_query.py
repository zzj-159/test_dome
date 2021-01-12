# -*- coding: utf-8 -*-
# @Time    : 2020/12/18
# @Author  :张正杰
# @Fuction :账务中心-老-放款查询

from common.dataVariable import *
from InterfaceData.Interface_Data import Interface_Data
import pytest
from time import ctime, sleep
import decimal
import json
import time
import random
import threading

repuest = Respont()
loger = repuest.Mylog
data = Interface_Data()
db_jst = repuest.ENV.db_jts
mysql = MysqlDb(db_jst)


class Test_accountsLoanStatusQquery:

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown(self):
        pass


    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_01_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷(self):
        loger.info("=====test_01_01_正常的放款接口_调用放款状态查询接口_校验其数据正确=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=21,
                                              describe="test_01_01_正常的放款接口_调用放款状态查询接口_校验其数据正确")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_01_01_正常的放款接口_调用放款状态查询接口_校验其数据正确======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()['result']['loanStatus'] in [1, 2, 3, 4, 5, 6, 7]
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_01_正常的放款接口_调用放款状态查询接口_校验其数据正确====断言失败，失败原因：%s" % (e))


    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷(self):
        loger.info("=====test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=22,
                                              describe="test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()['result']['loanStatus'] in [1, 2, 3, 4, 5, 6, 7]
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷====断言失败，失败原因：%s" % (e))


    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷(self):
        loger.info("=====test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=23,
                                              describe="test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()['result']['loanStatus'] in [1, 2, 3, 4, 5, 6, 7]
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_02_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡房贷====断言失败，失败原因：%s" % (e))



    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_03_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷(self):
        loger.info("=====test_01_03_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=24,
                                              describe="test_01_03_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_01_03_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()['result']['loanStatus'] in [1, 2, 3, 4, 5, 6, 7]
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_03_正常的放款接口_调用放款状态查询接口_校验其数据正确_锡车贷====断言失败，失败原因：%s" % (e))



    def test_02_01_接口正确_调用放款状态查询接口_报文中boday为空时_给出相应的错误提示(self):
        try:
            res_show = data.accounts_loan_show()
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] ==0
            assert res_show.status_code == 200
            assert res_show.json()["message"] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_01_接口正确_调用放款状态查询接口_报文中boday为空时_给出相应的错误提示====断言失败，失败原因：%s" % (e))

    def test_02_02_接口正确_调用放款状态查询接口_报文中boday为空字符串时_给出相应的错误提示(self):
        try:
            res_show = data.accounts_loan_show(loanid="")
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] ==0
            assert res_show.status_code == 200
            assert res_show.json()["message"] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_02_接口正确_调用放款状态查询接口_报文中boday为空字符串时_给出相应的错误提示====断言失败，失败原因：%s" % (e))



