# -*- coding: utf-8 -*-
# @Time    : 2020/12/1
# @Author  :张正杰
# @Fuction :账务中心-老-放款接口

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


class Test_accounts_reloan:
    # def __init__(self,ipList):
    #     self.ipList = ipList
    #     return

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown_class(self):
        pass
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_01_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡机贷(self):
        loger.info("=====test_1_01_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=25,
                                              describe="test_1_01_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            # res_mock = data.mock_accounts(loanid=loanid, uppStatus=01)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_1_01_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库======返回报文：%s" % (res.text))
            time.sleep(2)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            print(res.text)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡车贷(self):
        loger.info("=====test_1_02_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡车贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=26,
                                              describe="test_1_02_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        lending = repuest.commonParam.lending(prod_type.split(",")[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(",")[0], settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(",")[0], settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_1_02_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡车贷======返回报文：%s" % (res.text))
            time.sleep(2)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡车贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡房贷(self):
        loger.info("=====test_1_03_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=27,
                                              describe="test_1_03_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_1_03_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡房贷======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_03_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_锡房贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_04_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_平安普惠(self):
        loger.info("=====test_1_04_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_平安普惠=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=28,
                                              describe="test_1_04_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type.split(",")[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(",")[0], settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(",")[0], settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_1_04_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_平安普惠======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_接口正常放款失败_调用重新放款接口放款一百万以下小额放款_可以正常放款且数据库中数据正常落库_平安普惠====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_1_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡机贷(self):
        loger.info("=====test_02_1_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡机贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=29,
                                              describe="test_02_1_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡机贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_02_1_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡机贷======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if res.json()['code'] == 0:
                assert res.json()['code'] == 0
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_1_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡机贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_02_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡房贷(self):

        loger.info("=====test_02_02_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=30,
                                              describe="test_02_02_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡房贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_02_02_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡房贷======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_02_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡房贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_03_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡车贷(self):
        loger.info("=====test_02_03_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡车贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=31,
                                              describe="test_02_03_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡车贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        lending = repuest.commonParam.lending(prod_type.split(",")[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(",")[0], settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(",")[0], settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_02_03_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡车贷======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:

                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_03_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_锡车贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_04_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_平安普惠(self):
        loger.info("=====test_02_04_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_平安普惠=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=32,
                                              describe="test_02_04_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_平安普惠")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(",")[0], settleAcctName=lendingname,
                                            payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(",")[0], settleAcctName=lendingname,
                                       settleBaseAcctNo=lendingno)
            loger.info("test_02_04_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_平安普惠======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            print(res.text)
            if res.json()['code'] == 0:
                assert res.json()['code'] == 0
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_04_接口正常且放款失败_调用重新放款接口一百万以上大额放款_可以正常的调用核算接口且数据库中正确显示_平安普惠====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_1_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡机贷(self):

        loger.info("=====test_03_1_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡机贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=33,
                                              describe="test_03_1_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡机贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, payeeCertType="02", settleAcctName=lendingname, payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, payeeCertType="02", settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_03_1_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡机贷======返回报文：%s" % (res.text))
            time.sleep(5)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_03_1_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡机贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_2_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡车贷(self):
        loger.info("=====test_03_2_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡车贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=34,
                                              describe="test_03_2_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split('.')[0], payeeCertType="02", settleAcctName=lendingname,
                                            payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split('.')[0], payeeCertType="02", settleAcctName=lendingname,
                                       settleBaseAcctNo=lendingno)
            loger.info("test_03_2_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡车贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if res.json()['code'] == 0:
                assert res.json()['code'] == 0
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_03_2_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡车贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_3_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡房贷(self):
        loger.info("=====test_03_3_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=35,
                                              describe="test_03_3_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type, payeeCertType="02", settleAcctName=lendingname,
                                            payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type, payeeCertType="02", settleAcctName=lendingname,
                                       settleBaseAcctNo=lendingno)
            loger.info("test_03_3_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡房贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_03_3_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_锡房贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_4_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_平安普惠(self):
        loger.info("=====test_03_4_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_平安普惠=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=36,
                                              describe="test_03_4_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(',')[0], payeeCertType="02", settleAcctName=lendingname,
                                            payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(',')[0], payeeCertType="02", settleAcctName=lendingname,
                                       settleBaseAcctNo=lendingno)
            loger.info("test_03_4_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_平安普惠======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            # assert res.json()['code'] == 0
            if res.json()['code'] == 0:
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
            else:
                assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_03_4_接口正常放款对公账户放款失败_调用重新放款接口可以正常放款且数据库中数据正确显示_平安普惠====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_01_接口正常放款对公账户放款失败_重新放款接口案件还款方式不同_数据库中数据存储不同且数据库中数据正确(self):
        loger.info("=====test_04_01_接口正常放款对公账户放款失败_重新放款接口案件还款方式不同_数据库中数据存储不同且数据库中数据正确=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=37,
                                              describe="test_04_01_接口正常放款对公账户放款失败_重新放款接口案件还款方式不同_数据库中数据存储不同且数据库中数据正确")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res_normal = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                            origLoanAmt=origLoanAmt,
                                            prodType=prod_type.split(',')[0], payeeCertType="02",schedMode='2',
                                            settleAcctName=lendingname,
                                            payeeAcctNo='',
                                            settleBaseAcctNo=lendingno)
            time.sleep(3)
            res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                       origLoanAmt=origLoanAmt,
                                       prodType=prod_type.split(',')[0], payeeCertType="02",schedMode='2', settleAcctName=lendingname,
                                       settleBaseAcctNo=lendingno)
            loger.info("test_04_01_接口正常放款对公账户放款失败_重新放款接口案件还款方式不同_数据库中数据存储不同且数据库中数据正确======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if res.json()['code'] == 0:
                assert res.json()['code'] == 0
                assert assert_loan[1]["user_id"] == self.userId
                assert assert_loan[1]['partner_id'] == 'JZE'
                # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                # assert assert_loan[1]['loan_status'] == res_show_assert['loanStatus']
                mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo, origLoanAmt=origLoanAmt,
                                                        userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_04_01_接口正常放款对公账户放款失败_重新放款接口案件还款方式不同_数据库中数据存储不同且数据库中数据正确====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__5_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示(self):

        loger.info("=====test__5_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示=======接口测试开始")

        try:
            res = data.accounts_reloan()
            loger.info("test__5_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示======返回报文：%s" % (res.text))
            # time.sleep(3)
            print(res.json())
            if res.json()['code'] == 0:
                assert res.json()['code'] == 0
            else:
                assert res.json()['code'] == None
            # assert res.json()['message'] == "失败:状态不支持重新放款"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__5_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__5_01_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示(self):
        loger.info("=====test__5_01_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示=======接口测试开始")

        try:
            res = data.accounts_reloan(loanid="", clientNo="", userId="",
                                            origLoanAmt="",
                                            prodType="")
            loger.info("test__5_01_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示======返回报文：%s" % (res.text))
            # time.sleep(3)
            assert res.json()['code'] == None
            assert res.json()['message'] == "失败:不存在放款记录"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__5_01_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示====断言失败，失败原因：%s" % (e))


#
# if __name__ == "__main__":
    # ipList = ['192.168.2.1', '192.168.2.2','192.168.2.3','192.168.2.4','192.168.2.5']
    # pytest.main(['-s', '--workers=5', '--tests-per-worker=6', __file__])
