# -*- coding: utf-8 -*-
# @Time    : 2020/12/14
# @Author  :张正杰
# @Fuction :账务中心-新-还款
from time import sleep

import pytest

from InterfaceData.Interface_Data import Interface_Data
from common.dataVariable import Respont

rep = Respont()
loger = rep.Mylog
data = Interface_Data()

class Test_V2_Repay:
    def setup(self):
        # self.loanId = rep.commonParam.set_flow(count=2,describe='测试账单中心新接口放款接口(/v2/loan)') #创建订单
        self.userId = '010000003616'   #客户userId
        self.clientNo = rep.commonParam.accounts(self.userId)[0]['client_no'] #客户号
    def teardown(self):
        rep.Mylog.info("========测试结束,清除数据========= ")
        print("========测试结束========= ")

    def test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡机贷(self):
        loger.info("=====test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清=======接口测试开始")
        loanAmount = 30000

        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='锡机贷',
                                                       partnerId='YQT', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(7)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡机贷====接口断言失败=====失败原因%s" % (e))

    def test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡车贷(self):
        loger.info("=====test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡车贷=======接口测试开始")
        loanAmount = 30000

        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='金泽',
                                                       partnerId='JZ', loanAmount=loanAmount)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡车贷====接口断言失败=====失败原因%s" % (e))


    def test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡房贷(self):
        loger.info("=====test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡房贷=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='安居客',
                                                       partnerId='AJK', loanAmount=loanAmount)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_03_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_锡房贷====接口断言失败=====失败原因%s" % (e))

    def test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生(self):
        loger.info("=====test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='长安新生',
                                                       partnerId='CAXS', loanAmount=loanAmount)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))

    def test_1_05_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_平安普惠(self):
        loger.info("=====test_1_05_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_平安普惠=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='平安普惠',
                                                       partnerId='PAPH', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款(self):
        loger.info("=====test_2_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_部分还款=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='平安普惠',
                                                       partnerId='PAPH', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId,uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_3_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款(self):
        loger.info("=====test_3_01_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_正常还款日还款=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId,
                                                       prod_type_desc='平安普惠',
                                                       partnerId='PAPH', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_4_01_案件异常已逾期_正常还款日进行还款部分还款逾期还款_可以正常的还款以及落库(self):
        loger.info("=====test_4_01_案件异常已逾期_正常还款日进行还款部分还款逾期还款_可以正常的还款以及落库=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId,
                                                       prod_type_desc='平安普惠',
                                                       partnerId='PAPH', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))

    @pytest.mark.skip(reason="订单放款交互账务中心")
    def test_4_02_案件异常已结清_正常还款日进行还款部分还款逾期还款_可以正常的还款以及落库(self):
        loger.info("=====test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生=======接口测试开始")
        loanAmount = 30000
        try:
            loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId,
                                                       prod_type_desc='平安普惠',
                                                       partnerId='PAPH', loanAmount=loanAmount)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus='00')
            db_result2 = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result2)
            # assert db_result2[0]['loan_status'] == 6
            if db_result2[0]['loan_status'] == 6:
                loger.info("=====进行提前结清======")
                print("=====进行提前结清======")
                re = data.accounts_V2_repay(loanId=loanId, userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR" + loanId, receiptType='2')
                res = re.json()
                assert res['code'] == 0
                sleep(5)
                db_repay = rep.commonParam.assect_accounts_repay(loanId)
                print(db_repay)
                assert db_repay[0]['repay_status'] in [6, 8]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_案件正常_正常还款日调用还款接口_可以正确的还款以及落库_提前结清_长安新生====接口断言失败=====失败原因%s" % (e))


    def test_5_01_接口报文为空_接口返回正确的错误提示(self):
        loger.info("=====test_5_01_接口报文为空_接口返回正确的错误提示=======接口测试开始")
        loanAmount = 30000
        try:
                re = data.accounts_V2_repay(loanId='', userId=self.userId, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, reqSeqNo="PLMR", receiptType='2')
                res = re.json()
                print(res)
                assert res['success'] == False
                assert res['message'] == 'body.loanId:借据号不能为空'
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_01_接口报文为空_接口返回正确的错误提示====接口断言失败=====失败原因%s" % (e))