# -*- coding: utf-8 -*-
# @Time    : 2020/12/8
# @Author  :张正杰
# @Fuction :账务中心-老-还款试算接口

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


class Test_accounts_repayTrial:

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown_class(self):
        pass

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_01_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡机贷(self):
        time.sleep(0.5)
        loanid = repuest.commonParam.set_flow(count=67,
                                              describe="test_1_01_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            mysql = repuest.commonParam.assect_accounts_loan(loanid)
            print(mysql)
            if mysql != ():
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                if mysql[0]['loan_status'] == 6:
                    res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                    res_plan_list = data.plan_list(loanid=loanid)
                    schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                    outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                    outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                    outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                    assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                    num = len(res_plan_list['result'])
                    numer = 0
                    for i in res_plan_list['result']:
                        numer += i['dueCapital']
                    print(numer)
                    assert numer == outstandingPriAmt
                    res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                        receiptAmt=origLoanAmt, userId=self.userId)
                else:
                    pass
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_1_01_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡车贷(self):

        loanid = repuest.commonParam.set_flow(count=68,
                                              describe="test_1_01_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡车贷")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            mysql = repuest.commonParam.assect_accounts_loan(loanid)
            if mysql != ():
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                if mysql[0]['loan_status'] == 6:
                    res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                    res_plan_list = data.plan_list(loanid=loanid)
                    schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                    outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                    outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                    outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                    assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                    num = len(res_plan_list['result'])
                    numer = 0
                    for i in res_plan_list['result']:
                        numer += i['dueCapital']
                    print(numer)
                    assert numer == outstandingPriAmt
                    res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                        receiptAmt=origLoanAmt, userId=self.userId)
                else:
                    pass
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_1_01_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡车贷====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡房贷(self):
        time.sleep(1)
        loanid = repuest.commonParam.set_flow(count=69,
                                              describe="test_1_03_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡房贷")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            mysql = repuest.commonParam.assect_accounts_loan(loanid)
            if mysql != ():
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                if mysql[0]['loan_status'] == 6:
                    res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                    res_plan_list = data.plan_list(loanid=loanid)
                    schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                    outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                    outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                    outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                    assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                    num = len(res_plan_list['result'])
                    numer = 0
                    for i in res_plan_list['result']:
                        numer += i['dueCapital']
                    print(numer)
                    assert numer == outstandingPriAmt
                    res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                        receiptAmt=origLoanAmt, userId=self.userId)
                else:
                    pass
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_1_03_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_锡房贷====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_04_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_平安普惠(self):
        time.sleep(1.3)
        loanid = repuest.commonParam.set_flow(count=70,
                                              describe="test_1_04_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_平安普惠")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            mysql = repuest.commonParam.assect_accounts_loan(loanid)
            if mysql != ():
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                if mysql[0]['loan_status'] == 6:
                    res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                    res_plan_list = data.plan_list(loanid=loanid)
                    schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                    outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                    outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                    outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                    assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                    num = len(res_plan_list['result'])
                    numer = 0
                    for i in res_plan_list['result']:
                        numer += i['dueCapital']
                    print(numer)
                    assert numer == outstandingPriAmt
                    res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                        receiptAmt=origLoanAmt, userId=self.userId)
                else:
                    pass
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_1_04_接口正确不同渠道放款成功_调用还款是试算接口_可以正确查询出还款内容与还款计划相同_平安普惠====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_2_01_接口正确_还款日当天进行还款试算_可以正确的查询出信息(self):
        loanid = repuest.commonParam.set_flow(count=71,
                                              describe="test_2_01_接口正确_还款日当天进行还款试算_可以正确的查询出信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(5)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_2_01_接口正确_还款日当天进行还款试算_可以正确的查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_3_01_接口正确_案件已结清时进行还款试算_可以正确查询出信息(self):
        loanid = "20171204000017"
        try:
            # 案件需要跑批进行校验
            res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
            assert res['message'] == "失败:CL4014,CL4014 贷款号[null]发放号[null]客户号[null]借据号[20171204000017]对应的贷款信息不存在！"
            assert res['code'] == None
            assert res['success'] == False
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_3_01_接口正确_案件已结清时进行还款试算_可以正确查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_4_01_接口正确_案件已逾期进行还款试算_可以正确查询出信息(self):
        loanid = repuest.commonParam.set_flow(count=72,
                                              describe="test_4_01_接口正确_案件已逾期进行还款试算_可以正确查询出信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(5)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_4_01_接口正确_案件已逾期进行还款试算_可以正确查询出信息====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_5_01_接口正确_案件放款成功后进行还款试算_可以正确查询出信息(self):
        loanid = repuest.commonParam.set_flow(count=73,
                                              describe="test_5_01_接口正确_案件放款成功后进行还款试算_可以正确查询出信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_5_01_接口正确_案件放款成功后进行还款试算_可以正确查询出信息====断言失败，失败原：%s" % (e))

# 接口正确-非还款日进行还款试算-可以查询出相关信息
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_6_01_接口正确_非还款日进行还款试算_可以查询出相关信息(self):
        loanid = repuest.commonParam.set_flow(count=74,
                                              describe="test_6_01_接口正确_非还款日进行还款试算_可以查询出相关信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(5)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_6_01_接口正确_非还款日进行还款试算_可以查询出相关信息====断言失败，失败原：%s" % (e))

# 接口正确-案件存在宽限期时-可以查询出相关信息
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_7_01_接口正确_案件存在宽限期时_可以查询出相关信息(self):
        loanid = repuest.commonParam.set_flow(count=75,
                                              describe="test_7_01_接口正确_案件存在宽限期时_可以查询出相关信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(5)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="2").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_7_01_接口正确_案件存在宽限期时_可以查询出相关信息====断言失败，失败原：%s" % (e))

# 接口正确-还款类型不同-可以正确查询出相关信息
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="案件需要跑批")
    def test_8_01_接口正确_还款类型不同_可以正确查询出相关信息(self):
        loanid = repuest.commonParam.set_flow(count=76,
                                              describe="test_8_01_接口正确_还款类型不同_可以正确查询出相关信息")
        print(loanid)
        res = data.accounts_repayTrial(loanid=loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname,
                                            settleBaseAcctNo=lendingno)
            time.sleep(5)
            # 案件需要跑批进行校验
            mysql = repuest.commonParam.assect_accounts_loan(loanid)[0]
            if mysql['loan_status'] == 6:
                res = data.accounts_repayTrial(loanid=loanid, receiptType="4").json()
                res_plan_list = data.plan_list(loanid=loanid)
                schedTotalAmt = res["result"]['schedTotalAmt']  # 应还总额
                outstandingPriAmt = res['result']["outstandingPriAmt"]  # 应还本金
                outstandingIntAmt = res['result']["outstandingIntAmt"]  # 应还利息
                outstandingOdpAmt = res['result']['outstandingOdpAmt']  # 应还罚息
                assert schedTotalAmt == outstandingIntAmt + outstandingPriAmt + outstandingOdpAmt
                num = len(res_plan_list['result'])
                numer = 0
                for i in res_plan_list['result']:
                    numer += i['dueCapital']
                print(numer)
                assert numer == outstandingPriAmt
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
            else:
                pass
            mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                    userId=self.userId, receiptType="2")
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_8_01_接口正确_还款类型不同_可以正确查询出相关信息====断言失败，失败原：%s" % (e))

