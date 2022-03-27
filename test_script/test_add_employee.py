import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.login_page import Login_Page
from page.dashboard_page import Dashboard_Page
from page.main_page import Main_Page
from page.pim_page import Pim_Page


class Test_Add_employee(BaseTest):

    @pytest.mark.run(order=1)
    def test_Add_employee(self):

#get data from Excel
        un=Excel.get_dat(self.xl_path,"ValidLogin",2,1)
        pw=Excel.get_dat(self.xl_path,"ValidLogin",2,2)
        fn=Excel.get_dat(self.xl_path,"pim",1,2)
        ln=Excel.get_dat(self.xl_path,"pim",2,2)
        eid=Excel.get_dat(self.xl_path,"pim",3,2)
        cun=Excel.get_dat(self.xl_path,"pim",4,2)
        upw=Excel.get_dat(self.xl_path,"pim",5,2)
        psd=Excel.get_dat(self.xl_path,"pim",5,2)

        # 1. enter valied username
        login_page=Login_Page(self.driver)
        login_page.set_username(un)

# 2. enter valid password
        login_page.set_password(pw)

# 3. click login button
        login_page.click_login_button()

# 4. Click on PIM displayed
        main_page = Main_Page(self.driver)
        main_page.click_PIM_button()

#5.  Click on Add Employee
        pim_page = Pim_Page(self.driver)
        pim_page.click_Add_Employee()
        pim_page.set_firestname(fn)
        pim_page.set_lastname(ln)
        pim_page.set_employeeid(eid)
        pim_page.click_createlogin()
        pim_page.set_Username(cun)
        pim_page.set_userpassword(upw)
        pim_page.set_ConfirmPassword(psd)
        pim_page.click_save()
        pim_page.click_Employeelist()
        pim_page.click_Edit()
        pim_page.click_Gender()
        pim_page.click_save()
        v=pim_page.click_SavePersnaldetails()
        print(v)
        self.driver.get_screenshot_as_file(".\\screenshoots1.png")