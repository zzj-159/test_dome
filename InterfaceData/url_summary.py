# -*- coding: utf-8 -*-
# @Time    : 2020/10/28
# @Author  : 张正杰
# @Fuction : 配置传参

from common.getAPI_Info import API_Info
from common.getEnv import environment
from common.login import Login


class url_variable():
    def data_header(self, port):
        login = Login(port)
        header = login.header  # 获取header
        return header

    def data_url(self, port):
        Env = environment()
        host = Env.Host  # 获取前置url
        url = host + port  # url 拼装
        return url

    def pawn_url(self, port):
        Env = environment()
        host = Env.pawn_Host  # 获取前置url
        url = host + port  # url 拼装
        return url

    def accounts_url(self, port):
        Enx = environment()
        host = Enx.accounts_Host
        url = host + port
        return url

    @property
    def url_v2_loan(self):  # 账务-新 放款/重新放款
        port = '/accounts/v2/loan'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_v2_repay(self):  # 账务-新 还款
        port = '/accounts/v2/repay'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_v2_repayTrial(self):  # 账务中心 -新 还款试算
        port = '/accounts/v2/repayTrial'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_v2_reversal(self):  # 账务中心-新  冲正
        port = '/accounts/v2/reversal'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_loan(self):  # 账务中心-老-放款
        port = '/accounts/loan'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_reloan(self):  # 账务中心-老-重新放款
        port = '/accounts/reloan'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repay(self):  # 账务中心-老-还款
        port = '/accounts/repay'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_loan_show(self):  # 账务中心-老-放款状态查询
        port = '/accounts/loanStatus/query'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def plan_list(self):  # 账务中心-老-还款计划查询
        port = '/accounts/repay/plan/list'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repayTrial(self):  # 账务中心-老-还款试算
        port = '/accounts/repayTrial'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_V2_loan(self):  # 账务中心-新-放款
        port = '/accounts/v2/loan'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repayTrial(self):  # 账务中心-老-还款试算接口
        port = '/accounts/repayTrial'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repay_new(self):  # 账务中心-老-new-还款
        port = '/accounts/repay/new'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_hxDate_async(self):  # 账务中心-老-会计日期
        port = '/accounts/hxDate/async'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_reversal(self):  # 账务中心—老-冲正
        port = '/accounts/reversal'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_V2_repayTrial(self):  # 账务中心-新-还款试算
        port = '/accounts/v2/repayTrial'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_V2_reversal(self):  # 账务中心-新-冲正
        port = '/accounts/v2/reversal'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repayStatus_query(self):  # 账务中心-老-还款查询
        port = '/accounts/repayStatus/query'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_V2_repay(self):  # 账务中心-新-还款
        port = '/accounts/v2/repay'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header

    @property
    def url_accounts_repayStatus_query(self):  # 账务中心-还款-还款状态查询
        port = '/accounts/repayStatus/query'
        url = self.accounts_url(port=port)
        header = self.data_header(port=port)
        return url, header


if __name__ == "__main__":
    a = url_variable()
    url, header = a.url_accounts_V2_repay
    url, header = a.url_accounts_repayTrial
    print(url, header)
