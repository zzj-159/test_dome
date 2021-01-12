# -*- coding: utf-8 -*-
# @Time    : 2020/12/8
# @Author  :张正杰
# @Fuction :账务中心-老-还款计划

from common.dataVariable import *
from InterfaceData.Interface_Data import Interface_Data
import pytest
import decimal
import time
import random

repuest = Respont()
loger = repuest.Mylog
data = Interface_Data()
db_jst = repuest.ENV.db_jts
mysql = MysqlDb(db_jst)


class Test_accounts_repay_plan_list:

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']
        print(self.clientNo)

    def teardown_class(self):
        pass

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_01_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡机贷(self):
        loger.info("=====test_1_01_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡机贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=55,
                                              describe="test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        loger.info("test_1_01_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡机贷======返回报文：%s" % (res.text))
        time.sleep(3)
        res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        try:
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if assert_loan != ():
                if assert_loan[0]['loan_status'] == 6:
                    res = data.plan_list(loanid=loanid).json()
                    print(res)
                    # assert res['result'][0]['loanId'] == loanid
                    # assert res['result'][0]["stageNo"] == 1
                    # assert res['result'][0]['userId'] == self.userId
                    assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError)as e:
            loger.error("test_1_01_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡机贷====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡车贷(self):
        loger.info("=======test_01_02_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=56,
                                              describe="test_01_02_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name'][0]
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        try:
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if assert_loan != ():
                if assert_loan[0]['loan_status'] == 6:
                    res = data.plan_list(loanid=loanid).json()
                    assert res['code'] == 0
                    # assert res['result'][0]['loanId'] == loanid
                    print(res)
                    # assert res['result'][0]["stageNo"] == 1
                    # assert res['result'][0]['userId'] == self.userId
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡车贷====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡房贷(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡房贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=57,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        try:
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if assert_loan != ():
                if assert_loan[0]['loan_status'] == 6:
                    res = data.plan_list(loanid=loanid).json()
                    assert res['code'] == 0
                    # assert res['result'][0]['loanId'] == loanid
                    print(res)
                    # assert res['result'][0]["stageNo"] == 1
                    # assert res['result'][0]['userId'] == self.userId

                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡房贷====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=58,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        try:
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if assert_loan != ():
                if assert_loan[0]['loan_status'] == 6:
                    res = data.plan_list(loanid=loanid).json()
                    assert res['code'] == 0
                    # assert res['result'][0]['loanId'] == loanid
                    # assert res['result'][0]["stageNo"] == 1
                    # assert res['result'][0]['userId'] == self.userId
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_锡房贷====断言失败，失败原：%s" % (e))

    # 接口正确-还款日当天进行还款计划-可以正确的查询出信息
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_01_接口正确_还款日当天进行还款计划_可以正确的查询出信息(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=59,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        try:
            res = data.plan_list(loanid=loanid).json()
            assert res['code'] == 0
            assert res['result'][0]['loanId'] == loanid
            assert res['result'][0]["stageNo"] == 1
            assert res['result'][0]['userId'] == self.userId
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_01_接口正确_还款日当天进行还款计划_可以正确的查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_01_接口正确_案件已结清时进行还款计划_可以正确查询出信息(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=60,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        try:
            res = data.plan_list(loanid=loanid).json()
            assert res['code'] == 0
            assert res['result'][0]['repaidAmount'] != 0
            assert res['result'][0]['loanId'] == loanid
            assert res['result'][0]["stageNo"] == 1
            assert res['result'][0]['userId'] == self.userId
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_01_接口正确_案件已结清时进行还款计划_可以正确查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_4_01_接口正确_件已逾期进行还款计划_可以正确查询出信息(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=61,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        try:
            res = data.plan_list(loanid=loanid).json()
            assert res['code'] == 0
            assert res['result'][0]['duePenalty'] != 0
            assert res['result'][0]['loanId'] == loanid
            assert res['result'][0]["stageNo"] == 1
            assert res['result'][0]['userId'] == self.userId
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_01_接口正确_案件放款成功后进行还款计划_可以正确查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_5_01_接口正确_案件放款成功后进行还款计划_可以正确查询出信息(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=62,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        try:
            res = data.plan_list(loanid=loanid).json()
            assert res['code'] == 0
            assert res['result'][0]['duePenalty'] == 0
            assert res['result'][0]['loanId'] == loanid
            assert res['result'][0]["stageNo"] == 1
            assert res['result'][0]['userId'] == self.userId
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_01_接口正确_案件放款成功后进行还款计划_可以正确查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_6_01_接口正确_非还款日进行还款计划_可以查询出相关信息(self):
        loger.info("=======test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=63,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是还款计划接口_可以正确查询出还款内容_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                 settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        try:
            res = data.plan_list(loanid=loanid).json()
            res_assert = data.accounts_hxDate_async().json()
            assert res['code'] == 0
            assert res['result'][0]['dueDate'] != res_assert['result']["hxDate"]
            assert res['result'][0]['loanId'] == loanid
            assert res['result'][0]["stageNo"] == 1
            assert res['result'][0]['userId'] == self.userId
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_6_01_接口正确_非还款日进行还款计划_可以查询出相关信息====断言失败，失败原：%s" % (e))

    # 接口报文为空 / 为空字符串时 - 接口返回正确的错误提示
    def test_7_01_接口正确_接口报文为空时_接口返回正确的错误提示(self):
        try:
            res = data.plan_list().json()
            assert res['code'] == 0
            assert res['result'] == None
            assert res['success'] == True
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_7_01_接口正确_接口报文为空时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

    def test_7_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示(self):
        try:
            res = data.plan_list(loanid="").json()
            assert res['code'] == 0
            assert res['result'] == None
            assert res['success'] == True
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_7_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

    def test_8_01_接口正确_接口报文缺少必填项_报文给出正确的错误提示(self):
        try:
            res = data.plan_list().json()
            assert res['code'] == 0
            assert res['result'] == None
            assert res['success'] == True
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_7_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

#
# if __name__ == '__main__':
#     pytest.main(["-s",'-n=10'])
