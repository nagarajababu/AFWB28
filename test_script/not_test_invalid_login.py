import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.login_page import Login_Page


class Test_invalid_login(BaseTest):

    def test_invalid_login(self):
        #get data from Excel
        un=Excel.get_dat(self.xl_path,"InvalidLogin",2,1)
        pw=Excel.get_dat(self.xl_path,"InvalidLogin",2,2)

        #enter the invalid username
        login_page=Login_Page(self.driver)
        login_page.set_username(un)
        login_page.set_password(pw)
        login_page.click_login_button()
        result=login_page.verify_err_msg_is_displayed()
        print(result)
        #self.driver.get_screenshot_as_file(".\\screenshoots4.png")
        #enter invalid password
        #click login
        #verify that error message is displayed