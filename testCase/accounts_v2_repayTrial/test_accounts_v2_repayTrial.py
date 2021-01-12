# -*- coding: utf-8 -*-
# @Time    : 2020/12/8
# @Author  :竹玉红
# @Fuction :账务中心-新-还款试算接口
from time import sleep

import pytest

from InterfaceData.Interface_Data import Interface_Data
from common.dataVariable import Respont

rep = Respont()
loger = rep.Mylog
data = Interface_Data()
class Test_V2_repayTrial:
    def setup_class(self):
        self.userId = '010000003211'  # 客户userId
        self.clientNo = rep.commonParam.accounts(self.userId)[0]['client_no']  # 客户号

    def teardown_class(self):
        rep.Mylog.info("========测试结束,清除数据========= ")
        print("========测试结束========= ")

    # @pytest.mark.skip(reason="数据原因")
    def test_1_01_不同渠道产品的还款试算_传入放款成功的长安新生的订单号_接口正常出现试算结果(self):
        loger.info("=====test_1_01_不同渠道产品的还款试算_传入放款成功的长安新生的订单号_接口正常出现试算结果=======接口测试开始")
        # loanId = 'LHD20171203000020'
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow_caxs(count=2, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='长安新生').split(',')[0]
        print(prod_type)
        try:
            req = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type, clientNo=self.clientNo,
                                       userId=self.userId)
            print(req.json())
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus="00")
            mysql = rep.commonParam.assect_accounts_loan(loanId)[0]
            if mysql['loan_status'] == 6:
                re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
                assert re.status_code == 200
                res = re.json()
                # print(res)
                assert res['code'] == 0
                assert res['success'] == True
                assert res['result'] != None
                result = res['result']
                duePrincipal = result['duePrincipal']  # 应还本金
                dueInterest = result['dueInterest']  # 应还利息
                duePenalty = result['duePenalty']  # 应还罚金
                totalAmount = result['totalAmount']  # 还款总额
                dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
                if result['feeDetails'] != []:
                    feeAmt = result['feeDetails']['feeDetails']
                else:
                    feeAmt = 0
                assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
            # if mysql['loan_status'] == 6:

            # res_plan = data.plan_list(loanId).json()
            # print(res_plan)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_不同渠道产品的还款试算_传入放款成功的长安新生的订单号_接口正常出现试算结果====断言失败，失败原因：%s" % (e))
    #
    # # @pytest.mark.skip(reason="数据原因")
    def test_1_02_不同渠道产品的还款试算_传入放款成功的平安普惠的订单号_接口正常出现试算结果(self):
        # pass
        loger.info("=====test_1_02_不同渠道产品的还款试算_传入放款成功的平安普惠的订单号_接口正常出现试算结果=======接口测试开始")
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=2, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='平安普惠').split(',')[0]
        print(prod_type)
        try:
            req = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type,
                                        clientNo=self.clientNo,
                                        userId=self.userId)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus="00")
            mysql = rep.commonParam.assect_accounts_loan(loanId)[0]
            if mysql['loan_status'] == 6:
                re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
                assert re.status_code == 200
                res = re.json()
                # print(res)
                assert res['code'] == 0
                assert res['success'] == True
                assert res['result'] != None
                result = res['result']
                duePrincipal = result['duePrincipal']  # 应还本金
                dueInterest = result['dueInterest']  # 应还利息
                duePenalty = result['duePenalty']  # 应还罚金
                totalAmount = result['totalAmount']  # 还款总额
                dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
                if result['feeDetails'] != []:
                    feeAmt = result['feeDetails']['feeDetails']
                else:
                    feeAmt = 0
                assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
                data.accounts_repay_new(loanId=loanId, receiptType=2, clientNo=self.clientNo,
                                        receiptAmt=loanAmount, userId=self.userId)
            # res_plan = data.plan_list(loanId).json()
            # print(res_plan)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_不同渠道产品的还款试算_传入放款成功的长安新生的订单号_接口正常出现试算结果====断言失败，失败原因：%s" % (e))


    # @pytest.mark.skip(reason="数据原因")
    def test_1_03_不同渠道产品的还款试算_传入放款成功的机贷的订单号_接口正常出现试算结果(self):
        loger.info("创建订单")
        loanId = rep.commonParam.set_flow(count=2, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='锡机贷')
        print(prod_type)
        try:
            req = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type,
                                        clientNo=self.clientNo,
                                        userId=self.userId)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [5,4]:
                data.mock_accounts(loanid=loanId, uppStatus="00")
            mysql = rep.commonParam.assect_accounts_loan(loanId)[0]
            if mysql['loan_status'] == 6:
                re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
                assert re.status_code == 200
                res = re.json()
                # print(res)
                assert res['code'] == 0
                assert res['success'] == True
                assert res['result'] != None
                result = res['result']
                duePrincipal = result['duePrincipal']  # 应还本金
                dueInterest = result['dueInterest']  # 应还利息
                duePenalty = result['duePenalty']  # 应还罚金
                totalAmount = result['totalAmount']  # 还款总额
                dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
                if result['feeDetails'] != []:
                    feeAmt = result['feeDetails']['feeDetails']
                else:
                    feeAmt = 0
                assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
            # res_plan = data.plan_list(loanId).json()
            # print(res_plan)
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_01_不同渠道产品的还款试算_传入放款成功的长安新生的订单号_接口正常出现试算结果====断言失败，失败原因：%s" % (e))


    # @pytest.mark.skip(reason="数据原因")
    def test_1_04_不同渠道产品的还款试算_传入放款成功的车贷的订单号_接口正常出现试算结果(self):
        loger.info("=====test_1_04_不同渠道产品的还款试算_传入放款成功的车贷的订单号_接口正常出现试算结果=======接口测试开始")
        loanId = rep.commonParam.set_flow(count=2, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='金泽').split(',')[0]
        print(prod_type)
        try:
            req = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type,
                                        clientNo=self.clientNo,
                                        userId=self.userId)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [2, 5, 6]:
                data.mock_accounts(loanid=loanId, uppStatus="00")
            mysql = rep.commonParam.assect_accounts_loan(loanId)[0]
            if mysql['loan_status'] == 6:
                re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
                assert re.status_code == 200
                res = re.json()
                # print(res)
                assert res['code'] == 0
                assert res['success'] == True
                assert res['result'] != None
                result = res['result']
                duePrincipal = result['duePrincipal']  # 应还本金
                dueInterest = result['dueInterest']  # 应还利息
                duePenalty = result['duePenalty']  # 应还罚金
                totalAmount = result['totalAmount']  # 还款总额
                dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
                if result['feeDetails'] != []:
                    feeAmt = result['feeDetails']['feeDetails']
                else:
                    feeAmt = 0
                assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_04_不同渠道产品的还款试算_传入放款成功的车贷的订单号_接口正常出现试算结果====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_05_不同渠道产品的还款试算_传入放款成功的房贷的订单号_接口正常出现试算结果(self):
        loanId = rep.commonParam.set_flow(count=2, describe='测试账单中心新接口放款接口-正常放款一百万以下的小额放款(/v2/loan)')  # 创建订单
        loger.info("创建的订单号是：%s" % (loanId))
        print("创建的订单号：", loanId)
        loanAmount = 700000
        prod_type = rep.commonParam.prod_type(prod_type_desc='安居客').split(',')[0]
        print(prod_type)
        try:
            req = data.accounts_V2_loan(loanId=loanId, loanAmount=loanAmount, prodType=prod_type,
                                        clientNo=self.clientNo,
                                        userId=self.userId)
            sleep(2)
            db_result = rep.commonParam.assect_accounts_loan(loanId)
            print(db_result)
            if db_result[0]['loan_status'] in [2, 5, 6]:
                data.mock_accounts(loanid=loanId, uppStatus="00")
            mysql = rep.commonParam.assect_accounts_loan(loanId)[0]
            if mysql['loan_status'] == 6:
                re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
                assert re.status_code == 200
                res = re.json()
                # print(res)
                assert res['code'] == 0
                assert res['success'] == True
                assert res['result'] != None
                result = res['result']
                duePrincipal = result['duePrincipal']  # 应还本金
                dueInterest = result['dueInterest']  # 应还利息
                duePenalty = result['duePenalty']  # 应还罚金
                totalAmount = result['totalAmount']  # 还款总额
                dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
                if result['feeDetails'] != []:
                    feeAmt = result['feeDetails']['feeDetails']
                else:
                    feeAmt = 0
                assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_05_不同渠道产品的还款试算_传入放款成功的房贷的订单号_接口正常出现试算结果====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_1_06_不同渠道产品的还款试算_传入未放款成功的订单_无法进行还款试算(self):
        # pass
        loger.info("=====test_1_06_不同渠道产品的还款试算_传入未放款成功的订单_无法进行还款试算=======接口测试开始")
        loanId = '20171204000008' #订单status不为6
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            # assert res['result'] != None
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_1_06_不同渠道产品的还款试算_传入未放款成功的订单_无法进行还款试算====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_01_不同的还款日期进行还款试算_传入放款成功的早于系统还款日期的长安新生的订单_无法进行放款报试算日期不能早于系统当前日期(self):
        # pass
        loger.info("=====test_2_01_不同的还款日期进行还款试算_传入放款成功的早于系统还款日期的长安新生的订单_无法进行放款报试算日期不能早于系统当前日期=======接口测试开始")
        loanId = 'LHD20171203000020'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate='20290823')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            # assert res['message'] == "失败:NL9271,NL9271 试算日期不能早于系统当前日期"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_01_不同的还款日期进行还款试算_传入放款成功的早于系统还款日期的长安新生的订单_无法进行放款报试算日期不能早于系统当前日期====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_02_不同的还款日期进行还款试算_传入放款成功的等于系统还款日期的长安新生的订单_可以正常放款(self):
        # pass
        loger.info("=====test_2_02_不同的还款日期进行还款试算_传入放款成功的等于系统还款日期的长安新生的订单_可以正常放款=======接口测试开始")
        loanId = 'LHD20171203000020'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=data.accounts_hxDate_async().json()['result']['hxDate'])
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] != None
            result = res['result']
            duePrincipal = result['duePrincipal']  # 应还本金
            dueInterest = result['dueInterest']  # 应还利息
            duePenalty = result['duePenalty']  # 应还罚金
            totalAmount = result['totalAmount']  # 还款总额
            dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
            if result['feeDetails'] != []:
                feeAmt = result['feeDetails']['feeDetails']
            else:
                feeAmt = 0
            assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_02_不同的还款日期进行还款试算_传入放款成功的等于系统还款日期的长安新生的订单_可以正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_03_不同的还款日期进行还款试算_传入放款成功的晚于系统还款日期的长安新生的订单_可以正常放款(self):
        # pass
        loger.info("=====test_2_03_不同的还款日期进行还款试算_传入放款成功的晚于系统还款日期的长安新生的订单_可以正常放款=======接口测试开始")
        loanId = 'LHD20171203000020'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate=rep.commonParam.dealHxdate())
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] != None
            result = res['result']
            duePrincipal = result['duePrincipal']  # 应还本金
            dueInterest = result['dueInterest']  # 应还利息
            duePenalty = result['duePenalty']  # 应还罚金
            totalAmount = result['totalAmount']  # 还款总额
            dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
            if result['feeDetails'] != []:
                feeAmt = result['feeDetails']['feeDetails']
            else:
                feeAmt = 0
            assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_03_不同的还款日期进行还款试算_传入放款成功的晚于系统还款日期的长安新生的订单_可以正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_2_04_不同的还款日期进行还款试算_其他渠道的订单不受时间限制_传入放款成功的房贷订单随意传入放款成功的日期_可以正常放款(self):
        # pass
        loger.info("=====test_2_04_不同的还款日期进行还款试算_其他渠道的订单不受时间限制_传入放款成功的房贷订单随意传入放款成功的日期_可以正常放款=======接口测试开始")
        loanId = '20171203000022'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate='20290329')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == 0
            assert res['success'] == True
            assert res['result'] != None
            result = res['result']
            duePrincipal = result['duePrincipal']  # 应还本金
            dueInterest = result['dueInterest']  # 应还利息
            duePenalty = result['duePenalty']  # 应还罚金
            totalAmount = result['totalAmount']  # 还款总额
            dueGuaranteeFee = result['dueGuaranteeFee']  # 应还保证金费用
            if result['feeDetails'] != []:
                feeAmt = result['feeDetails']['feeDetails']
            else:
                feeAmt = 0
            assert totalAmount == dueInterest + duePenalty + duePrincipal + dueGuaranteeFee + feeAmt
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_04_不同的还款日期进行还款试算_其他渠道的订单不受时间限制_传入放款成功的房贷订单随意传入放款成功的日期_可以正常放款=======接口测试开始")

    # @pytest.mark.skip(reason="数据原因")
    def test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款(self):
        # pass
        loger.info("=====test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款=======接口测试开始")
        loanId = 'LHD20171203000020'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate='200829')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            assert res['message'] == "失败:NL9271,NL9271 试算日期不能早于系统当前日期"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_2_05_不同的还款日期进行还款试算_传入放款成功的错误日期的长安新生的订单_无法正常放款====断言失败，失败原因：%s" % (e))

    # @pytest.mark.skip(reason="数据原因")
    def test_3_01_案件已结清的订单的还款试算_传入还款成功的已结清的订单号_无法进行还款试算(self):
        # pass
        loger.info("=====test_3_01_案件已结清的订单的还款试算_传入还款成功的已结清的订单号_无法进行还款试算=======接口测试开始")
        loanId = '20171204000009'
        try:
            re = data.accounts_V2_repayTrial(loanId=loanId, receiptDate='200829')
            assert re.status_code == 200
            res = re.json()
            # print(res)
            assert res['code'] == None
            assert res['success'] == False
            # assert res['message'] == "失败:NL9271,NL9271 试算日期不能早于系统当前日期"
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("test_3_01_案件已结清的订单的还款试算_传入还款成功的已结清的订单号_无法进行还款试算====断言失败，失败原因：%s" % (e))

if __name__ =="__main__":
    hxDate = data.accounts_hxDate_async().json()['result']['hxDate']
    print(hxDate)
    year = int(hxDate[0:4])
    month = int(hxDate[4:6])
    day = int(hxDate[6:8])
    print(year,month+1,day+1)