import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.leave_page import Leave_Page
from page.login_page import Login_Page
from page.dashboard_page import Dashboard_Page
from page.main_page import Main_Page
from page.pim_page import Pim_Page


class Test_Leave_employee(BaseTest):

    @pytest.mark.run(order=2)
    def test_Leave_employee(self):

#get data from Excel
        un=Excel.get_dat(self.xl_path,"ValidLogin",2,1)
        pw=Excel.get_dat(self.xl_path,"ValidLogin",2,2)
        fn=Excel.get_dat(self.xl_path,"pim",1,2)
        ln=Excel.get_dat(self.xl_path,"pim",2,2)
        eid=Excel.get_dat(self.xl_path,"pim",3,2)
        cun=Excel.get_dat(self.xl_path,"pim",4,2)
        upw=Excel.get_dat(self.xl_path,"pim",5,2)
        psd=Excel.get_dat(self.xl_path,"pim",5,2)
        en=Excel.get_dat(self.xl_path,"pim",6,2)

        # 1. enter valied username
        login_page=Login_Page(self.driver)
        login_page.set_username(un)

# 2. enter valid password
        login_page.set_password(pw)

# 3. click login button
        login_page.click_login_button()

# 4. Click on Leave displayed
        main_page = Main_Page(self.driver)
        main_page.click_Leave_button()

#5.  Click on Add Employee
        leave_page = Leave_Page(self.driver)
        leave_page.click_Entitlements_Button()
        leave_page.click_Add_Leave_Entitlement()
        leave_page.click_Employee(fn)
        leave_page.set_LeaveType()
        leave_page.click_SelectLeaveType()
        leave_page.set_Entitlement(en)
        leave_page.click_save()
        self.driver.get_screenshot_as_file(".\\screenshoots5.png")