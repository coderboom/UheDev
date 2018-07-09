import HTMLTestRunner
from DevPurchase.LoginModule import LoginTestCase
import os
import unittest
# get the directory path to output report file
dir = os .getcwd()

# 需要测试的测试用例
Login_Test = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase.TestLogin)
# 加载所有的 test case
test_suite = unittest.TestSuite([Login_Test, ])

# open the report file
outputfile = open(dir+'\\SeleniumTestLogin.html', 'wb')

# 配置
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outputfile, title="登陆测试", description='Acceptance Tests')
# 开始运行
runner.run(test_suite)
