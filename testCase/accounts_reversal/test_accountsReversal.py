# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  :张正杰
# @Fuction :账务中心-老-冲正

from common.dataVariable import *
from InterfaceData.Interface_Data import Interface_Data
import pytest
import decimal
import json
import time
import random

repuest = Respont()
loger = repuest.Mylog
data = Interface_Data()
db_jst = repuest.ENV.db_jts
mysql = MysqlDb(db_jst)


class Test_accounts_reversal:

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown_class(self):
        pass

    # 接口正确-不同放款原因-调用冲正接口-可以正确的落库信息以及报文正确
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_01_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_银行卡问题(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=77,
                                              describe="test_1_01_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno,
                                      payeeAcctNo='456321789562')
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='银行卡错误').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res_assert[0]['loan_status'] in (8, 9)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确====断言失败，失败原因：%s" % (e))

    # 接口正确-不同放款原因-调用冲正接口-可以正确的落库信息以及报文正确
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_额度不足(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=78,
                                              describe="test_1_02_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_额度不足")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno,
                                      payeeAcctNo='456321789562')
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='额度不足').json()
            assert res['code'] == 0
            assert res['success'] == True
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res_assert[0]['loan_status'] in (8, 9)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_额度不足====断言失败，失败原因：%s" % (e))

    # 接口正确-不同放款原因-调用冲正接口-可以正确的落库信息以及报文正确
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_核算放款成功支付失败(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=79,
                                              describe="test_1_03_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_核算放款成功支付失败")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno,
                                      payeeAcctNo='456321789562')
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='核算放款成功支付失败').json()
            assert res['code'] == 0
            assert res['success'] == True
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res_assert[0]['loan_status'] in (8, 9)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_03_接口正确_不同放款原因_调用冲正接口_可以正确的落库信息以及报文正确_核算放款成功支付失败====断言失败，失败原因：%s" % (e))

    # 接口正确-非异常情况时调用冲正接口-给出正确的错误提示
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_01_接口正确_非异常情况时调用冲正接口_给出正确的错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=80,
                                              describe="test_2_01_接口正确_非异常情况时调用冲正接口_给出正确的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='银行卡异常').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            # assert res['message'] == "失败:CL4014,CL...3]对应的贷款信息不存在！"
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_01_接口正确_非异常情况时调用冲正接口_给出正确的错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_01_接口正确_案件正常放款调用冲正接口_给出错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        # loanid = repuest.commonParam.set_flow(count=1,
        #                                       describe="test_3_01_接口正确_案件正常放款调用冲正接口_给出错误提示")
        # print(loanid)
        # origLoanAmt = '50000.00'
        # prod_type = repuest.commonParam.prod_type("锡机贷")
        # lending = repuest.commonParam.lending(prod_type)[0]
        # lendingname = lending['acct_name']
        # lendingno = lending['acct_no']
        # res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
        #                               origLoanAmt=origLoanAmt,
        #                               prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo="20171216000089", reversal='0', reversalReason='银行卡异常').json()
            assert res['code'] == None
            assert res['success'] == False
            # res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            # assert res['message'] == "失败:CL4014,CL4014 贷款号[null]发放号[null]客户号[null]借据号[20171204000017]对应的贷款信息不存在！"
            # mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
            #                                         userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_01_接口正确_案件正常放款调用冲正接口_给出错误提示====断言失败，失败原因：%s" % (e))

    # _已逾期_已结清
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_02_接口正确_案件已逾期调用冲正接口_给出错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=81,
                                              describe="test_3_02_接口正确_案件已逾期调用冲正接口_给出错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='银行卡异常').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res['message'] == "失败:CL4014,CL4014 贷款号[null]发放号[null]客户号[null]借据号[20171204000017]对应的贷款信息不存在！"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_02_接口正确_案件已逾期调用冲正接口_给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_03_接口正确_案件已结清调用冲正接口_给出错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=82,
                                              describe="test_3_03_接口正确_案件已结清调用冲正接口_给出错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                      origLoanAmt=origLoanAmt,
                                      prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='0', reversalReason='银行卡异常').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res['message'] == "失败:CL4014,CL4014 贷款号[null]发放号[null]客户号[null]借据号[20171204000017]对应的贷款信息不存在！"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_03_接口正确_案件已结清调用冲正接口_给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    # 接口报文为空/为空字符串时-接口返回正确的错误提示
    def test_4_01_接口正确_接口报文为空时_接口返回正确的错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=83,
                                              describe="test_4_01_接口正确_接口报文为空时_接口返回正确的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        # res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
        #                               origLoanAmt=origLoanAmt,
        #                               prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal().json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res['message'] == "失败:000301,000301 [BODY.REVERSAL_REASON(冲销原因)]域必须输入"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_4_01_接口正确_接口报文为空时_接口返回正确的错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    # 接口报文为空/为空字符串时-接口返回正确的错误提示
    def test_4_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=84,
                                              describe="test_4_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        # res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
        #                               origLoanAmt=origLoanAmt,
        #                               prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo="", reversal='', reversalReason='').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res['message'] == "失败:000302,000302 [BODY.REVERSAL_REASON(冲销原因)]域不能为空"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_4_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示====断言失败，失败原因：%s" % (e))

# 接口正确-接口报文缺少必填项-报文给出正确的错误提示
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    # 接口报文为空/为空字符串时-接口返回正确的错误提示
    def test_5_01_接口正确_接口报文缺少必填项_报文给出正确的错误提示(self):
        # 借据号
        # 冲正标志
        # 冲销原因
        loanid = repuest.commonParam.set_flow(count=85,
                                              describe="test_5_01_接口正确_接口报文缺少必填项_报文给出正确的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        # res_loan = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
        #                               origLoanAmt=origLoanAmt,
        #                               prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        try:
            res = data.accounts_reversal(cmisloanNo=loanid, reversal='', reversalReason='').json()
            assert res['code'] == None
            assert res['success'] == False
            res_assert = repuest.commonParam.assect_accounts_loan(loanid)
            assert res['message'] == "失败:000302,000302 [BODY.REVERSAL_REASON(冲销原因)]域不能为空"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_01_接口正确_接口报文缺少必填项_报文给出正确的错误提示====断言失败，失败原因：%s" % (e))
