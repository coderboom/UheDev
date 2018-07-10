import unittest, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class WhiteTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(3)
        cls.base_url = 'http://dev.uhetrip.com:13215/signin?ref=root'

        cls.browser.get(cls.base_url)
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(5)

        user_name = 'lisi'
        user_pwd = 'aa234'

        user_name_element = 'username'
        user_pwd_element = 'password'
        identify_code_element = '//*[@id="siginBoxCard"]/div[2]/form/div[3]/div/div[1]/div/div/div/input'
        loading_btn_element = 'isloading_btn'
        submenu_title_element = '/html/body/div[1]/div/div/div/div[2]/ul/li[5]/div'

        # user_name_input = browser.find_element_by_id(user_name_element)
        user_name_input = cls.browser.find_element(By.ID, user_name_element)
        user_name_input.is_displayed()
        user_pwd_input = cls.browser.find_element_by_id(user_pwd_element)
        user_pwd_input.is_displayed()
        identify_code_input = cls.browser.find_element_by_xpath(
            identify_code_element)
        identify_code_input.is_displayed()
        loading_btn_click = cls.browser.find_element_by_id(loading_btn_element)
        loading_btn_click.is_displayed()

        user_name_input.send_keys(user_name)
        user_pwd_input.send_keys(user_pwd)
        identify_code_input.send_keys('0328')
        loading_btn_click.click()

        cls.browser.implicitly_wait(10)
        # submenu_title_text = browser.find_element_by_xpath(
        #  '/html/body/div[1]/div/div/div/div[2]/ul/li[4]/div').getText()
        # /html/body/div[1]/div/div/div/div[2]/ul/li[5]/div/text()
        #  定位到标签，用 .text获取text
        submenu_title_text = cls.browser.find_element_by_xpath(
            submenu_title_element).text
        if submenu_title_text == user_name:
            print('登陆成功')
        else:
            print('登陆失败')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_white_single(self):
        browser = self.browser
        # 勾选行李免额，允许退票、允许改期
        browser.find_element_by_id('hasBaggage').click()
        browser.find_element_by_id('allowRefund').click()
        browser.find_element_by_id('allowChange').click()
        # browser.find_element_by_id('depCity').click()
        browser.implicitly_wait(10)
        # 点击搜索button
        browser.find_element_by_xpath('//*[@id="search-box-s"]/div[1]/div[3]/button').click()
        # time.sleep(100)
        browser.implicitly_wait(100)
        # 点击航班详情
        # browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[5]/div[1]/div[4]/span[3]/button').click()

        # browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[5]/div[1]/div[5]/span').click()

        # browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[344]/div/div[3]/span/button').click()
        # browser.back()

        # 点击预订
        browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[5]/div[1]/div[4]/span[1]/button').click()
        # 等待预订界面加载出来
        browser.implicitly_wait(60)
        # 添加常用联系人
        browser.find_element_by_xpath('//*[@id="validateDetailsShow"]/div/div[2]/form/div[2]/div/header/button[1]').click()

        browser.find_element_by_xpath(
            '/html/body/div[23]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span').click()
        browser.find_element_by_xpath('/html/body/div[23]/div/div[2]/div/div[2]/button[1]').click()
        browser.find_element_by_xpath('//*[@id="validateDetailsShow"]/div/div[2]/form/div[3]/div/header/button').click()
        browser.find_element_by_xpath(
            '/html/body/div[26]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[1]/div/label/span').click()
        browser.find_element_by_xpath('/html/body/div[26]/div/div[2]/div/button[1]').click()
        browser.find_element_by_xpath('//*[@id="validateDetailsShow"]/div/div[2]/form/div[7]/button').click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
