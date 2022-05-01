from generic.base_test import BaseTest
from generic.excel import Excel
from page import login_page
from page.leave_page import Leave_Page


class Test_Apply_Leave(BaseTest):

    def test_apply_leave(self):
        # get data from Excel
        un = Excel.get_dat(self.xl_path, "ValidLogin", 2, 1)
        pw = Excel.get_dat(self.xl_path, "ValidLogin", 2, 2)

        leave_page = Leave_Page(self.driver)
        login_page.set_username(un)
        login_page.set_password(pw)
        leave_page.click_Apply()
        leave_page.set_LeaveType()
