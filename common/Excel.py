# !/usr/bin/python
# -*- coding: UTF-8 _*_
# @Time    : 2020/11/20
# @Author  : zhangzhengjie

import pandas as pd
import xlrd
from xlutils.copy import copy


class find_rom:

    def find_row_one(self, num_value, file_name):
        """
        Returns the row number based on the value of the specified cell
        """
        demo_df = pd.read_excel(file_name)
        if '[' in num_value:
            on = num_value.split('[')
            for indexs in demo_df.index:
                for i in range(len(demo_df.loc[indexs].values)):
                    if (str(demo_df.loc[indexs].values[i]) == on[0]):
                        row = str(indexs + 2).rstrip('L')
                        print(row)
                        return row
        else:
            for indexs in demo_df.index:
                for i in range(len(demo_df.loc[indexs].values)):
                    if (str(demo_df.loc[indexs].values[i]) == num_value):
                        row = str(indexs + 2).rstrip('L')
                        print(row)
                        return row

                    # if ((str(demo_df.loc[indexs].values[i]) == on[0]):
                    #     return str(indexs +2).rstrip('L')

    def excel_append(self, file, name, num):
        '''
        :param file: 地址
        :param name: 添加内容 通过   跳过  失败   错误   预期失败    预期通过
        :param num: 位置
        :return:
        '''
        # demo_df = pd.read_excel(file)
        # for indexs in demo_df.index:
        #     for i in range(len(demo_df.loc[indexs].values)):
        #         if (str(demo_df.loc[indexs].values[i]) == data):
        #             self.row = str(indexs + 2).rstrip('L')
        #
        # print(self.row, type(self.row))
        file = file
        wb = xlrd.open_workbook(file)  # 打开工作簿
        sheets = wb.sheet_names()  # 获取工作簿中的所有表格
        worksheet = wb.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        # rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(wb)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        # sheet_copy = data_copy.get_sheet(0)  # 从data_copy对象中获取第一个sheet对象
        # a = int(num) - 1
        # print(a)
        if name == "passed":
            # print(type(int(num) - 1))
            new_worksheet.write((int(num) - 1), 4, name)
        else:
            # print(type(int(num) - 1))
            new_worksheet.write((int(num) - 1), 4, name)
            new_worksheet.write((int(num) - 1), 5, "错误")

        # for i in range(2):
        #     for j in range(2):
        #         new_worksheet.write(i + rows_old, j, "测试内容")
        new_workbook.save(file)  # 保存工作簿
        print("追加写入成功！")


if __name__ == "__main__":
    a = find_rom()
    num = a.find_row_one('test_01_BorrowerInquiriesOrder_用户编号userId存在_获取订单信息[]',
                         'D:/test-loanorder_19/dataPreparation/test.xls')
    print(num)
    # print(num)
    # seat = a.excel_append('D:/test-loanorder_19/dataPreparation/test.xls', 'cs写入内容', num=num)
