import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.login_page import Login_Page
from page.dashboard_page import Dashboard_Page

class Test_Valid_Login(BaseTest):

    @pytest.mark.run(order=1)
    def test_valid_login(self):

#get data from Excel
        un=Excel.get_dat(self.xl_path,"ValidLogin",2,1)
        pw=Excel.get_dat(self.xl_path,"ValidLogin",2,2)

        # 1. enter valied username
        login_page=Login_Page(self.driver)
        login_page.set_username(un)

# 2. enter valid password
        login_page.set_password(pw)

# 3. click login button
        login_page.click_login_button()

#    verify
# 4. Verify that home page is displayed
        dashboard_page=Dashboard_Page(self.driver)
        result=dashboard_page.verify_dashboard_page_is_displayed(self.wait)
        assert result