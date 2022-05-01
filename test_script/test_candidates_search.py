import time

import pytest
from generic.base_test import BaseTest
from generic.excel import Excel
from page.login_page import Login_Page
from page.dashboard_page import Dashboard_Page
from page.recruitment_page import Recruitment_Page


class Test_Candidates_Search(BaseTest):
    def test_candidates_search(self):

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

# 4. Verify that home page is displayed
        dashboard_page = Dashboard_Page(self.driver)
        dashboard_page.click_recruitment()

        recruitment_page = Recruitment_Page(self.driver)
        recruitment_page.click_candidates()
        time.sleep(2)
        recruitment_page.select_job_title()
        time.sleep(2)
        recruitment_page.select_Vacancy()
        time.sleep(2)
        recruitment_page.select_hiringmanager()
        time.sleep(2)
        recruitment_page.select_status()
        time.sleep(10)
       # recruitment_page.click_vacancies()