import unittest
import selenium

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.base_url = 'http://dev.uhetrip.com:13215/signin?ref=root'

    def test_login(self):
        browser = self.browser
        browser.get(self.base_url)
        browser.maximize_window()
        browser.implicitly_wait(5)

        user_name = 'lisisi'
        user_pwd = 'aa2345'

        user_name_element = 'username'
        user_pwd_element = 'password'
        identify_code_element = '//*[@id="siginBoxCard"]/div[2]/form/div[3]/div/div[1]/div/div/div/input'
        loading_btn_element = 'isloading_btn'
        submenu_title_element = '/html/body/div[1]/div/div/div/div[2]/ul/li[4]/div'
        
        user_name_input = browser.find_element_by_id(user_name_element)
        user_name_input.is_displayed()
        user_pwd_input = browser.find_element_by_id(user_pwd_element)
        user_pwd_input.is_displayed()
        identify_code_input = browser.find_element_by_xpath(
            identify_code_element)
        identify_code_input.is_displayed()
        loading_btn_click = browser.find_element_by_id(loading_btn_element)
        loading_btn_click.is_displayed()

        user_name_input.send_keys(user_name)
        user_pwd_input.send_keys(user_pwd)
        identify_code_input.send_keys('0328')
        loading_btn_click.click()

        browser.implicitly_wait(10)
        # submenu_title_text = browser.find_element_by_xpath(
        #  '/html/body/div[1]/div/div/div/div[2]/ul/li[4]/div').getText()
        #  定位到标签，用 .text获取text
        submenu_title_text = browser.find_element_by_xpath(
            submenu_title_element).text
        if submenu_title_text == user_name:
            print('登陆成功')
        else:
            print('登陆失败')
        
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
