#encoding:utf-8
'''执行测试用例'''
import unittest
import  os
from beautifulReport import BeautifulReport
'''通过loader的方式来查找执行的用例'''
suite=unittest.TestLoader().discover(start_dir='cases',
                                     pattern='test*.py',
                                     top_level_dir=None)
# with open(,'wb') as file:
runer=BeautifulReport(suite).report(filename='CI测试报告',
                                    description='勺子课堂API',
                                    log_path='.',
                                    verbosity=2)