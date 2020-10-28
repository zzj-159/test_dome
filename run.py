# !/usr/bin/python
# -*- coding: UTF-8 _*_

import time
import os
from common.Log import MyLog
import pytest
import subprocess
from common import Shell
def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == "__main__":
    logger = MyLog
    path = "./testCase"
    # dirs = os.listdir(path)  # 获取指定路径下的文件
    # for i in dirs:  # 循环读取路径下的文件并筛选输出
    #     if os.path.splitext(i)[1] == ".py":  # 筛选py文件
    #         print(i)

    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        pytest.main([path,"--alluredir", "./report/reportallure"])
        print("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败！%s" % (e))
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        # os.system('allure serve ./report/reportallure')
        # os.system('allure generate %s -o %s --clean'%('./report/reportallure', './report/reporthtml'))
        cmd = 'allure generate %s -o %s --c' % ('./report/reportallure', './report/reporthtml')
        logger.info("开始执行报告生成")
        print("开始执行报告生成")
        # cmd = 'allure generate %s -o %s -c' % (project_path + dir_manage('${report_xml_dir}$'),
                                               # project_path + dir_manage('${report_html_dir}$'))
        invoke(cmd)
        # shell.invoke(cmd)
        logger.info("报告生成完毕")
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        logger.error("报告生成失败，请重新执行%s" % (e))
        logger.error('执行用例失败，请检查环境配置')
        raise

    # time.sleep(5)
