# -*- coding: utf-8 -*-
# @Time    : 2020/12/2
# @Author  : 竹玉红
# @Fuction : 账务中心-新-放款接口-锡车贷渠道
import json
from time import sleep

import pytest

from InterfaceData.Interface_Data import Interface_Data
from common.dataVariable import Respont

rep = Respont()
loger = rep.Mylog
data = Interface_Data()

class Test_V2Loan_car:
    def setup(self):
        # self.loanId = rep.commonParam.set_flow(count=109,describe='测试账单中心新接口放款接口(/v2/loan)') #创建订单
        self.userId = '010000003616'   #客户userId
        self.clientNo = rep.commonParam.accounts(self.userId)[0]['client_no'] #客户号
    def teardown(self):
        rep.Mylog.info("========测试结束,清除数据========= ")
        print("========测试结束========= ")

    # @pytest.mark.skip(reason="数据原因")
    def test_1_01_正常放款一百万以下的小额放款_传入贷款金额小于100万_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        loger.info("=====test_1_01_正常放款一百万以下的小额放款_传入贷款金额小于100万_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s"%(loanId))
        print("创建的订单号：",loanId)
        loanAmount = 700
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        print(prod_type)
        try:
            re = data.accounts_V2_loan(loanId=loanId,loanAmount=loanAmount,prodType=prod_type,clientNo=self.clientNo,
                                       userId=self.userId,partnerId='JZ')
            loger.info("test_1_01_正常放款一百万以下的小额放款_传入贷款金额小于100万_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount']-loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'],db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,5,6,4],loan_rsult

            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId,receiptType=2,clientNo=self.clientNo,
                             receiptAmt=loanAmount,userId=self.userId)

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_正常放款一百万以下的小额放款_传入贷款金额小于100万_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        loger.info("=====test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万以上的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s"%(loanId))
        print(loanId)
        loanAmount = 1200000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0].split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId,loanAmount=loanAmount,prodType=prod_type,clientNo=self.clientNo,
                                       userId=self.userId,partnerId='JZ')
            loger.info("test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount']-loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,2,5,6,4], loan_rsult
            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_03_正常放款一百万_传入贷款金额等于100万_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        loger.info("=====test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s"%(loanId))
        print(loanId)
        loanAmount = 1000000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId,loanAmount=loanAmount,prodType=prod_type,clientNo=self.clientNo,
                                       userId=self.userId,partnerId='JZ')
            loger.info("test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount']-loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'],db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,2,5,6,4], loan_rsult
            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_02_正常放款一百万以上的大额放款_传入贷款金额大于100万_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_04_放款金额校验_传入贷款金额为0_放款失败_锡车贷订单(self):
        loger.info("=====test_1_04_放款金额校验_传入贷款金额为0_放款失败_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-放款金额为0(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 0
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type, clientNo=self.clientNo,
                                       userId=self.userId,partnerId='JZ')
            loger.info("test_1_04_放款金额校验_传入贷款金额为0_放款失败_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            # assert db_result[0]['accounting_result'] == '失败:NL6203,NL6203 发放金额必须大于0！'
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [4], loan_rsult
            # if db_result[0]['loan_status'] in [2,5,6,4]:
            #     data.mock_accounts(loanid=loanId,uppStatus="00")

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_放款金额校验_传入贷款金额为0_放款失败_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_01_放款银行卡_对公放款_传入对公的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        loger.info("=====test_2_01_对公放款_传入对公的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-对公放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 60000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        public_account={"payeeAccDept":"中国工商银行股份有限公司长沙东塘支行","payeeAcctName":"湖南湘松工程机械有限责任公司",
                        "payeeAcctNo":"1901009009020132035","payeeAcctType":"PUBLIC",
                        "payeeBankCode":"102100099996","payeeCertNo":"370702199003078678","payeeCertType":"01"}

        try:
            re = data.accounts_V2_loan(loanId=loanId,partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                       payeeAccDept=public_account['payeeAccDept'],payeeAcctName=public_account['payeeAcctName'],
                      payeeAcctNo=public_account['payeeAcctNo'],payeeCertNo=public_account['payeeCertNo'],
                    payeeAcctType=public_account['payeeAcctType'],payeeCertType=public_account['payeeCertType'],
                                       payeeBankCode=public_account['payeeBankCode'])
            loger.info("test_2_01_对公放款_传入对公的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'],db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,5,6,4], loan_rsult

            loger.info("========校验对公银行卡是否正确入库===========")
            db_payAc_dict = json.loads(db_result[0]['pay_info'])
            assert db_payAc_dict['payeeAccDept'] == public_account['payeeAccDept']
            assert db_payAc_dict['payeeAcctName'] == public_account['payeeAcctName']
            assert db_payAc_dict['payeeAcctNo'] == public_account['payeeAcctNo']
            assert db_payAc_dict['payeeAcctType'] == public_account['payeeAcctType']
            assert db_payAc_dict['payeeCertNo'] == public_account['payeeCertNo']
            assert db_payAc_dict['payeeCertType'] == public_account['payeeCertType']
            assert db_payAc_dict['payeeBankCode'] == public_account['payeeBankCode']
            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_01_对公放款_传入对公的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_02_放款银行卡_对私放款_传入对私的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        loger.info("=====test_2_02_对私放款_传入对私的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-对私放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 70000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        private_account={"payeeAccDept":"江苏银行","payeeAcctName":"张媛媛","payeeAcctNo":"6228760109007829211",
                         "payeeAcctType":"DEBIT","payeeCertNo":"320923199101222729","payeeCertType":"01"}

        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                       payeeAccDept=private_account['payeeAccDept'],payeeAcctName=private_account['payeeAcctName'],
                      payeeAcctNo=private_account['payeeAcctNo'],payeeCertNo=private_account['payeeCertNo'],
                    payeeAcctType=private_account['payeeAcctType'],payeeCertType=private_account['payeeCertType'])
            loger.info("test_2_02_对私放款_传入对私的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'],db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,5,6,4], loan_rsult

            loger.info("========校验对私银行卡是否正确入库===========")
            db_payAc_dict = json.loads(db_result[0]['pay_info'])
            assert db_payAc_dict['payeeAccDept'] == private_account['payeeAccDept']
            assert db_payAc_dict['payeeAcctName'] == private_account['payeeAcctName']
            assert db_payAc_dict['payeeAcctNo'] == private_account['payeeAcctNo']
            assert db_payAc_dict['payeeAcctType'] == private_account['payeeAcctType']
            assert db_payAc_dict['payeeCertNo'] == private_account['payeeCertNo']
            assert db_payAc_dict['payeeCertType'] == private_account['payeeCertType']
            # assert db_payAc_dict['payeeAccDept'] == public_account['payeeAccDept']
            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_02_对私放款_传入对私的账户信息_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_03_放款银行卡_银行卡账号异常_传入对私的错误的账户信息_放款失败报账号异常_锡车贷订单(self):
        # pass
        loger.info("=====test_2_03_放款银行卡_银行卡账号异常_传入对私的错误的账户信息_放款失败_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-银行卡异常(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 30000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        private_account={"payeeAccDept":"平安银行","payeeAcctName":"张媛媛","payeeAcctNo":"622876010923923122",
                         "payeeAcctType":"DEBIT","payeeCertNo":"320923199101222729","payeeCertType":"01"}

        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=private_account['payeeAccDept'],
                                       payeeAcctName=private_account['payeeAcctName'],
                                       payeeAcctNo=private_account['payeeAcctNo'],
                                       payeeCertNo=private_account['payeeCertNo'],
                                       payeeAcctType=private_account['payeeAcctType'],
                                       payeeCertType=private_account['payeeCertType'])
            loger.info("test_2_03_放款银行卡_银行卡账号异常_传入对私的错误的账户信息_放款失败_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            # assert db_result[0]['loan_status'] in [7], loan_rsult
            # assert db_result[0]['upp_result'] == '账户状态异常！'

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_03_放款银行卡_银行卡账号异常_传入对私的错误的账户信息_放款失败_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_04_放款银行卡_银行卡账号异常_传入错误的对公的账户信息_放款失败报账号异常_锡车贷订单(self):
        # pass
        loger.info("=====test_2_04_放款银行卡_银行卡账号异常_传入对公的账户信息_放款失败_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-错误的对公放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 60000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        public_account={"payeeAccDept":"中国建设银行股份有限公司长沙东塘支行","payeeAcctName":"湖南湘松工程机械有限责任公司",
                        "payeeAcctNo":"19010090090288898980132035","payeeAcctType":"PUBLIC",
                        "payeeBankCode":"102103430099996","payeeCertNo":"370702199003078678","payeeCertType":"01"}

        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                       payeeAccDept=public_account['payeeAccDept'],payeeAcctName=public_account['payeeAcctName'],
                      payeeAcctNo=public_account['payeeAcctNo'],payeeCertNo=public_account['payeeCertNo'],
                    payeeAcctType=public_account['payeeAcctType'],payeeCertType=public_account['payeeCertType'],
                                       payeeBankCode=public_account['payeeBankCode'])
            loger.info("test_2_04_放款银行卡_银行卡账号异常_传入对公的账户信息_放款失败_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'],db_result[0]['upp_result'])
            # assert db_result[0]['loan_status'] in [7], loan_rsult
            # assert db_result[0]['upp_result'] == '账户状态异常！'
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_04_放款银行卡_银行卡账号异常_传入对公的账户信息_放款失败_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_05_放款银行卡_行内银行卡放款_传入锡商银行卡号_可以正常放款且数据库中数据正常落库_锡车贷订单(self):
        # pass
        loger.info("=====test_2_05_放款银行卡_行内银行卡放款_传入锡商银行卡号_可以正常放款且数据库中数据正常落库_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-行内放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print(loanId)
        loanAmount = 70000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        private_account = {"payeeAcctName":"张媛媛","payeeAcctNo":"6236435330000014233","payeeAcctType":"DEBIT",
                           "payeeAccDept":"无锡锡商银行股份有限公司",
                           "payeeCertNo":"320923199101222729","payeeCertType":"01"}

        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=private_account['payeeAccDept'],
                                       payeeAcctName=private_account['payeeAcctName'],
                                       payeeAcctNo=private_account['payeeAcctNo'],
                                       payeeCertNo=private_account['payeeCertNo'],
                                       payeeAcctType=private_account['payeeAcctType'],
                                       payeeCertType=private_account['payeeCertType'])
            loger.info("test_2_05_放款银行卡_行内银行卡放款_传入锡商银行卡号_可以正常放款且数据库中数据正常落库_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            loger.info("=====校验数据库信息落库是否正常=============")
            assert db_result[0]['user_id'] == self.userId
            assert db_result[0]['client_no'] == self.clientNo
            assert db_result[0]['loan_amount'] - loanAmount == 0
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            assert db_result[0]['loan_status'] in [2,5,6,4], loan_rsult

            loger.info("========校验对私银行卡是否正确入库===========")
            db_payAc_dict = json.loads(db_result[0]['pay_info'])
            assert db_payAc_dict['payeeAccDept'] == private_account['payeeAccDept']
            assert db_payAc_dict['payeeAcctName'] == private_account['payeeAcctName']
            assert db_payAc_dict['payeeAcctNo'] == private_account['payeeAcctNo']
            assert db_payAc_dict['payeeAcctType'] == private_account['payeeAcctType']
            assert db_payAc_dict['payeeCertNo'] == private_account['payeeCertNo']
            assert db_payAc_dict['payeeCertType'] == private_account['payeeCertType']
            # assert db_payAc_dict['payeeAccDept'] == public_account['payeeAccDept']
            if db_result[0]['loan_status'] in [2,5,6,4]:
                data.mock_accounts(loanid=loanId,uppStatus="00")
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_05_放款银行卡_行内银行卡放款_传入锡商银行卡号_可以正常放款且数据库中数据正常落库_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_3_01_核算成功放款失败状态进行重新放款_传入因对公的账户信息错误导致放款失败订单号_修改成正确的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单(self):
        pass
        loger.info("=====test_3_01_核算成功放款失败状态进行重新放款_传入因对公的账户信息错误导致放款失败订单号_修改成正确"
                   "的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-错误的对公放款重新放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号是：",loanId)
        loanAmount = 60000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        public_account_error={"payeeAccDept":"中国建设银行股份有限公司长沙东塘支行","payeeAcctName":"湖南湘松工程机械有限责任公司",
                        "payeeAcctNo":"19010090090288898980132035","payeeAcctType":"PUBLIC",
                        "payeeBankCode":"102103430099996","payeeCertNo":"370702199003078678","payeeCertType":"01"}
        public_account_correct = {"payeeAccDept":"中国工商银行股份有限公司长沙东塘支行","payeeAcctName":"湖南湘松工程机械有限责任公司",
                        "payeeAcctNo":"1901009009020132035","payeeAcctType":"PUBLIC",
                        "payeeBankCode":"102100099996","payeeCertNo":"370702199003078678","payeeCertType":"01"}
        try:
            loger.info("传入错误的银行卡信息，创建核算成功-放款失败状态的订单")
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=public_account_error['payeeAccDept'],
                                       payeeAcctName=public_account_error['payeeAcctName'],
                                       payeeAcctNo=public_account_error['payeeAcctNo'],
                                       payeeCertNo=public_account_error['payeeCertNo'],
                                       payeeAcctType=public_account_error['payeeAcctType'],
                                       payeeCertType=public_account_error['payeeCertType'],
                                       payeeBankCode=public_account_error['payeeBankCode'])
            loger.info("test_3_01_核算成功放款失败状态进行重新放款_传入因对公的账户信息错误导致放款失败订单号_修改成正确"
                       "的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print("放款失败的数据库信息：",db_result)
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            # assert db_result[0]['loan_status'] in [7], loan_rsult
            if db_result[0]['loan_status'] == 7:
                print("============开始进行重新放款===================")
                loger.info("============开始进行重新放款===================")
                reloan = data.accounts_V2_loan(loanId=loanId,partnerId='JZ', loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=public_account_correct['payeeAccDept'],
                                       payeeAcctName=public_account_correct['payeeAcctName'],
                                       payeeAcctNo=public_account_correct['payeeAcctNo'],
                                       payeeCertNo=public_account_correct['payeeCertNo'],
                                       payeeAcctType=public_account_correct['payeeAcctType'],
                                       payeeCertType=public_account_correct['payeeCertType'],
                                       payeeBankCode=public_account_correct['payeeBankCode'])
                assert reloan.status_code == 200

                resloan = reloan.json()
                print(resloan)
                assert resloan['code'] == 0
                assert resloan['success'] == True
                assert resloan['result'] == True
                sleep(5)
    #         #     loanId = 'LHD20171203000007'
    #         #     db_result = [{'id':1245}]
                loger.info("重新放款成功后，校验数据库中的银行卡信息是否更正过来，放款状态是否正常")
                db_result_reloan = rep.commonParam.assect_accounts_loan(loanId)
                print("重新放款的数据库信息：{}".format(db_result_reloan))
                loger.info("重新放款的数据库信息：{}".format(db_result_reloan))
                for dbre in db_result_reloan:
                    # print(dbre)
                    if dbre['id'] != db_result[0]['id']:
                        print(dbre)
                        reloan_rsult = '放款错误原因：{},{}'.format(dbre['accounting_result'],
                                                           dbre['upp_result'])
                        assert dbre['loan_status'] in [5,6,4],reloan_rsult
                        db_payAc_dict = json.loads(dbre['pay_info'])
                        print("开始验证银行卡信息")
                        assert db_payAc_dict['payeeAccDept'] == public_account_correct['payeeAccDept']
                        assert db_payAc_dict['payeeAcctName'] == public_account_correct['payeeAcctName']
                        assert db_payAc_dict['payeeAcctNo'] == public_account_correct['payeeAcctNo']
                        assert db_payAc_dict['payeeAcctType'] == public_account_correct['payeeAcctType']
                        assert db_payAc_dict['payeeCertNo'] == public_account_correct['payeeCertNo']
                        assert db_payAc_dict['payeeCertType'] == public_account_correct['payeeCertType']
                        assert db_payAc_dict['payeeBankCode'] == public_account_correct['payeeBankCode']
                        if dbre['loan_status'] in [2, 5, 6]:
                           data.mock_accounts(loanid=loanId, uppStatus="00")
                           data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_01_核算成功放款失败状态进行重新放款_传入因对公的账户信息错误导致放款失败订"
                        "单号_修改成正确的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_长安新"
                        "生的订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_3_02_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败订单号_修改成正确的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单(self):
        pass
        loger.info("=====test_3_02_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败订单号_修改成正确的"
                   "银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-错误的对私放款重新放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号是：",loanId)
        loanAmount = 30000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        private_account_error={"payeeAccDept":"建设银行银行","payeeAcctName":"张正杰","payeeAcctNo":"622185655685200197319710",
                               "payeeAcctType":"DEBIT","payeeBankCode":"","payeeCertNo":"320830199708192413","payeeCertType":"01"}

        private_account_correct = {"payeeAccDept":"邮政储蓄银行","payeeAcctName":"张正杰","payeeAcctNo":"6221885200197319710",
                                   "payeeAcctType":"DEBIT","payeeBankCode":"","payeeCertNo":"320830199708192413","payeeCertType":"01"}
        try:
            loger.info("传入错误的银行卡信息，创建核算成功-放款失败状态的订单")
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=private_account_error['payeeAccDept'],
                                       payeeAcctName=private_account_error['payeeAcctName'],
                                       payeeAcctNo=private_account_error['payeeAcctNo'],
                                       payeeCertNo=private_account_error['payeeCertNo'],
                                       payeeAcctType=private_account_error['payeeAcctType'],
                                       payeeCertType=private_account_error['payeeCertType'])
            loger.info("test_3_02_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败订单号_修改成正确的"
                       "银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print("放款失败的数据库信息：",db_result)
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            # assert db_result[0]['loan_status'] in [7], loan_rsult
            if db_result[0]['loan_status'] == 7:
                print("============开始进行重新放款===================")
                loger.info("============开始进行重新放款===================")
                reloan = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=private_account_correct['payeeAccDept'],
                                       payeeAcctName=private_account_correct['payeeAcctName'],
                                       payeeAcctNo=private_account_correct['payeeAcctNo'],
                                       payeeCertNo=private_account_correct['payeeCertNo'],
                                       payeeAcctType=private_account_correct['payeeAcctType'],
                                       payeeCertType=private_account_correct['payeeCertType'])
                assert reloan.status_code == 200

                resloan = reloan.json()
                print(resloan)
                assert resloan['code'] == 0
                assert resloan['success'] == True
                assert resloan['result'] == True
                sleep(5)
            #     loanId = 'LHD20171203000007'
            #     db_result = [{'id':1245}]
                loger.info("重新放款成功后，校验数据库中的银行卡信息是否更正过来，放款状态是否正常")
                db_result_reloan = rep.commonParam.assect_accounts_loan(loanId)
                print("重新放款的数据库信息：{}".format(db_result_reloan))
                loger.info("重新放款的数据库信息：{}".format(db_result_reloan))
                for dbre in db_result_reloan:
                    # print(dbre)
                    if dbre['id'] != db_result[0]['id']:
                        print(dbre)
                        reloan_rsult = '放款错误原因：{},{}'.format(dbre['accounting_result'],
                                                           dbre['upp_result'])
                        assert dbre['loan_status'] in [5,6,4],reloan_rsult
                        db_payAc_dict = json.loads(dbre['pay_info'])
                        print("开始验证银行卡信息")
                        assert db_payAc_dict['payeeAccDept'] == private_account_correct['payeeAccDept']
                        assert db_payAc_dict['payeeAcctName'] == private_account_correct['payeeAcctName']
                        assert db_payAc_dict['payeeAcctNo'] == private_account_correct['payeeAcctNo']
                        assert db_payAc_dict['payeeAcctType'] == private_account_correct['payeeAcctType']
                        assert db_payAc_dict['payeeCertNo'] == private_account_correct['payeeCertNo']
                        assert db_payAc_dict['payeeCertType'] == private_account_correct['payeeCertType']
                        print("银行卡验证完成，一切正常")
                        if dbre['loan_status'] in [2, 5, 6]:
                           data.mock_accounts(loanid=loanId, uppStatus="00")
                           data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                            receiptAmt=loanAmount, userId=self.userId)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_02_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败订单号_修改成正确"
                        "的银行卡信息进行重新放款_重新放款成功且数据库银行卡信息修改正确_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_3_03_核算成功放款失败状态进行重新放款_传入的账户信息错误导致放款失败订单号_依旧修改为错误的银行卡信息进行重新放款_重新放款失败_锡车贷订单(self):
        # pass
        loger.info("=====test_3_03_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败订单号_依旧修改为"
                   "错误的银行卡信息进行重新放款_重新放款失_锡车贷订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='对私重新放款失败(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号是：", loanId)
        loanAmount = 30000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        private_account_error = {"payeeAccDept": "建设银行银行", "payeeAcctName": "张正杰",
                                 "payeeAcctNo": "622185655685200197319710",
                                 "payeeAcctType": "DEBIT", "payeeBankCode": "", "payeeCertNo": "320830199708192413",
                                 "payeeCertType": "01"}

        private_account_error2 = {"payeeAccDept": "平安银行", "payeeAcctName": "张正杰",
                                   "payeeAcctNo": "6221885200197367676719710",
                                   "payeeAcctType": "DEBIT", "payeeBankCode": "", "payeeCertNo": "320830199708192413",
                                   "payeeCertType": "01"}

        private_account_correct = {"payeeAccDept": "邮政储蓄银行", "payeeAcctName": "张正杰",
                                   "payeeAcctNo": "6221885200197319710",
                                   "payeeAcctType": "DEBIT", "payeeBankCode": "", "payeeCertNo": "320830199708192413",
                                   "payeeCertType": "01"}
        try:
            loger.info("传入错误的银行卡信息，创建核算成功-放款失败状态的订单")
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                       payeeAccDept=private_account_error['payeeAccDept'],
                                       payeeAcctName=private_account_error['payeeAcctName'],
                                       payeeAcctNo=private_account_error['payeeAcctNo'],
                                       payeeCertNo=private_account_error['payeeCertNo'],
                                       payeeAcctType=private_account_error['payeeAcctType'],
                                       payeeCertType=private_account_error['payeeCertType'])
            loger.info("test_3_03_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失"
                       "败订单号_依旧修改为错误的银行卡信息进行重新放款_重新放款失_锡车贷订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] == True
            sleep(5)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print("放款失败的数据库信息：", db_result)
            loan_rsult = '放款错误原因：{},{}'.format(db_result[0]['accounting_result'], db_result[0]['upp_result'])
            # assert db_result[0]['loan_status'] in [7], loan_rsult
            if db_result[0]['loan_status'] == 7:
                print("============开始进行重新放款===================")
                loger.info("============开始进行重新放款===================")
                reloan = data.accounts_V2_loan(loanId=loanId,partnerId='JZ', loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,userId=self.userId,
                                           payeeAccDept=private_account_error2['payeeAccDept'],
                                           payeeAcctName=private_account_error2['payeeAcctName'],
                                           payeeAcctNo=private_account_error2['payeeAcctNo'],
                                           payeeCertNo=private_account_error2['payeeCertNo'],
                                           payeeAcctType=private_account_error2['payeeAcctType'],
                                           payeeCertType=private_account_error2['payeeCertType'])
                assert reloan.status_code == 200
                resloan = reloan.json()
                print(resloan)
                assert resloan['code'] == 0
                assert resloan['success'] == True
                assert resloan['result'] == True
                sleep(5)
                loger.info("重新放款成功后，校验数据库中的银行卡信息是否更正过来，放款状态是否正常")
                db_result_reloan = rep.commonParam.assect_accounts_loan(loanId)
                print("重新放款的数据库信息：{}".format(db_result_reloan))
                loger.info("重新放款的数据库信息：{}".format(db_result_reloan))
                for dbre in db_result_reloan:
                # print(dbre)
                  if dbre['id'] != db_result[0]['id']:
                    print(dbre)
                    reloan_rsult = '放款错误原因：{},{}'.format(dbre['accounting_result'],
                                                         dbre['upp_result'])
                    assert dbre['loan_status']  in [7], reloan_rsult  #放款依旧失败



        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_03_核算成功放款失败状态进行重新放款_传入因对私的账户信息错误导致放款失败"
                        "订单号_依旧修改为错误的银行卡信息进行重新放款_重新放款失_锡车贷订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    # def test_4_01_还款方式不同的放款_还款方式为_1_等额本息_放款成功_金泽订单(self):
    #     # pass
    #     loger.info("=====test_4_01_还款方式不同的放款_还款方式为_1_等额本息_放款成功_金泽订单=======接口测试开始")
    #     loger.info("创建订单")
    #     loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-还款方式为1的放款(/v2/loan)')  # 创建订单
    #     loger.info("创建的订单号是：%s" % (loanId))
    #     print("创建的订单号是：", loanId)
    #     loanAmount = 30000
    #     prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
    #     repayMode = "1"
    #     try:
    #         re = data.accounts_V2_loan(loanId=loanId,partnerId='JZ', loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,
    #                                    userId=self.userId,repayMode=repayMode)
    #         loger.info("test_4_01_还款方式不同的放款_还款方式为_1_等额本息_放款成功_金泽订单======返回报文：%s" % (re.text))
    #         assert re.status_code == 200
    #         res = re.json()
    #         print(res)
    #         assert res['code'] == 0
    #         assert res['success'] == True
    #         assert res['result'] == True
    #         db_result = rep.commonParam.assect_accounts_loan(loanId)
    #         if db_result[0]['loan_status'] in [2,5,6,4]:
    #             data.mock_accounts(loanid=loanId,uppStatus="00")
    #             data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
    #                                         receiptAmt=loanAmount, userId=self.userId)
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_4_01_还款方式不同的放款_还款方式为_1_等额本息_放款成功_金泽订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    # def test_4_02_还款方式不同的放款_还款方式为_2_等额本金_放款成功_金泽订单(self):
    #     # pass
    #     loger.info("=====test_4_02_还款方式不同的放款_还款方式为_2_等额本金_放款成功_金泽订单=======接口测试开始")
    #     loger.info("创建订单")
    #     loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-还款方式为2的放款(/v2/loan)')  # 创建订单
    #     loger.info("创建的订单号是：%s" % (loanId))
    #     print("创建的订单号是：", loanId)
    #     loanAmount = 20000
    #     prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
    #     repayMode = "2"
    #     try:
    #         re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type,clientNo=self.clientNo,
    #                                    userId=self.userId,repayMode=repayMode)
    #         loger.info("test_4_02_还款方式不同的放款_还款方式为_2_等额本金_放款成功_金泽订单======返回报文：%s" % (re.text))
    #         assert re.status_code == 200
    #         res = re.json()
    #         print(res)
    #         assert res['code'] == 0
    #         assert res['success'] == True
    #         assert res['result'] == True
    #         db_result = rep.commonParam.assect_accounts_loan(loanId)
    #         if db_result[0]['loan_status'] in [2, 5, 6]:
    #             data.mock_accounts(loanid=loanId, uppStatus="00")
    #     except (ZeroDivisionError, TypeError, NameError) as e:
    #         loger.error("test_4_02_还款方式不同的放款_还款方式为_2_等额本金_放款成功_金泽订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_4_01_接口必填参数校验_传入空订单号_接口调用失败_借据号不能为空(self):
        loger.info("=====test_5_01_接口必填参数校验_传入空订单号_接口调用失败_借据号不能为空_金泽订单=======接口测试开始")
        # loger.info("创建订单")
        # loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        # loger.info("创建的订单号是：%s" % (loanId))
        # print("创建的订单号：", loanId)
        loanId = ''
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type, clientNo=self.clientNo,
                                       userId=self.userId)
            loger.info("test_5_01_接口必填参数校验_传入空订单号_接口调用失败_借据号不能为空_金泽订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] != 0
            assert res['success'] == False
            assert res['message'] == "body.loanId:借据号不能为空"

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_正常放款一百万以下的小额放款_传入贷款金额小于100万_可以正常放款且数据库中数据正常落库_金泽订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_4_02_接口必填参数校验_传入空userId_接口调用失败_用户id不能为空(self):
        loger.info("=====test_5_02_接口必填参数校验_传入空userId_接口调用失败_用户id不能为空_金泽订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        # loanId = ''
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type, clientNo=self.clientNo,
                                       userId='')
            loger.info("test_5_02_接口必填参数校验_传入空userId_接口调用失败_用户id不能为空_金泽订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] != 0
            assert res['success'] == False
            assert res['message'] == "body.userId:互金用户ID不能为空"

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_02_接口必填参数校验_传入空userId_接口调用失败_用户id不能为空_金泽订单====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_4_03_接口必填参数校验_传入空clientNo_接口调用失败_clientNo不能为空(self):
        loger.info("=====test_5_03_接口必填参数校验_传入空clientNo_接口调用失败_clientNo不能为空_金泽订单=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=109, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        # loanId = ''
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        try:
            re = data.accounts_V2_loan(loanId=loanId, partnerId='JZ',loanAmount=loanAmount, prodType=prod_type, clientNo='',
                                       userId=self.userId)
            loger.info("test_5_03_接口必填参数校验_传入空clientNo_接口调用失败_clientNo不能为空_金泽订单======返回报文：%s" % (re.text))
            assert re.status_code == 200
            res = re.json()
            print(res)
            assert res['code'] != 0
            assert res['success'] == False
            assert res['message'] == "body.clientNo:客户号不能为空"

        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_5_03_接口必填参数校验_传入空clientNo_接口调用失败_clientNo不能为空_金泽订单====断言失败，失败原因：%s" % (e))