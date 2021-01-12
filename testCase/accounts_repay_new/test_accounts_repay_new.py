# -*- coding: utf-8 -*-
# @Time    : 2020/12/14
# @Author  :张正杰
# @Fuction :账务中心-老-还款new

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


class Test_accounts_repay_new:
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
    def test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清(self):
        loger.info("test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=38,
                                              describe="test_accountsLoan_1_01_接口正常_一百万以下小额调用接口放款_可以正常放款且数据库中数据正常落库")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款(self):
        loger.info("test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=39,
                                              describe="test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款(self):
        loger.info("test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=40,
                                              describe="test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款")
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
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_车贷(self):
        loger.info("test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_车贷====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=41,
                                              describe="test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_车贷")
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
        # print(assert_loan[0]['loan_status'])
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_车贷====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷(self):
        loger.info("test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=42,
                                              describe="test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("安居客").split(',')[0]
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        # print(assert_loan[0]['loan_status'])
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_平安普惠(self):
        loger.info("test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=43,
                                              describe="test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷")
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
        if assert_loan !=():
            if assert_loan[0]['loan_status'] != 6:
                res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
            if assert_loan[0]['loan_status'] == 6:
                res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                    receiptAmt=origLoanAmt, userId=self.userId)
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_2_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_不同渠道_房贷====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_01_案件正常未到还款日非放款日当天进行还款_部分还款(self):
        loger.info("test_03_01_案件正常未到还款日非放款日当天进行还款_部分还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=44,
                                              describe="test_03_01_案件正常未到还款日非放款日当天进行还款_部分还款")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_03_01_案件正常未到还款日非放款日当天进行还款_部分还款====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_02_案件正常未到还款日非放款日当天进行还款_可以正常的还款且数据库正常_提前结清(self):
        loger.info("test_03_02_案件正常未到还款日非放款日当天进行还款_提前结清====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=45,
                                              describe="test_03_02_案件正常未到还款日非放款日当天进行还款_提前结清")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        time.sleep(3)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        # print(assert_loan[0]['loan_status'])
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_03_02_案件正常未到还款日非放款日当天进行还款_提前结清====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_03_案件正常未到还款日非放款日当天进行还款_给出相应的错误提示_正常还款(self):
        loger.info("test_03_03_案件正常未到还款日非放款日当天进行还款_正常还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=46,
                                              describe="test_03_03_案件正常未到还款日非放款日当天进行还款_正常还款")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_03_03_案件正常未到还款日非放款日当天进行还款_正常还款====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_03_04_案件正常_正常还款日当天进行还款_可以正确还款且数据库落库正确_正常还款(self):
        loger.info("test_03_04_案件正常_正常还款日当天进行还款_正常还款====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=47,
                                              describe="test_03_04_案件正常_正常还款日当天进行还款_正常还款")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_03_04_案件正常_正常还款日当天进行还款_正常还款====接口断言失败=====失败原因%s" % (e))

    # 案件异常（已逾期/已结清）-正常还款日进行还款/部分还款/逾期还款-可以正常的还款以及落库
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示(self):
        loger.info("test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=48,
                                              describe="test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示(self):
        loger.info("test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示====接口测试开始")
        loanid = '20171204000017'
        origLoanAmt = 2000
        res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="4",
                                            receiptAmt=origLoanAmt, userId=self.userId)
        seq_no = res_repay.json()['result']
        try:
            assert res_repay.json()['code'] == 0
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_04_01_案件已结清_还款日当天进行正常还款_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示(self):
        loger.info("test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=1,
                                              describe="test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示(self):
        loger.info("test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=49,
                                              describe="test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                    due_amount_all = 0
                    due_amount = res_repay_query.json()["result"]['repayDetails']
                    for i in due_amount:
                        due_amount_all += i['capital'] + i['interest'] + ['penalty']
                    assert due_amount_all == origLoanAmt
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_04_02_案件已结清_还款日当天进行提前结清_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_03_案件逾期_进行提前结清_可以正确还款且数据落库正常(self):
        loger.info("test_04_03_案件逾期_进行提前结清_可以正确还款且数据落库正常====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=50,
                                              describe="test_04_03_案件逾期_进行提前结清_可以正确还款且数据落库正常")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
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
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_04_03_案件逾期_进行提前结清_可以正确还款且数据落库正常====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_04_04_案件逾期_进行逾期还款_可以正确还款且数据落库正常(self):
        loger.info("test_04_04_案件逾期_进行逾期还款_可以正确还款且数据落库正常====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=51,
                                              describe="test_04_04_案件逾期_进行逾期还款_可以正确还款且数据落库正常")
        print(loanid)
        origLoanAmt = '50000.00'
        prod_type = repuest.commonParam.prod_type("平安普惠")
        lending = repuest.commonParam.lending(prod_type)[0]
        lendingname = lending['acct_name']
        lendingno = lending['acct_no']
        res = data.accounts_loan(loanid=loanid, clientNo=self.clientNo, userId=self.userId, origLoanAmt=origLoanAmt,
                                 prodType=prod_type, settleAcctName=lendingname, settleBaseAcctNo=lendingno)
        assert_loan = repuest.commonParam.assect_accounts_loan(loanid)
        # print(assert_loan[0]['loan_status'])
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error("test_04_04_案件逾期_进行逾期还款_可以正确还款且数据落库正常====接口断言失败=====失败原因%s" % (e))

    # 案件正常-正常还款6期后，提前结清时不收取服务费（不同渠道不同校验）
    @pytest.mark.filterwarnings
    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_05_01_案件正常_正常还款6期后进行提前结清不收取服务费_数据可以正常落库且数据正确还款查询中没有服务费_锡机贷(self):
        loger.info("test_05_01_案件正常_正常还款6期后进行提前结清不收取服务费_数据可以正常落库且数据正确还款查询中没有服务费_锡机贷====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=52,
                                              describe="test_05_01_案件正常_正常还款6期后进行提前结清不收取服务费_数据可以正常落库且数据正确还款查询中没有服务费_锡机贷")
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
        if assert_loan[0]['loan_status'] != 6:
            res_mock = data.mock_accounts(loanid=loanid, uppStatus=00)
        if assert_loan[0]['loan_status'] == 6:
            res_repay = data.accounts_repay_new(clientNo=self.clientNo, loanId=loanid, receiptType="2",
                                                receiptAmt=origLoanAmt, userId=self.userId)
            seq_no = res_repay.json()['result']
            try:
                assert res_repay.json()['code'] == 0
                res_repay_query = data.accounts_repayStatus_query(loanid=seq_no)
                due_amount_all = 0
                due_amount = res_repay_query.json()["result"]['repayDetails']
                for i in due_amount:
                    due_amount_all += i['capital'] + i['interest'] + ['penalty']
                assert due_amount_all == origLoanAmt
            except (ZeroDivisionError, TypeError, NameError) as e:
                loger.error(
                    "test_05_01_案件正常_正常还款6期后进行提前结清不收取服务费_数据可以正常落库且数据正确还款查询中没有服务费_锡机贷====接口断言失败=====失败原因%s" % (e))

    # 案件正常-正常还款的卡类型不同时，校验其还款是否可以正确还款（一类卡/二类卡）
    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_06_01_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_二类卡(self):
        loger.info("test_06_01_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_二类卡====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=53,
                                              describe="test_06_01_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_二类卡")
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
                                                    receiptAmt=origLoanAmt, userId=self.userId,
                                                    payerAcctNo='6236435330000002196')
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    repay_accounts = repuest.commonParam.repayment_log(loanid=loanid)
                    repay = repay_accounts[-1]['repay_acct_info']['payerAcctNo']
                    assert repay == '6236435330000002196'
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_06_01_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_二类卡====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.filterwarnings
    # @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_06_02_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_一类卡(self):
        loger.info("test_06_02_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_一类卡====接口测试开始")
        loanid = repuest.commonParam.set_flow(count=54,
                                              describe="test_06_02_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_一类卡")
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
                                                    receiptAmt=origLoanAmt, userId=self.userId,
                                                    payerAcctNo='6214832509940735')
                seq_no = res_repay.json()['result']
                try:
                    assert res_repay.json()['code'] == 0
                    repay_accounts = repuest.commonParam.repayment_log(loanid=loanid)
                    repay = repay_accounts[-1]['repay_acct_info']['payerAcctNo']
                    assert repay == '6214832509940735'
                except (ZeroDivisionError, TypeError, NameError) as e:
                    loger.error("test_06_02_案件正常_正常提前结清还款的卡类型不同时_校验其还款是否可以正常还款_一类卡====接口断言失败=====失败原因%s" % (e))

    # 接口报文为空/为空字符串时-接口返回正确的错误提示
    def test_07_01_接口正常_发送报文为空时_给出相应的错误提示(self):
        loger.info("test_07_01_接口正常_发送报文为空时_给出相应的错误提示====接口测试开始")
        res_repay = data.accounts_repay_new(receiptType='02', userId=self.userId)
        try:

            assert res_repay.json()['code'] != 0
            assert res_repay.json()['message'] in ["body.clientNo:核心客户号不能为空", "body.loanId:借据号不能为空"]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_07_01_接口正常_发送报文为空时_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    def test_07_02_接口正常_发送报文为空字符串时_给出相应的错误提示(self):
        loger.info("test_07_02_接口正常_发送报文为空字符串时_给出相应的错误提示====接口测试开始")
        res_repay = data.accounts_repay_new(receiptType='02', userId=self.userId, clientNo='', loanId='')
        try:
            assert res_repay.json()['code'] != 0
            assert res_repay.json()['message'] in ["body.clientNo:核心客户号不能为空", "body.loanId:借据号不能为空"]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_07_02_接口正常_发送报文为空字符串时_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))

    def test_08_01_接口正常_接口报文缺少必填项时_给出相应的错误提示(self):
        loger.info("test_08_01_接口正常_接口报文缺少必填项时_给出相应的错误提示====接口测试开始")
        res_repay = data.accounts_repay_new(receiptType='02', userId=self.userId, loanId='')
        try:
            assert res_repay.json()['code'] != 0
            assert res_repay.json()['message'] in ["body.clientNo:核心客户号不能为空", "body.loanId:借据号不能为空"]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_08_01_接口正常_接口报文缺少必填项时_给出相应的错误提示====接口断言失败=====失败原因%s" % (e))
