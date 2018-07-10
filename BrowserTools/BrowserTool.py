import os
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Browser(object):
    def __init__(self):
        self.browser_type = None

    # 打开浏览器的方法
    def Openbrowser(self):
        if self.browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            self.driver = webdriver.Ie()
        elif self.browser_type == '':
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
