# -*- coding: utf-8 -*-
# @Time    : 2020/11/09
# @Author  : 张正杰
# @Fuction : 创建订单保存内容相关接口
import json

import requests

from createOrder.createOrder_car import CreatOrder_car
from createOrder.creatOrder_machine import CreatOrder_machine
from common.getAPIResponse import API_Reponse
from common.getEnv import environment
from common.login import Login
from common.Log import MyLog
import requests

import requests
from InterfaceData.url_summary import url_variable

Env = environment()
host = Env.Host  # 获取前置url
loger = MyLog
port = '/order/createOrder'

repuest = API_Reponse()
db_jst = Env.db_jts
urlVa = url_variable()


class Interface_Data():

    # 账务中心放款/重新放款接口
    def v2_loan(self):
        """
        /accounts/v2/loan
        账务中心放款/重新放款接口
        :return:
        """
        url, header = urlVa.url_v2_loan
        data = {
            "appHead": {
                "currentNum": "48",
                "pageEnd": "Excepteur do laboris sint",
                "pageStart": "incididunt nisi amet in",
                "pgupOrPgdn": "culpa",
                "totalFlag": "quis",
                "totalNum": "54",
                "totalPages": "aliquip ipsum Ut in",
                "totalRows": "tempor Ut aliqua dolore magna"
            },
            "body": {
                "clientNo": "consequat Duis laboris ut",
                "interestRate": 43,
                "loanAmount": 20,
                "loanId": "84",
                "operator": "Duis",
                "payeeAccount": {
                    "payeeAcctName": "明收也今了",
                    "payeeAcctNo": "ea labore dolore minim",
                    "payeeAcctType": "mollit non Duis quis",
                    "payeeCertNo": "eiusmod amet minim et",
                    "payeeCertType": "qui id dolor velit nostrud",
                    "payeeAccDept": "enim amet ullamco",
                    "payeeBankCode": "43",
                    "payeeBankName": "并明大文路",
                    "payeeCityName": "图型样养还水到",
                    "payeePhone": "18147824987",
                    "payeeProName": "被放整明持连结"
                },
                "prodType": "eu officia",
                "repayMode": "irure voluptate dolor minim",
                "term": "tempor elit",
                "termType": "dolor adipisicing do minim ipsum",
                "userId": "80",
                "analysis2": "reprehenderit labore aute sed Ut",
                "contributionAccount": {
                    "accountName": "知地义物声没合",
                    "accountNo": "reprehenderit adipisicing magna"
                },
                "customerInterestRate": 65,
                "interestDay": "aute",
                "penaltyRate": 87,
                "uiMinAmt": "sunt mollit in"
            },
            "sysHead": {
                "authFlag": "et occaecat",
                "branchId": "13",
                "bussSeqNo": "Lorem qui",
                "company": "ad",
                "destBranchNo": "sit consectetur",
                "logId": "73",
                "messageCode": "12",
                "messageType": "nostrud ex laborum",
                "moduleId": "76",
                "partnerId": "15",
                "platformId": "11",
                "platformUserId": "25",
                "reference": "et minim consectetur",
                "ret": [
                    {
                        "retCode": "30",
                        "retMsg": "eiusmod Lorem"
                    },
                    {
                        "retCode": "37",
                        "retMsg": "elit ipsum"
                    }
                ],
                "retStatus": "sed ipsum",
                "runDate": "2007-11-17",
                "seqNo": "sunt nulla dolor tempor",
                "serviceCode": "76",
                "sourceBranchNo": "qui consequat",
                "sourceType": "incididunt dolore dolor id",
                "systemId": "78",
                "tranDate": "2009-05-16",
                "tranMode": "mollit occaecat do magna pariatur",
                "tranTimestamp": "1978-03-20 06:48:30",
                "userId": "62",
                "userLang": "anim",
                "wsId": "71"
            }
        }
        try:
            loger.info("===========放款/重新放款接口==========接口运行开始")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("=========放款/重新放款接口返回报文：%s============" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("放款/重新放款接口运行失败，失败原因：%s" % (e))

    # 账务还款接口
    def v2_repay(self):
        url, header = urlVa.url_v2_repay
        data = {
            "appHead": {
                "currentNum": "2",
                "pageEnd": "esse mollit",
                "pageStart": "in",
                "pgupOrPgdn": "id proident amet",
                "totalFlag": "cillum labore",
                "totalNum": "46",
                "totalPages": "fugiat incididunt",
                "totalRows": "id est amet"
            },
            "body": {
                "clientNo": "dolor non id voluptate",
                "loanId": "62",
                "operator": "ullamco adipisicing do",
                "receiptType": "anim labore",
                "repayAcctInfo": {
                    "payerAcctName": "快没志将效",
                    "payerAcctNo": "dolore in do dolor sunt",
                    "payerAcctType": "Excepteur nostrud",
                    "payerCertNo": "eu nostrud sed consequat",
                    "payerCertType": "in",
                    "payerPhone": "18150704803"
                },
                "repayType": -47112773,
                "reqSeqNo": "ex dolore",
                "userId": "13",
                "feeInfoArray": [
                    {
                        "discountAmt": 58,
                        "discountType": "20",
                        "feeCcy": "enim nostrud",
                        "feeInfoAmt": 74,
                        "feeInfoAmtRec": 86,
                        "feeType": "aliquip ut"
                    },
                    {
                        "discountAmt": 99,
                        "discountType": "28",
                        "feeCcy": "aute nulla proident in",
                        "feeInfoAmt": 8,
                        "feeInfoAmtRec": 25,
                        "feeType": "Duis irure magna"
                    },
                    {
                        "discountAmt": 2,
                        "discountType": "30",
                        "feeCcy": "ex",
                        "feeInfoAmt": 73,
                        "feeInfoAmtRec": 26,
                        "feeType": "elit ad ut"
                    },
                    {
                        "discountAmt": 93,
                        "discountType": "36",
                        "feeCcy": "laboris minim amet ullamco",
                        "feeInfoAmt": 32,
                        "feeInfoAmtRec": 85,
                        "feeType": "aute Lorem amet"
                    },
                    {
                        "discountAmt": 21,
                        "discountType": "24",
                        "feeCcy": "sed quis fugiat",
                        "feeInfoAmt": 75,
                        "feeInfoAmtRec": 33,
                        "feeType": "consectetur eu aute ex labore"
                    }
                ],
                "optionCtl": "laborum velit dolore nostrud pariatur",
                "prepaymentCollectionPenalty": 80,
                "prepaymentCollectionPenaltyPayType": -69626675,
                "prepaymentPenalty": 21,
                "prepaymentPenaltyPayType": 72003503,
                "receiptAmt": 19,
                "urgentFlag": "enim amet ullamco Duis"
            },
            "sysHead": {
                "authFlag": "nostrud magna occaecat in ullamco",
                "branchId": "15",
                "bussSeqNo": "aliqua ut culpa do",
                "company": "ut culpa deserunt non ea",
                "destBranchNo": "aliqua consequat non",
                "logId": "38",
                "messageCode": "98",
                "messageType": "pariatur",
                "moduleId": "82",
                "partnerId": "30",
                "platformId": "93",
                "platformUserId": "81",
                "reference": "quis enim dolor sit",
                "ret": [
                    {
                        "retCode": "3",
                        "retMsg": "magna in velit culpa"
                    },
                    {
                        "retCode": "76",
                        "retMsg": "occaecat"
                    },
                    {
                        "retCode": "34",
                        "retMsg": "veniam ad"
                    }
                ],
                "retStatus": "aliquip laborum incididunt",
                "runDate": "2007-09-26",
                "seqNo": "Duis veniam",
                "serviceCode": "70",
                "sourceBranchNo": "minim sed dolor non do",
                "sourceType": "velit mollit eu enim tempor",
                "systemId": "89",
                "tranDate": "1989-03-18",
                "tranMode": "in esse adipisicing nisi id",
                "tranTimestamp": "1987-08-20 08:51:33",
                "userId": "24",
                "userLang": "id esse sit adipisicing",
                "wsId": "68"
            }
        }
        try:
            loger.info("===========账务-还款接口运行开始=================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务还款接口返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("===账务还款接口运行失败=====失败原因：%s" % (e))

    # 账务中心-还款试算
    def v2_repayTrial(self):
        url, header = urlVa.url_v2_repayTrial
        data = {
            "appHead": {
                "currentNum": "79",
                "pageEnd": "ipsum labore",
                "pageStart": "consectetur sed",
                "pgupOrPgdn": "cupidatat",
                "totalFlag": "sint commodo",
                "totalNum": "89",
                "totalPages": "amet sint Lorem ipsum commodo",
                "totalRows": "eu elit"
            },
            "body": {
                "loanId": "20",
                "receiptType": "qui voluptate velit",
                "intMethod": "est fugiat non in",
                "isPayPrepaymentCollectionPenalty": True,
                "isPayPrepaymentPenalty": False,
                "receiptDate": "2016-12-01",
                "urgentFlag": "eiusmod cillum exercitation"
            },
            "sysHead": {
                "authFlag": "commodo ut exercitation",
                "branchId": "78",
                "bussSeqNo": "nulla Ut occaecat",
                "company": "culpa",
                "destBranchNo": "ut exercitation culpa",
                "logId": "35",
                "messageCode": "32",
                "messageType": "eiusmod et",
                "moduleId": "34",
                "partnerId": "70",
                "platformId": "66",
                "platformUserId": "47",
                "reference": "adipisicing irure",
                "ret": [
                    {
                        "retCode": "10",
                        "retMsg": "labore eu sed elit"
                    },
                    {
                        "retCode": "72",
                        "retMsg": "commodo sunt veniam fugiat"
                    },
                    {
                        "retCode": "89",
                        "retMsg": "nostrud Excepteur in enim Duis"
                    },
                    {
                        "retCode": "57",
                        "retMsg": "ut dolore ut labore"
                    }
                ],
                "retStatus": "nulla enim ut consequat",
                "runDate": "1999-06-27",
                "seqNo": "commodo in sint",
                "serviceCode": "89",
                "sourceBranchNo": "labore incididunt exercitation",
                "sourceType": "consequat",
                "systemId": "81",
                "tranDate": "1975-06-15",
                "tranMode": "culpa pariatur commodo",
                "tranTimestamp": "2004-07-30 14:44:37",
                "userId": "44",
                "userLang": "eu",
                "wsId": "35"
            }
        }
        try:
            loger.info("=============账务中心还款试算接口========运行开始")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("========账务中心还款试算接口返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError)as e:
            loger.error("===========还款试算接口异常=======异常原因：%s" % (e))

    # 账务中心-新-冲正
    def v2_reversal(self):
        url, header = urlVa.url_v2_reversal
        data = {
            "appHead": {
                "currentNum": "4",
                "pageEnd": "nulla dolore",
                "pageStart": "consequat",
                "pgupOrPgdn": "sunt aliquip",
                "totalFlag": "aute consequat nostrud tempor amet",
                "totalNum": "97",
                "totalPages": "sint mollit",
                "totalRows": "consequat sit dolor anim sint"
            },
            "body": {
                "loanId": "40",
                "reversalReason": "cupidatat"
            },
            "sysHead": {
                "authFlag": "aliqua ad ut pariatur",
                "branchId": "94",
                "bussSeqNo": "ad elit enim",
                "company": "do nulla ipsum",
                "destBranchNo": "in nisi",
                "logId": "7",
                "messageCode": "73",
                "messageType": "magna reprehenderit",
                "moduleId": "14",
                "partnerId": "71",
                "platformId": "75",
                "platformUserId": "62",
                "reference": "enim occaecat Duis culpa",
                "ret": [
                    {
                        "retCode": "34",
                        "retMsg": "aliquip mollit laboris"
                    },
                    {
                        "retCode": "72",
                        "retMsg": "exercitation"
                    },
                    {
                        "retCode": "67",
                        "retMsg": "dolore enim"
                    },
                    {
                        "retCode": "21",
                        "retMsg": "deserunt aliquip dolore"
                    }
                ],
                "retStatus": "ut culpa laborum",
                "runDate": "1981-08-29",
                "seqNo": "Lorem ad",
                "serviceCode": "41",
                "sourceBranchNo": "cillum eiusmod magna",
                "sourceType": "cupidatat ut ea",
                "systemId": "12",
                "tranDate": "2003-04-30",
                "tranMode": "occaecat Excepteur labore",
                "tranTimestamp": "2001-08-10 15:27:34",
                "userId": "71",
                "userLang": "mollit",
                "wsId": "17"
            }
        }
        try:
            loger.info("===============账务中心-新-冲正接口运行开始===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-冲正接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-冲正接口运行失败-失败原因：%s" % (e))

    # 账务中心-老-放款
    def accounts_loan(self, loanid=None, clientNo=None, userId=None, origLoanAmt=None, prodType=None,
                      payeeCertType="01", payeeAcctNo="6236435330000014233", schedMode="1", settleAcctName="锡东消费放款",
                      settleBaseAcctNo="14408200000000052"):
        """
        :param loanid: 订单号
        :param clientNo：核算客户号
        :param userId: 客户号
        :param origLoanAmt: 金额
        :param prodType: 渠道
        payeeCertType：收款账户类型
        payeeAcctNo :收款账户
        schedMode: 还款方式
        :return:
        """

        url, header = urlVa.url_accounts_loan
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "accountingLoanEvent": {
                    "analysis2": "S",
                    "anytimeRec": "N",
                    "autoSettle": "Y",
                    "ccy": "CNY",
                    "clSettle": [{
                        "amtType": "PF",
                        "payRecInd": "PAY",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "PAY",
                        "settleAcctName": settleAcctName,  # "锡东消费放款"
                        "settleAmt": origLoanAmt,  # 放款金额
                        "settleBaseAcctNo": settleBaseAcctNo,  # "14408200000000052"
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "TPP",
                        "settleAcctName": settleAcctName,
                        "settleBaseAcctNo": settleBaseAcctNo,
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "REC",
                        "settleAcctName": "锡东消费回收",
                        "settleBaseAcctNo": "14408200000000066",
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "MRE",
                        "settleAcctName": "保证金账户",
                        "settleBaseAcctNo": "12201010000000013",
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }],
                    "clientNo": clientNo,  # 客户号
                    "cmisloanNo": loanid,  # 借据号
                    "contractNo": loanid,  # 合同号
                    "countryCitizen": "CHN",
                    "fiveCategory": "1",
                    "homeBranch": "100000",
                    "huntingStatus": "Y",
                    "intApplType": "N",
                    "intArray": [{
                        "calcBeginDate": "",
                        "calcEndDate": "",
                        "cycleFreq": "M1",
                        "intClass": "INT",
                        "intDay": "1",
                        "intInd": "Y",
                        "monthBasis": "30",
                        "penaltyOdiRateType": "",
                        "realRate": "15.00",
                        "yearBasis": "360"
                    }, {
                        "calcBeginDate": "",
                        "calcEndDate": "",
                        "cycleFreq": "M1",
                        "intClass": "ODP",
                        "intDay": "1",
                        "intInd": "Y",
                        "monthBasis": "30",
                        "penaltyOdiRateType": "",
                        "realRate": "22.50",
                        "yearBasis": "360"
                    }],
                    "intDay": "1",
                    "intPenalty": "N",
                    "maturityDate": "2021-12-01",
                    "odIntPenalty": "N",
                    "odPriPenalty": "N",
                    "openBranch": "100000",
                    "origLoanAmt": origLoanAmt,  # 金额
                    "ownershipType": "SG",
                    "preRepayDeal": "A",
                    "priPenalty": "Y",
                    "prodType": prodType,  # 渠道
                    "schedMode": schedMode,
                    "startDate": "2020-12-01 09:32:21",
                    "term": "12",
                    "termType": "M",
                    "uiMinAmt": "56.25"
                },
                "operator": "kitas",
                "payEvent": {
                    "payeeAcctName": "张媛媛",
                    "payeeAcctNo": payeeAcctNo,
                    "payeeAcctType": "DEBIT",
                    "payeeBankCode": "323302000012",
                    "payeeBankName": "无锡锡商银行股份有限公司",
                    "payeeCertNo": "320923199101222729",
                    "payeeCertType": payeeCertType
                },
                "userId": userId  # 客户号
            },
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "partnerId": "JZE",
                "platformId": "JTS",
                "seqNo": "d587011ea01d47f8be6f45c328e17e96",
                "sourceBranchNo": "0102",
                "sourceType": "020152",
                "systemId": "KTM",
                "tranDate": "20201201",
                "tranMode": "ONLINE",
                "tranTimestamp": "160678634",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        try:
            loger.info("===========账务中心—老-放款接口开始运行==========")
            res = repuest.post_Req(url=url, json=data, header=header)
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心放款接口测试异常------异常原因：%s" % (e))

    # 账务中心-老-重新放款
    def accounts_reloan(self, loanid=None, clientNo=None, userId=None, origLoanAmt=None, prodType=None,
                        payeeCertType="01", payeeAcctNo="6236435330000014233", schedMode="1", settleAcctName="锡东消费放款",
                        settleBaseAcctNo="14408200000000052"):
        url, header = urlVa.url_accounts_reloan
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "accountingLoanEvent": {
                    "analysis2": "S",
                    "anytimeRec": "N",
                    "autoSettle": "Y",
                    "ccy": "CNY",
                    "clSettle": [{
                        "amtType": "PF",
                        "payRecInd": "PAY",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "PAY",
                        "settleAcctName": settleAcctName,  # "锡东消费放款"
                        "settleAmt": origLoanAmt,  # 放款金额
                        "settleBaseAcctNo": settleBaseAcctNo,  # "14408200000000052"
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "TPP",
                        "settleAcctName": settleAcctName,
                        "settleBaseAcctNo": settleBaseAcctNo,
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "REC",
                        "settleAcctName": "锡东消费回收",
                        "settleBaseAcctNo": "14408200000000066",
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }, {
                        "amtType": "ALL",
                        "payRecInd": "REC",
                        "settleAcctCcy": "CNY",
                        "settleAcctClass": "MRE",
                        "settleAcctName": "保证金账户",
                        "settleBaseAcctNo": "12201010000000013",
                        "settleBranch": "100000",
                        "settleMethod": "R"
                    }],
                    "clientNo": clientNo,  # 客户号
                    "cmisloanNo": loanid,  # 借据号
                    "contractNo": loanid,  # 合同号
                    "countryCitizen": "CHN",
                    "fiveCategory": "1",
                    "homeBranch": "100000",
                    "huntingStatus": "Y",
                    "intApplType": "N",
                    "intArray": [{
                        "calcBeginDate": "",
                        "calcEndDate": "",
                        "cycleFreq": "M1",
                        "intClass": "INT",
                        "intDay": "1",
                        "intInd": "Y",
                        "monthBasis": "30",
                        "penaltyOdiRateType": "",
                        "realRate": "15.00",
                        "yearBasis": "360"
                    }, {
                        "calcBeginDate": "",
                        "calcEndDate": "",
                        "cycleFreq": "M1",
                        "intClass": "ODP",
                        "intDay": "1",
                        "intInd": "Y",
                        "monthBasis": "30",
                        "penaltyOdiRateType": "",
                        "realRate": "22.50",
                        "yearBasis": "360"
                    }],
                    "intDay": "1",
                    "intPenalty": "N",
                    "maturityDate": "2021-12-01",
                    "odIntPenalty": "N",
                    "odPriPenalty": "N",
                    "openBranch": "100000",
                    "origLoanAmt": origLoanAmt,  # 金额
                    "ownershipType": "SG",
                    "preRepayDeal": "A",
                    "priPenalty": "Y",
                    "prodType": prodType,  # 渠道
                    "schedMode": schedMode,
                    "startDate": "2020-12-01 09:32:21",
                    "term": "12",
                    "termType": "M",
                    "uiMinAmt": "56.25"
                },
                "operator": "kitas",
                "payEvent": {
                    "payeeAcctName": "张媛媛",
                    "payeeAcctNo": payeeAcctNo,
                    "payeeAcctType": "DEBIT",
                    "payeeBankCode": "323302000012",
                    "payeeBankName": "无锡锡商银行股份有限公司",
                    "payeeCertNo": "320923199101222729",
                    "payeeCertType": payeeCertType
                },
                "userId": userId  # 客户号
            },
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "partnerId": "JZE",
                "platformId": "JTS",
                "seqNo": "d587011ea01d47f8be6f45c328e17e96",
                "sourceBranchNo": "0102",
                "sourceType": "020152",
                "systemId": "KTM",
                "tranDate": "20201201",
                "tranMode": "ONLINE",
                "tranTimestamp": "160678634",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        try:
            loger.info("========账务中心-老-重新放款接口运行开始=========")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("========账务中心-老-重新放款接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("========账务中心-老-重新放款接口异常异常原因：%s" % (e))

    # 账务中心-老-还款
    def accounts_repay(self):
        url, header = urlVa.url_accounts_repay
        data = {
            "appHead": {
                "currentNum": "53",
                "pageEnd": "mollit",
                "pageStart": "labore culpa",
                "pgupOrPgdn": "minim occaecat Excepteur aliqua",
                "totalFlag": "anim",
                "totalNum": "43",
                "totalPages": "dolor sunt",
                "totalRows": "nisi culpa ad"
            },
            "body": {
                "cmisloanNo": "eiusmod qui",
                "operator": "enim nulla",
                "receiptType": "incididunt dolore eiusmod",
                "repayAcctInfo": {
                    "payerAcctName": "规队群且设行而",
                    "payerAcctNo": "culpa fugiat non Ut",
                    "payerAcctType": "in laborum ad esse",
                    "payerCertNo": "nisi dolor",
                    "payerCertType": "sint",
                    "payerPhone": "13531554662"
                },
                "repayType": 78221872,
                "ccy": "aliquip occaecat labore reprehenderit",
                "clSettle": [
                    {
                        "payerAcctName": "权广个界群",
                        "payerAcctNo": "in fugiat",
                        "payerAcctType": "in in aute",
                        "payerCertNo": "ullamco exercitation Lorem",
                        "payerCertType": "ullamco consectetur mollit laborum ex",
                        "payerPhone": "18184805215"
                    }
                ],
                "clientNo": "elit ad",
                "feeInfoArray": [
                    {
                        "discountAmt": 77,
                        "discountType": "42",
                        "feeCcy": "in in veniam cillum nulla",
                        "feeInfoAmt": 21,
                        "feeInfoAmtRec": 44,
                        "feeType": "fugiat elit exercitation sed dolor"
                    },
                    {
                        "discountAmt": 30,
                        "discountType": "58",
                        "feeCcy": "dolor",
                        "feeInfoAmt": 35,
                        "feeInfoAmtRec": 12,
                        "feeType": "fugiat Duis cupidatat non"
                    },
                    {
                        "discountAmt": 88,
                        "discountType": "69",
                        "feeCcy": "incididunt cupidatat dolor",
                        "feeInfoAmt": 53,
                        "feeInfoAmtRec": 56,
                        "feeType": "voluptate deserunt velit cupidatat qui"
                    }
                ],
                "mreYn": "ad fugiat eu Lorem",
                "optionCtl": "laborum est",
                "receiptAmt": 70,
                "receiptFee": 89,
                "userId": "97"
            },
            "sysHead": {
                "authFlag": "irure adipisicing",
                "branchId": "27",
                "bussSeqNo": "dolore",
                "company": "consequat veniam ad deserunt culpa",
                "destBranchNo": "commodo",
                "logId": "56",
                "messageCode": "71",
                "messageType": "labore et eiusmod",
                "moduleId": "39",
                "partnerId": "3",
                "platformId": "19",
                "platformUserId": "11",
                "reference": "minim in labore",
                "ret": [
                    {
                        "retCode": "81",
                        "retMsg": "sint fugiat esse"
                    }
                ],
                "retStatus": "eu",
                "runDate": "2009-08-11",
                "seqNo": "Excepteur elit incididunt aute",
                "serviceCode": "25",
                "sourceBranchNo": "Excepteur occaecat exercitation aute nulla",
                "sourceType": "elit",
                "systemId": "30",
                "tranDate": "1980-11-12",
                "tranMode": "ad deserunt",
                "tranTimestamp": "2013-06-23 02:50:34",
                "userId": "64",
                "userLang": "dolore incididunt sed dolor",
                "wsId": "22"
            }
        }
        try:
            loger.info("=============账务中心-老-还款接口运行开始============")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("===============账务中心-老-还款接口返回报文===%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("=============账务中心-老-还款接口运行异常--异常原因：%s" % (e))

    # 账务中心-老-放款状态查询
    def accounts_loan_show(self, loanid=None):
        url, header = urlVa.url_accounts_loan_show
        print(header)
        print(url)
        data = {
            "appHead": {
                "currentNum": "88",
                "pageEnd": "est incididunt proident veniam dolor",
                "pageStart": "laboris",
                "pgupOrPgdn": "enim voluptate nisi dolor",
                "totalFlag": "velit pariatur",
                "totalNum": "99",
                "totalPages": "velit laboris ipsum",
                "totalRows": "mollit anim occaecat"
            },
            "body": loanid,
            "sysHead": {
                "authFlag": "dolor eiusmod mollit dolore cupidatat",
                "branchId": "97",
                "bussSeqNo": "do",
                "company": "ex",
                "destBranchNo": "dolor Duis laborum",
                "logId": "95",
                "messageCode": "15",
                "messageType": "dolore Ut consequat in",
                "moduleId": "92",
                "partnerId": "13",
                "platformId": "51",
                "platformUserId": "26",
                "reference": "deserunt dolore cillum",
                "ret": [{
                    "retCode": "29",
                    "retMsg": "minim velit sunt exercitation"
                }],
                "retStatus": "in mollit",
                "runDate": "2017-01-04",
                "seqNo": "ut ea commodo consectetur ipsum",
                "serviceCode": "52",
                "sourceBranchNo": "sunt labore cupidatat nulla",
                "sourceType": "dolore est id",
                "systemId": "64",
                "tranDate": "2014-07-21",
                "tranMode": "culpa sit ut amet dolore",
                "tranTimestamp": "1993-04-25 04:44:21",
                "userId": "11",
                "userLang": "sunt mollit",
                "wsId": "64"
            }
        }
        print(data)
        try:
            loger.info("=============账务中心-老-放款状态查询运行开始============")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("===============账务中心-老-放款状态查询返回报文===%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("=============账务中心-老-放款状态查询运行异常--异常原因：%s" % (e))

    # 账务中心-老-还款计划查询
    def plan_list(self, loanid=None):
        url, header = urlVa.plan_list
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": loanid,
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "platformId": "DHGL",
                "seqNo": "8d6c8e79cc6f4b4ba1d851a3f671c46c",
                "sourceBranchNo": "0102",
                "sourceType": "010113",
                "systemId": "PL",
                "tranDate": "20201202",
                "tranMode": "ONLINE",
                "tranTimestamp": "160687462",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        try:
            loger.info("=============账务中心-老-还款接口运行开始============")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("===============账务中心-老-还款接口返回报文===%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("=============账务中心-老-还款接口运行异常--异常原因：%s" % (e))

    # 账务中心-老-还款试算
    def accounts_repayTrial(self, loanid=None, receiptType=None):
        url, header = urlVa.url_accounts_repayTrial
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "cmisloanNo": loanid,  # 订单号
                "dueDate": "",
                "intMethod": "",
                "optionKw": "",
                "priOutstanding": "",
                "receiptType": receiptType,  # 还款类型
                "schedTotalAmt": "",
                "stageNo": "",
                "syncFinalBilling": ""
            },
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "platformId": "JTS",
                "seqNo": "fe9d9cd689874848bead96e402877b79",
                "sourceBranchNo": "0102",
                "sourceType": "020152",
                "systemId": "KTM",
                "tranDate": "20201202",
                "tranMode": "ONLINE",
                "tranTimestamp": "160687926",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        try:
            loger.info("===============账务中心-老-还款试算===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-老-还款试算接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-老-还款试算接口运行失败-失败原因：%s" % (e))

    # 账务中心-新-放款-目前仅用于长安新生
    def accounts_V2_loan(self, loanId=None, clientNo='', userId='', loanAmount=60000.00,
                         operator='kitas',
                         partnerId='CAXS', prodType='110118', interestRate=15.30, term=6, termType='M', repayMode="1",
                         payeeAccDept='无锡锡商银行股份有限公司', payeeAcctName='张媛媛', payeeAcctNo='6236435330000014233',
                         payeeCertNo='320923199101222729', payeeAcctType='DEBIT', payeeCertType='01', payeeBankCode=''
                         ):
        url, header = urlVa.url_accounts_V2_loan
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "clientNo": clientNo,
                "contributionAccount": {
                    "accountName": "",
                    "accountNo": ""
                },
                "customerInterestRate": 15.300000,
                "entrustedAccount": {
                    "accountName": "无锡锡商银行股份有限公司",
                    "accountNo": "6236435330000002196"
                },
                "interestDay": "18",
                "interestRate": interestRate,
                "loanAmount": loanAmount,
                "loanId": loanId,
                "operator": operator,
                "payeeAccount": {
                    "payeeAccDept": payeeAccDept,
                    "payeeAcctName": payeeAcctName,
                    "payeeAcctNo": payeeAcctNo,
                    "payeeAcctType": payeeAcctType,
                    "payeeCertNo": payeeCertNo,
                    "payeeCertType": payeeCertType,
                    "payeeBankCode": payeeBankCode
                },
                "penaltyRate": 22.950000,
                "prodType": prodType,
                "repayMode": repayMode,
                "term": term,
                "termType": termType,
                "userId": userId
            },
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "partnerId": partnerId,
                "platformId": "JTS",
                "seqNo": "88ab3fdfb9f14cd09cc07d03efc84c62",
                "sourceBranchNo": "0102",
                "sourceType": "020152",
                "systemId": "KTM",
                "tranDate": "20210701",
                "tranMode": "ONLINE",
                "tranTimestamp": "160682354",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        # print(data)
        try:
            loger.info("===============账务中心-新-放款-目前仅用于长安新生===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-放款-目前仅用于长安新生接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-放款-目前仅用于长安新生接口运行失败-失败原因：%s" % (e))

    # 账务中心-新-还款试算
    def accounts_V2_repayTrial(self, loanId=None, receiptDate='20290825', receiptType='2',
                               intMethod='1', isPayPrepaymentCollectionPenalty=True, isPayPrepaymentPenalty=True,
                               urgentFlag='N'):
        url, header = urlVa.url_accounts_V2_repayTrial
        data = {
            "appHead": {},
            "body": {
                "loanId": loanId,
                "receiptType": "2",
                "intMethod": "1",
                "isPayPrepaymentCollectionPenalty": False,
                "isPayPrepaymentPenalty": False,
                "receiptDate": receiptDate,
                "urgentFlag": "N"
            },
            "sysHead": {}
        }
        try:
            loger.info("===============账务中心-新-还款试算===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-还款试算接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-还款试算接口运行失败-失败原因：%s" % (e))

    # 账务中心-老-new-还款
    def accounts_repay_new(self, clientNo=None, loanId=None, receiptAmt=None, receiptType=None, userId=None,
                           payerAcctNo='6214832509940735'):
        url, header = urlVa.url_accounts_repay_new
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "clientNo": clientNo,  # 核心客户号
                "loanId": loanId,  # 订单号
                "operator": "test11",
                "optionCtl": "Y",
                "prepaymentCollectionPenaltyPayType": 1,
                "prepaymentPenaltyPayType": 1,
                "receiptAmt": receiptAmt,  # 还款金额
                "receiptType": receiptType,  # 放款方式
                "repayAcctInfo": {
                    "payerAcctName": "张正杰",
                    "payerAcctNo": payerAcctNo,
                    "payerAcctType": "DEBIT",
                    "payerCertNo": "320923199101222729",
                    "payerCertType": "01",
                    "payerPhone": "18661279193"
                },
                "repayType": 2,
                "reqSeqNo": "PLMR2017120800000003",
                "userId": userId  # 用户userid
            },
            "sysHead": {
                "authFlag": "N",
                "branchId": "100001",
                "company": "XSBANK",
                "destBranchNo": "0106",
                "moduleId": "li",
                "platformId": "DHGL",
                "seqNo": "9c509b40e5d74f43a7a6d8fbb6ea797d",
                "sourceBranchNo": "0102",
                "sourceType": "010113",
                "systemId": "PL",
                "tranDate": "20201208",
                "tranMode": "ONLINE",
                "tranTimestamp": "160739689",
                "userId": "cp0102",
                "userLang": "CHINESE",
                "wsId": "001"
            }
        }
        try:
            loger.info("===============账务中心-老-new-还款===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-老-new-还款接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-老-new-还款接口运行失败-失败原因：%s" % (e))

    # 账务中心-老-new-会计日
    def accounts_hxDate_async(self):
        url, header = urlVa.url_accounts_hxDate_async
        data = {
            "appHead": {
                "currentNum": "7",
                "pageEnd": "pariatur",
                "pageStart": "culpa",
                "pgupOrPgdn": "aute",
                "totalFlag": "elit cupidatat cillum sint sed",
                "totalNum": "71",
                "totalPages": "in",
                "totalRows": "fugiat cupidatat"
            },
            "sysHead": {
                "authFlag": "sit aliqua eu",
                "branchId": "4",
                "bussSeqNo": "ullamco in nisi ad",
                "company": "dolore ea tempor fugiat",
                "destBranchNo": "consectetur magna reprehenderit quis",
                "logId": "85",
                "messageCode": "70",
                "messageType": "est aute",
                "moduleId": "40",
                "partnerId": "91",
                "platformId": "87",
                "platformUserId": "96",
                "reference": "laboris sunt enim",
                "ret": [
                    {
                        "retCode": "66",
                        "retMsg": "aute non velit Ut"
                    },
                    {
                        "retCode": "26",
                        "retMsg": "commodo aliquip"
                    },
                    {
                        "retCode": "70",
                        "retMsg": "qui ipsum aliqua nostrud sed"
                    }
                ],
                "retStatus": "mollit ut irure",
                "runDate": "1988-06-23",
                "seqNo": "Excepteur in est ipsum",
                "serviceCode": "89",
                "sourceBranchNo": "amet qui sunt cillum commodo",
                "sourceType": "deserunt",
                "systemId": "56",
                "tranDate": "1991-02-28",
                "tranMode": "est non anim",
                "tranTimestamp": "1989-06-16 16:34:24",
                "userId": "73",
                "userLang": "deserunt voluptate nisi",
                "wsId": "59"
            }
        }
        try:
            loger.info("===============账务中心-老-new-会计日===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-老-new-会计日接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-老-new-会计日接口运行失败-失败原因：%s" % (e))

    # 账务中心-老-冲正
    def accounts_reversal(self, cmisloanNo=None, reversal=None, reversalReason=None):
        url, header = urlVa.url_accounts_reversal
        data = {
            "appHead": {
                "currentNum": "60",
                "pageEnd": "proident incididunt",
                "pageStart": "amet in",
                "pgupOrPgdn": "magna in ipsum sunt",
                "totalFlag": "minim",
                "totalNum": "44",
                "totalPages": "consectetur ut voluptate",
                "totalRows": "in id ex"
            },
            "body": {
                "cmisloanNo": cmisloanNo,  # 借据号
                "reversal": reversal,  # 冲正标志
                "reversalReason": reversalReason  # 冲销原因
            },
            "sysHead": {
                "authFlag": "laborum consequat",
                "branchId": "68",
                "bussSeqNo": "ex voluptate",
                "company": "occaecat eiusmod adipisicing",
                "destBranchNo": "quis",
                "logId": "38",
                "messageCode": "54",
                "messageType": "dolore ut",
                "moduleId": "49",
                "partnerId": "9",
                "platformId": "27",
                "platformUserId": "61",
                "reference": "sunt adipisicing Excepteur deserunt consequat",
                "ret": [
                    {
                        "retCode": "97",
                        "retMsg": "ipsum occaecat quis laborum"
                    },
                    {
                        "retCode": "30",
                        "retMsg": "Duis"
                    },
                    {
                        "retCode": "58",
                        "retMsg": "consequat in culpa dolore"
                    },
                    {
                        "retCode": "45",
                        "retMsg": "velit Duis nostrud et nisi"
                    }
                ],
                "retStatus": "reprehenderit nisi",
                "runDate": "2009-04-13",
                "seqNo": "culpa non sed",
                "serviceCode": "39",
                "sourceBranchNo": "anim sunt",
                "sourceType": "aute non cupidatat",
                "systemId": "43",
                "tranDate": "1993-10-21",
                "tranMode": "ex nostrud laboris laborum",
                "tranTimestamp": "2008-01-29 02:15:46",
                "userId": "35",
                "userLang": "cillum magna sunt nulla",
                "wsId": "84"
            }
        }
        try:
            loger.info("===============账务中心-老-冲正===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-老-冲正接口运行返回报文：%s" % (res.text))
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-老-冲正接口运行失败-失败原因：%s" % (e))

    # 账务中心-新-冲正
    def accounts_V2_reversal(self, loanId=None, reason='测试'):
        url, header = urlVa.url_accounts_V2_reversal
        data = {
            "appHead": {},
            "body": {
                "loanId": loanId,
                "reversalReason": reason
            },
            "sysHead": {}
        }
        try:
            loger.info("===============账务中心-新-冲正===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-冲正接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-冲正接口运行失败-失败原因：%s" % (e))

    def accounts_repayStatus_query(self, loanid=None):
        url, header = urlVa.url_accounts_repayStatus_query
        data = {
            "appHead": {
                "currentNum": "42",
                "pageEnd": "in labore dolore amet",
                "pageStart": "quis sit esse incididunt enim",
                "pgupOrPgdn": "consectetur Excepteur anim ut",
                "totalFlag": "sed aliqua in est",
                "totalNum": "20",
                "totalPages": "in dolore mollit magna",
                "totalRows": "reprehenderit nulla sunt"
            },
            "body": loanid,
            "sysHead": {
                "authFlag": "elit",
                "branchId": "36",
                "bussSeqNo": "veniam",
                "company": "velit nostrud nisi",
                "destBranchNo": "id commodo aliqua",
                "logId": "52",
                "messageCode": "11",
                "messageType": "veniam ipsum mollit",
                "moduleId": "21",
                "partnerId": "18",
                "platformId": "96",
                "platformUserId": "32",
                "reference": "magna",
                "ret": [
                    {
                        "retCode": "19",
                        "retMsg": "amet enim"
                    },
                    {
                        "retCode": "21",
                        "retMsg": "in anim aliquip"
                    },
                    {
                        "retCode": "25",
                        "retMsg": "dolore qui"
                    }
                ],
                "retStatus": "anim Duis tempor consectetur",
                "runDate": "1986-04-08",
                "seqNo": "ut sed officia proident",
                "serviceCode": "95",
                "sourceBranchNo": "velit",
                "sourceType": "minim dolor",
                "systemId": "5",
                "tranDate": "1987-07-03",
                "tranMode": "non labore ullamco aliqua nisi",
                "tranTimestamp": "2000-06-10 22:44:56",
                "userId": "85",
                "userLang": "Ut Duis",
                "wsId": "10"
            }
        }
        try:
            loger.info("===============账务中心-新-冲正===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-冲正接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-冲正接口运行失败-失败原因：%s" % (e))

    def mock_accounts(self, loanid, uppStatus):
        # loanid 订单号
        # uppStatus  聚合支付状态00（成功）、01（失败）
        url = "http://10.10.67.90:8070/accounts/compensate/loan?pwd=accp&loanId=%s&uppStatus=%s" % (loanid, uppStatus)
        print(url, type(url))
        headers = {'Content-Type': 'application/json; charset=UTF-8', 'token': 'ec73aaa3-412a-4fa0-81d9-6d3ce9171186'}
        payload = {}
        try:
            res = requests.request("GET", url, headers=headers, data=payload)
            print(res.text.encode('utf8'))
            loger.info("账务中心-mock成功接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-mock成功接口运行失败-失败原因：%s" % (e))

    # 账务中心-新-还款
    def accounts_V2_repay(self, clientNo=None, loanId=None, reqSeqNo=None, receiptAmt=None, userId=None,
                          receiptType='2'):
        url, header = urlVa.url_accounts_V2_repay
        data = {
            "appHead": {
                "currentNum": "",
                "pageEnd": "",
                "pageStart": "",
                "pgupOrPgdn": "",
                "totalFlag": "",
                "totalNum": "6",
                "totalPages": "",
                "totalRows": ""
            },
            "body": {
                "clientNo": clientNo,
                "loanId": loanId,
                "operator": "119",
                "receiptType": receiptType,
                "repayAcctInfo": {
                    "payerAcctName": "张媛媛",
                    "payerAcctNo": "6217856100017468910",
                    "payerAcctType": "DEBIT",
                    "payerCertNo": "320923199101222729",
                    "payerCertType": "01",
                    "payerPhone": "18661279193"
                },
                "repayType": 1,
                "reqSeqNo": reqSeqNo,
                "userId": userId,
                "feeInfoArray": [
                    {
                        "discountAmt": 55,
                        "discountType": "81",
                        "feeCcy": "",
                        "feeInfoAmt": 29,
                        "feeInfoAmtRec": 33,
                        "feeType": ""
                    },
                    {
                        "discountAmt": 16,
                        "discountType": "93",
                        "feeCcy": "",
                        "feeInfoAmt": 63,
                        "feeInfoAmtRec": 91,
                        "feeType": ""
                    },
                    {
                        "discountAmt": 61,
                        "discountType": "33",
                        "feeCcy": "",
                        "feeInfoAmt": 58,
                        "feeInfoAmtRec": 32,
                        "feeType": ""
                    }
                ],
                "optionCtl": "",
                "prepaymentCollectionPenalty": 1,
                "prepaymentCollectionPenaltyPayType": 1,
                "prepaymentPenalty": 1,
                "prepaymentPenaltyPayType": 1,
                "receiptAmt": receiptAmt,
                "urgentFlag": ""
            },
            "sysHead": {
                "authFlag": "",
                "branchId": "15",
                "bussSeqNo": "",
                "company": "",
                "destBranchNo": "",
                "logId": "6",
                "messageCode": "14",
                "messageType": "",
                "moduleId": "86",
                "partnerId": "2",
                "platformId": "37",
                "platformUserId": "31",
                "reference": "",
                "ret": [
                    {
                        "retCode": "3",
                        "retMsg": ""
                    },
                    {
                        "retCode": "48",
                        "retMsg": ""
                    }
                ],
                "retStatus": "",
                "runDate": "",
                "seqNo": "",
                "serviceCode": "89",
                "sourceBranchNo": "",
                "sourceType": "",
                "systemId": "",
                "tranDate": "",
                "tranMode": "",
                "tranTimestamp": "",
                "userId": "87",
                "userLang": "",
                "wsId": "81"
            }
        }
        try:
            loger.info("===============账务中心-新-还款===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-还款接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-还款接口运行失败-失败原因：%s" % (e))

    # 还款查询
    def accounts_repayStatus_query(self, loanid=None):
        url, header = urlVa.url_accounts_repayStatus_query
        data = {
            "appHead": {
                "currentNum": "67",
                "pageEnd": "sed proident enim veniam",
                "pageStart": "reprehenderit",
                "pgupOrPgdn": "non adipisicing amet consequat",
                "totalFlag": "cillum culpa ut",
                "totalNum": "67",
                "totalPages": "laborum",
                "totalRows": "in eiusmod"
            },
            "body": loanid,
            "sysHead": {
                "authFlag": "ut ad qui ipsum",
                "branchId": "32",
                "bussSeqNo": "in",
                "company": "esse amet",
                "destBranchNo": "sint enim ut ut",
                "logId": "94",
                "messageCode": "39",
                "messageType": "cillum culpa proident et",
                "moduleId": "23",
                "partnerId": "98",
                "platformId": "65",
                "platformUserId": "10",
                "reference": "ad sit cillum ipsum",
                "ret": [
                    {
                        "retCode": "91",
                        "retMsg": "laboris cupidatat velit sit"
                    },
                    {
                        "retCode": "47",
                        "retMsg": "sint eiusmod dolor"
                    },
                    {
                        "retCode": "46",
                        "retMsg": "occaecat Lorem"
                    },
                    {
                        "retCode": "57",
                        "retMsg": "commodo exercitation pariatur ad"
                    }
                ],
                "retStatus": "mollit quis occaecat anim",
                "runDate": "1983-04-21",
                "seqNo": "minim",
                "serviceCode": "8",
                "sourceBranchNo": "dolore proident",
                "sourceType": "Ut velit fugiat est",
                "systemId": "70",
                "tranDate": "2002-02-17",
                "tranMode": "officia sit",
                "tranTimestamp": "1998-11-17 05:33:34",
                "userId": "42",
                "userLang": "nisi proident culpa",
                "wsId": "34"
            }
        }
        try:
            loger.info("===============账务中心-新-还款===================")
            res = repuest.post_Req(url=url, json=data, header=header)
            loger.info("账务中心-新-还款接口运行返回报文：%s" % (res.text))
            print(res.json())
            return res
        except (ZeroDivisionError, TypeError, NameError) as e:
            loger.error("账务中心-新-还款接口运行失败-失败原因：%s" % (e))


if __name__ == "__main__":
    a = Interface_Data()
    # ee = a.accounts_loan_show(loanid="20171202000006")
    # print(ee.json())
    # kk = a.accounts_V2_loan(loanId='20171202000012')
    # print("ww:", kk.json())
    # a.accounts_V2_repayTrial(loanId='20171203000011',receiptDate='20280731')
    b = a.accounts_repayStatus_query(loanid='20171203000011')
    # print(b.text)
    print(b.json())
    # c = a.accounts_repay_new(loanId='20171215000070',receiptType=2,clientNo='1000000040',
    #                          receiptAmt=700000.00,userId='010000003211')
    # b = a.mock_accounts(loanid='20171217000431',uppStatus='00')
    # c = a.accounts_repay_new(loanId='20171217000431',receiptType=2,clientNo='1000000040',
    #                          receiptAmt=300000.00,userId='010000003211')
    # print(c.json())
    # print(b.json())
    # a.accounts_V2_repay(loanId='20171217000431',userId='010000003211',
    #                     clientNo='1000000040',receiptAmt='300000',reqSeqNo='PLMR20171217000431')
