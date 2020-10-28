# !/usr/bin/python
# -*- coding: UTF-8 _*_
import time
import os
from common.Log import MyLog
import pytest
from common import Shell

if __name__ == "__main__":
    path = "./testCase"
    pytest.main([path,'--result-log=report/reportallure/test.log',
                      '--junit-xml=report/reportallure/test.xml',
                 '--html=report/reporthtml/test.html'])
