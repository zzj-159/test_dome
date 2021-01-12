# -*- coding: utf-8 -*-
# @Time    : 2020/12/1
# @Author  :张正杰
# @Fuction :账务中心-老-放款接口

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


class Test_accountsLoan:

    def setup_class(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown_class(self):
        pass

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷(self):
        loger.info("=====test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=1,
                                              describe="test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    #     银行卡的校验
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=2)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_02_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷(self):
        loger.info("=======test_01_02_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=2,
                                              describe="test_01_02_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name'][0]
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_02_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_03_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷(self):
        loger.info("=======test_01_03_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=3,
                                              describe="test_01_03_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_03_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=4)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_01_04_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠(self):
        loger.info("=======test_01_04_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=4,
                                              describe="test_01_04_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_01_04_accounts_loan_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=5)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__2_01_接口正常_一百万以上大额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷(self):
        loger.info("=====test__2_01_接口正常_一百万以上大额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=5,
                                              describe="test__2_01_接口正常_一百万以上大额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            loger.info("test__2_01_接口正常_一百万以上大额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷======返回报文：%s" % (res.text))
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__2_01_接口正常_一百万以上大额调用接口放款_可以正常放款且数据库中数据正常落库_锡机贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=6)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_02_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷(self):
        loger.info("=======test_02_02_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=6,
                                              describe="test_02_02_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0

                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_02_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡车贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=7)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_03_接口正常_一百万以下大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷(self):
        loger.info("=======test_02_03_接口正常_一百万以下大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=7,
                                              describe="test_02_03_接口正常_一百万以下大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            print(res.text)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_03_接口正常_一百万以下大额放款调用接口放款_可以正常放款且数据库中数据正常落库_锡房贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=8)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_04_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠(self):
        loger.info("=======test_02_04_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=8,
                                              describe="test_02_04_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            print(res.text)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_04_接口正常_一百万以上大额放款调用接口放款_可以正常放款且数据库中数据正常落库_平安普惠===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=9)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__3_01_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡机贷(self):
        loger.info("=====test__3_01_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡机贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=9,
                                              describe="test__3_01_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡机贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, payeeCertType="02", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            loger.info("test__3_01_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡机贷======返回报文：%s" % (res.text))
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__3_01_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡机贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=10)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_02_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡车贷(self):
        loger.info("=======test_3_02_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡车贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=10,
                                              describe="test_3_02_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], payeeCertType="02", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)

            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_02_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡车贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=11)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_03_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡房贷(self):
        loger.info("=======test_3_03_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡房贷=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=11,
                                              describe="test_3_03_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡房贷")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("安居客")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, payeeCertType="02", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    assert bank_card['payeeCertType'] == "02"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_03_接口正常_对公账户放款_可以正常放款且数据库中数据正常落库_锡房贷===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=12)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_04_接口正常_对公账户放款款_可以正常放款且数据库中数据正常落库_平安普惠(self):
        loger.info("=======test_3_04_接口正常_对公账户放款款_可以正常放款且数据库中数据正常落库_平安普惠=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=12,
                                              describe="test_3_04_接口正常_对公账户放款款_可以正常放款且数据库中数据正常落库_平安普惠")
        print(loanid)
        origLoanAmt = '1010000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], payeeCertType="02", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    assert bank_card['payeeCertType'] == "02"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_04_接口正常_对公账户放款款_可以正常放款且数据库中数据正常落库_平安普惠===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=13)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_4_01_接口正常_案件还款方式不同放款_可以正常放款且数据库中数据正常落库(self):
        loger.info("=======test_4_01_接口正常_案件还款方式不同放款_可以正常放款且数据库中数据正常落库=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=13,
                                              describe="test_4_01_接口正常_案件还款方式不同放款_可以正常放款且数据库中数据正常落库")
        print(loanid)
        origLoanAmt = '30000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            # 1 等额本息
            # * 2 等额本金
            # * 3 一次还本付息/前收息
            # * 4 按频率付息、一次还本
            # * 5 按频率付息、任意本金
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], payeeCertType="02", schedMode='2',
                                     settleAcctName=lendingname, settleBaseAcctNo=lendingno)
            time.sleep(3)
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == "6236435330000014233"
                    assert bank_card['payeeCertType'] == "02"
                    mock = repuest.commonParam.oracle_repay(loanid=loanid, clientNo=self.clientNo,
                                                            origLoanAmt=origLoanAmt,
                                                            userId=self.userId, receiptType="2")
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_4_01_接口正常_案件还款方式不同放款_可以正常放款且数据库中数据正常落库===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=14)
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_5_01_接口正确_放款成功校验不同渠道的账单日_锡车贷对日还款(self):
        loger.info("=======test_5_01_接口正确_放款成功校验不同渠道的账单日_锡车贷对日还款=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=14,
                                              describe="test_5_01_接口正确_放款成功校验不同渠道的账单日_锡车贷对日还款")
        print(loanid)
        origLoanAmt = '30000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        print(prod_type.split(',')[0])
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], payeeCertType="01", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            num = 1
            while True:
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                res_show = data.accounts_loan_show(loanid=loanid)
                res_show_assert = res_show.json()['result']
                num += 1
                if res_show_assert['loanStatus'] == 6:
                    reimbursement = data.plan_list(loanid=loanid)
                    monts = repuest.commonParam.Date_processing(start=reimbursement.json()['result'][0]["dueDate"],
                                                                end=res_show_assert['loanDate'])
                    assert monts == 1
                    break
                elif res_show_assert['loanStatus'] == 4 or 7:
                    res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                               origLoanAmt=origLoanAmt,
                                               prodType=prod_type.split(',')[0], payeeCertType="01",
                                               settleAcctName=lendingname,
                                               settleBaseAcctNo=lendingno)
                    loger.info("放款失败===重新放款")
                    if assert_loan[0]['loan_status'] == 6:
                        res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                            receiptAmt=origLoanAmt, userId=self.userId)
                    else:
                        pass
                    if num == 2:
                        break
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_01_接口正确_放款成功校验不同渠道的账单日_锡车贷对日还款===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=15)
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_5_02_接口正确_放款成功校验不同渠道的账单日_锡机贷对日还款(self):
        loger.info("=======test_5_02_接口正确_放款成功校验不同渠道的账单日_锡机贷对日还款=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=15,
                                              describe="test_5_02_接口正确_放款成功校验不同渠道的账单日_锡机贷对日还款")
        print(loanid)
        origLoanAmt = '30000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, payeeCertType="01", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            num = 1
            while True:
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                res_show = data.accounts_loan_show(loanid=loanid)
                res_show_assert = res_show.json()['result']
                num += 1
                if res_show_assert['loanStatus'] == 6:
                    reimbursement = data.plan_list(loanid=loanid)
                    monts = repuest.commonParam.Date_processing(start=reimbursement.json()['result'][0]["dueDate"],
                                                                end=res_show_assert['loanDate'])
                    assert monts == 1
                    break
                elif res_show_assert['loanStatus'] == 4 or 7:
                    res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                               origLoanAmt=origLoanAmt,
                                               prodType=prod_type, payeeCertType="01",
                                               settleAcctName=lendingname,
                                               settleBaseAcctNo=lendingno)
                    loger.info("放款失败===重新放款")
                    if assert_loan[0]['loan_status'] == 6:
                        res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                            receiptAmt=origLoanAmt, userId=self.userId)
                    else:
                        pass
                    if num == 2:
                        break
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_02_接口正确_放款成功校验不同渠道的账单日_锡机贷对日还款===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=16)
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款(self):
        loger.info("=======test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=16,
                                              describe="test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款")
        print(loanid)
        origLoanAmt = '30000.00'
        prod_type = repuest.commonParam.prod_type("苏州蓝蝎")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, payeeCertType="01", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            num = 1
            while True:
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                res_show = data.accounts_loan_show(loanid=loanid)
                res_show_assert = res_show.json()['result']
                num += 1
                if res_show_assert['loanStatus'] == 6:
                    reimbursement = data.plan_list(loanid=loanid)
                    monts = repuest.commonParam.Date_processing(start=reimbursement.json()['result'][0]["dueDate"],
                                                                end=res_show_assert['loanDate'])
                    assert monts == 1
                    break
                elif res_show_assert['loanStatus'] == 4 or 7:
                    res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                               origLoanAmt=origLoanAmt,
                                               prodType=prod_type, payeeCertType="01",
                                               settleAcctName=lendingname,
                                               settleBaseAcctNo=lendingno)
                    loger.info("放款失败===重新放款")
                    if assert_loan[0]['loan_status'] == 6:
                        res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                            receiptAmt=origLoanAmt, userId=self.userId)
                    else:
                        pass
                    if num == 2:
                        break
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=17)
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_5_04_接口正确_放款成功校验不同渠道的账单日_平安普惠对日还款(self):
        loger.info("=======test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款=====接口运行开始")
        loanid = repuest.commonParam.set_flow(count=17,
                                              describe="test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款")
        print(loanid)
        origLoanAmt = '30000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        print(prod_type)
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(',')[0], payeeCertType="01", settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno)
            time.sleep(3)
            num = 1
            while True:
                assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
                res_show = data.accounts_loan_show(loanid=loanid)
                res_show_assert = res_show.json()['result']
                num += 1
                if res_show_assert['loanStatus'] == 6:
                    reimbursement = data.plan_list(loanid=loanid)
                    monts = repuest.commonParam.Date_processing(start=reimbursement.json()['result'][0]["dueDate"],
                                                                end=res_show_assert['loanDate'])
                    assert monts == 1
                    break
                elif res_show_assert['loanStatus'] == 4 or 7:
                    res = data.accounts_reloan(loanid=loanid, clientNo=self.clientNo, userId=self.userId,
                                               origLoanAmt=origLoanAmt,
                                               prodType=prod_type.split(",")[0], payeeCertType="01",
                                               settleAcctName=lendingname,
                                               settleBaseAcctNo=lendingno)
                    loger.info("放款失败===重新放款")
                    if assert_loan[0]['loan_status'] == 6:
                        res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                            receiptAmt=origLoanAmt, userId=self.userId)
                    else:
                        pass
                    if num == 2:
                        break
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_03_接口正确_放款成功校验不同渠道的账单日_锡房贷对日还款===断言失败----失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=18)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__6_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示(self):

        loger.info("=====test__6_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示=======接口测试开始")

        try:
            res = data.accounts_loan()
            if res.text != '':
                loger.info("test__6_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示======返回报文：%s" % (res.text))
            time.sleep(3)
            assert res.json()['code'] == None
            assert res.json()['message'] == "body.userId:互金用户ID不能为空"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__6_01_接口正常_接口报文中数据为空时_接口给出相应的异常处理给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.run(order=19)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__6_02_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示(self):
        loger.info("=====test__6_02_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示=======接口测试开始")

        try:
            res = data.accounts_loan()
            if res.text != '':
                loger.info("test__6_02_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示======返回报文：%s" % (res.text))
                time.sleep(3)
                assert res.json()['code'] == None
                assert res.json()['message'] == "body.userId:互金用户ID不能为空"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__6_02_接口正常_接口报文中数据为空字符串时_接口给出相应的异常处理给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=20)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__7_01_接口正常_接口报文中数据必填项数据为空缺少一个或两给必填项时_接口给出相应的异常处理给出错误提示(self):
        loger.info("=====test__7_01_接口正常_接口报文中数据必填项数据为空缺少一个或两给必填项时_接口给出相应的异常处理给出错误提示=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=1,
                                              describe="test__7_01_接口正常_接口报文中数据必填项数据为空缺少一个或两给必填项时_接口给出相应的异常处理给出错误提示")
        try:
            res = data.accounts_loan(loanid=loanid)
            if res.text != '':
                loger.info("test__7_01_接口正常_接口报文中数据必填项数据为空缺少一个或两给必填项时_接口给出相应的异常处理给出错误提示======返回报文：%s" % (res.text))
                time.sleep(3)
                assert res.json()['code'] == None
                assert res.json()['message'] == "body.userId:互金用户ID不能为空"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__7_01_接口正常_接口报文中数据必填项数据为空缺少一个或两给必填项时_接口给出相应的异常处理给出错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=21)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__8_01_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库(self):
        loger.info("=====test__8_01_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=18,
                                              describe="test__8_01_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡机贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno,
                                     payeeAcctNo="")
            loger.info("test__8_01_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    # assert assert_loan[0]['upp_result'] == "收款人账号"
                    #     银行卡的校验
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == ""
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__8_01_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=22)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__8_02_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡房贷(self):
        loger.info("=====test__8_02_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡房贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=29,
                                              describe="test__8_02_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("苏州蓝蝎")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno,
                                     payeeAcctNo="")
            loger.info("test__8_02_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡房贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    # assert assert_loan[0]['loan_amount'] == decimal.Decimal(origLoanAmt)
                    # assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    # assert assert_loan[0]['upp_result'] == "收款人账号"
                    #     银行卡的校验
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == ""
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__8_02_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡房贷====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.run(order=23)
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test__8_03_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡车贷(self):
        loger.info("=====test__8_03_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡车贷=======接口测试开始")
        loanid = repuest.commonParam.set_flow(count=20,
                                              describe="test__8_03_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡车贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰")
        lending = repuest.commonParam.lending(prod_type.split(',')[0])[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        try:
            res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                     prodType=prod_type.split(",")[0], settleAcctName=lendingname,
                                     settleBaseAcctNo=lendingno, payeeAcctNo="")
            loger.info("test__8_03_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡车贷======返回报文：%s" % (res.text))
            time.sleep(3)
            res_show = data.accounts_loan_show(loanid=loanid)
            res_show_assert = res_show.json()['result']
            assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
            if res.text != '':
                if res.json()['code'] == 0:
                    assert res.json()['code'] == 0
                    assert assert_loan[0]["user_id"] == self.userId
                    assert assert_loan[0]['partner_id'] == 'JZE'
                    assert assert_loan[0]['loan_status'] == res_show_assert['loanStatus']
                    # assert assert_loan[0]['upp_result'] == "收款人账号"
                    #     银行卡的校验
                    bank_card = json.loads(assert_loan[0]['pay_info'])
                    assert bank_card['payeeAcctNo'] == ""
                else:
                    assert res.json()['code'] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test__8_03_接口正常_放款银行卡异常_放款失败_可以正常放款且数据库中数据正常落库_锡车贷====断言失败，失败原因：%s" % (e))
