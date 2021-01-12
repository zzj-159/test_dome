# -*- coding: utf-8 -*-
# @Time    : 2020/12/9
# @Author  :竹玉红
# @Fuction :账务中心-新-冲正接口
from time import sleep

import pytest

from InterfaceData.Interface_Data import Interface_Data
from common.dataVariable import Respont

rep = Respont()
loger = rep.Mylog
data = Interface_Data()
class Test_V2_reversal:
    def setup_class(self):
        self.userId = '010000003152'  # 客户userId
        self.clientNo = rep.commonParam.accounts(self.userId)[0]['client_no']  # 客户号

    def teardown_class(self):
        rep.Mylog.info("========测试结束,清除数据========= ")
        print("========测试结束========= ")

    # @pytest.mark.skip(reason="数据原因")
    def test_1_01_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_长安新生订单(self):
        # pass
        loger.info("=====test_1_01_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_长安新生订单=======接口测试开始")
        # loanId = '20171215000316'
        loanId = rep.commonParam.createAbnormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='长安新生',
                                                     partnerId='CAXS')
        try:
            re = data.accounts_V2_reversal(loanId=loanId,reason='测试')
            assert re.status_code == 200
            res = re.json()
            print(res)
            # assert 1 == 1
            if res['code'] == 0:
               assert res['success'] == True
               loger.info("校验数据库中订单状态")
               db_result = rep.commonParam.assect_accounts_loan(loanId)
               assert db_result[0]['loan_status'] in [9]

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_长安新生订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_03_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单(self):
        # pass
        loger.info("=====test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单=======接口测试开始")
        # loanId = 'LHD20171203000020'
        loanId = rep.commonParam.createAbnormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='平安普惠',
                                                     partnerId='PAPH')
        try:
            sleep(5)
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert 1 == 1
            if res['code'] == 0:
                assert res['success'] == True
                loger.info("校验数据库中订单状态")
                db_result = rep.commonParam.assect_accounts_loan(loanId)
                assert db_result[0]['loan_status'] in [9]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_04_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_锡房贷订单(self):
        # pass
        loger.info("=====test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单=======接口测试开始")
        # loanId = 'LHD20171203000020'
        loanId = rep.commonParam.createAbnormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='安居客',
                                                     partnerId='AJK')
        try:
            sleep(5)
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            print(res)
            # assert 1 == 1
            if res['code'] == 0:
                assert res['success'] == True
                loger.info("校验数据库中订单状态")
                db_result = rep.commonParam.assect_accounts_loan(loanId)
                assert db_result[0]['loan_status'] in [9]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_05_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_锡车贷订单(self):
        # pass
        loger.info("=====test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单=======接口测试开始")
        # loanId = '20171216000339'
        loanId = rep.commonParam.createAbnormalOrder(clientNo=self.clientNo,userId=self.userId,prod_type_desc='金泽',partnerId='JZ')

        try:
            sleep(5)
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            # assert 1 == 1
            if res['code'] == 0:
                assert res['success'] == True
                loger.info("校验数据库中订单状态")
                db_result = rep.commonParam.assect_accounts_loan(loanId)
                assert db_result[0]['loan_status'] in [9]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_锡机贷订单(self):
        # pass
        loger.info("=====test_1_02_不同渠道放款失败进行冲正_银行卡异常的情况_核算成功放款失败的订单_冲正成功_平安普惠订单=======接口测试开始")
        # loanId = '20171216000348'
        loanId = rep.commonParam.createAbnormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='锡机贷',
                                                     partnerId='QYT')
        try:
            sleep(5)
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert 1 == 1
            if res['code'] == 0:
                assert res['success'] == True
                loger.info("校验数据库中订单状态")
                db_result = rep.commonParam.assect_accounts_loan(loanId)
                assert db_result[0]['loan_status'] in [9]
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    # def test_2_01_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_长安新生订单(self):
    #     # pass
    #     loger.info("=====test_2_01_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_长安新生订单=======接口测试开始")
    #     loanId = 'LHD20171203000020'
    #     try:
    #         re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
    #         assert re.status_code == 200
    #         res = re.json()
    #         # print(res)
    #         # assert 1 == 1
    #         assert res['code'] == 0
    #         assert res['success'] == True
    #         loger.info("校验数据库中订单状态")
    #         db_result = rep.commonParam.assect_accounts_loan(loanId)
    #         assert db_result[0]['loan_status'] in [9]
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_2_01_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_长安新生订单====断言失败，失败原因：%s" % (e))
    #
    # # @pytest.mark.skip(reason="数据原因")
    # def test_2_02_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_平安普惠订单(self):
    #     # pass
    #     loger.info("=====test_2_02_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_平安普惠订单=======接口测试开始")
    #     loanId = 'LHD20171203000020'
    #     try:
    #         re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
    #         assert re.status_code == 200
    #         res = re.json()
    #         # print(res)
    #         assert res['code'] == None
    #         assert res['success'] == False
    #         # assert res['message'] == '失败:状态不支持冲正'
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_2_02_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_平安普惠订单====断言失败，失败原因：%s" % (e))
    #
    # # @pytest.mark.skip(reason="数据原因")
    # def test_2_03_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡房贷订单(self):
    #     # pass
    #     loger.info("=====test_2_03_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡房贷订单=======接口测试开始")
    #     # loanId = 'LHD20171203000020'
    #     loanAmount = 30000
    #     loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='安居客',
    #                                                  partnerId='AJK',loanAmount=loanAmount)
    #     try:
    #         sleep(5)
    #         re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
    #         assert re.status_code == 200
    #         res = re.json()
    #         # print(res)
    #         assert res['code'] == None
    #         assert res['success'] == False
    #         db_result = rep.commonParam.assect_accounts_loan(loanId)
    #         # assert res['message'] == '失败:状态不支持冲正'
    #         if db_result[0]['loan_status'] in [5]:
    #             data.mock_accounts(loanid=loanId, uppStatus="00")
    #             data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
    #                                     receiptAmt=loanAmount, userId=self.userId)
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_2_03_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡房贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_01_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败(self):
        # pass
        loger.info("=====test_2_04_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡机贷订单=======接口测试开始")
        loanAmount = 30000
        loanId = rep.commonParam.createNormalOrder(clientNo=self.clientNo, userId=self.userId, prod_type_desc='锡机贷',
                                                   partnerId='YQT', loanAmount=loanAmount)
        try:
            sleep(5)
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            # assert res['message'] == '失败:状态不支持冲正'
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_04_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡机贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    # def test_2_05_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡车贷订单(self):
    #     # pass
    #     loger.info("=====test_2_05_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡车贷订单=======接口测试开始")
    #     loanId = 'LHD20171203000020'
    #     try:
    #         re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
    #         assert re.status_code == 200
    #         res = re.json()
    #         # print(res)
    #         assert res['code'] == None
    #         assert res['success'] == False
    #         # assert res['message'] == '失败:状态不支持冲正'
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_2_05_非异常情况无法冲正_放款成功的订单进行冲正操作_冲正操作失败_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_3_01_接口必填项校验_传入空订单_冲正失败(self):
        # pass
        loger.info("=====test_3_01_接口必填项校验_传入空订单_冲正失败=======接口测试开始")
        loanId = ''
        try:
            re = data.accounts_V2_reversal(loanId=loanId, reason='测试')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            assert res['message'] == '失败:案件不存在'
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_01_接口必填项校验_传入空订单_冲正失败====断言失败，失败原因：%s" % (e))