# 接口报文为空/为空字符串时-接口返回正确的错误提示
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="案件需要跑批")
    def test_9_01_接口正确_接口报文为空时_接口返回正确的错误提示(self):
        try:
            # 案件需要跑批进行校验
            res = data.accounts_repayTrial().json()
            # assert res['message'] == "body.receiptType:还款类型不能为空"
            assert res['code'] == None
            assert res['success'] == False
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_9_01_接口正确_接口报文为空时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="案件需要跑批")
    def test_9_03_接口正确_接口报文为空字符串时_接口返回正确的错误提示(self):
        try:
            # 案件需要跑批进行校验
            res = data.accounts_repayTrial().json()
            print(res)
            # assert res['message'] == "body.receiptType:还款类型不能为空"
            assert res['code'] == None
            assert res['success'] == False
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_9_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="案件需要跑批")
    def test_9_02_接口正确_接口报文缺少必填项_报文给出正确的错误提示(self):
        try:
            # 案件需要跑批进行校验
            res = data.accounts_repayTrial().json()
            # assert res['message'] == "body.cmisloanNo:借据号不能为空"
            assert res['code'] == None
            assert res['success'] == False
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_9_02_接口正确_接口报文为空字符串时_接口返回正确的错误提示====断言失败，失败原：%s" % (e))

# 接口正确-该案件订单号不存在-报文返回正确的错误提示
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="案件需要跑批")
    def test_10_01_接口正确_该案件订单号不存在_报文返回正确的错误提示(self):
        loanid = '20161202000051'
        try:
            # 案件需要跑批进行校验
            res = data.accounts_repayTrial(loanid=loanid,receiptType='2').json()
            assert res['message'] == "失败:CL4014,CL4014 贷款号[null]发放号[null]客户号[null]借据号[20161202000051]对应的贷款信息不存在！"
            assert res['code'] == None
            assert res['success'] == False
        except (ZeroDivisionError, NameError, TypeError) as e:
            loger.error("test_10_01_接口正确_该案件订单号不存在_报文返回正确的错误提示====断言失败，失败原：%s" % (e))
