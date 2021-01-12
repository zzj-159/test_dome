# -*- coding: utf-8 -*-
# @Time    : 2020/12/18
# @Author  :张正杰
# @Fuction :账务中心-老-还款查询

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


class Test_accountsRepayStatusQquery:

    def setup(self):
        self.userId = '010000004651'
        mysql = repuest.commonParam.accounts(self.userId)
        all = mysql[0]
        self.clientNo = all['client_no']

    def teardown(self):
        pass

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_01_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_锡车贷(self):
        loger.info("test_1_01_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=64,
                                              describe="test_1_01_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("万辰").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        print(assert_loan[0]['loan_status'])
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            assert_loanid = res_repay.json()['result']
            try:
                query = data.accounts_repayStatus_query(loanid=assert_loanid)
                assert query.status_code == 200
                assert query.json()['code'] == 0
                assert query.json()['result'] != None
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_1_01_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_锡机贷(self):
        loger.info("test_1_02_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_锡机贷====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=65,
                                              describe="test_1_02_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_锡机贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("锡机贷")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        # print(assert_loan[0]['loan_status'])
        if assert_loan != ():
            if assert_loan[0]['loan_status'] != 6:
                res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if assert_loan[0]['loan_status'] == 6:
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
                assert_loanid = res_repay.json()['result']
                try:
                    query = data.accounts_repayStatus_query(loanid=assert_loanid)
                    assert query.status_code == 200
                    assert query.json()['code'] == 0
                    assert query.json()['result'] != None
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_1_02_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_锡机贷====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_04_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_平安普惠(self):
        loger.info("test_1_04_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_平安普惠====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=66,
                                              describe="test_1_04_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_平安普惠")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        # print(assert_loan[0]['loan_status'])
        if assert_loan != ():
            if assert_loan[0]['loan_status'] != 6:
                res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if assert_loan[0]['loan_status'] == 6:
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
                assert_loanid = res_repay.json()['result']
                try:
                    query = data.accounts_repayStatus_query(loanid=assert_loanid)
                    assert query.status_code == 200
                    assert query.json()['code'] == 0
                    assert query.json()['result'] != None
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_1_04_案件正常_正常还款日调用还款接口_调用还款查询接口_可以正常查询出还款状态_平安普惠====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnin
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_01_接口正确_调用还款状态查询接口_报文中boday为空时_给出相应的错误提示(self):
        try:
            res_show = data.accounts_repayStatus_query()
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()["message"] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_01_接口正确_调用还款状态查询接口_报文中boday为空时_给出相应的错误提示====断言失败，失败原因：%s" % (e))

    @pytest.mark.filterwarnin
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_02_02_接口正确_调用还款状态查询接口_报文中boday为空字符串时_给出相应的错误提示(self):
        try:
            res_show = data.accounts_repayStatus_query(loanid="")
            print(res_show.text)
            res_show_assert = res_show.json()['result']
            assert res_show.json()['code'] == 0
            assert res_show.status_code == 200
            assert res_show.json()["message"] == None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_02_02_接口正确_调用还款状态查询接口_报文中boday为空字符串时_给出相应的错误提示====断言失败，失败原因：%s" % (e))
