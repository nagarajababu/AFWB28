from generic.base_test import BaseTest
from page.login_page import Login_Page
from page.dashboard_page import Dashboard_Page
class Test_Valid_Login(BaseTest):

    def test_valid_login(self):
# 1. enter valied username
        login_page=Login_Page(self.driver)
        login_page.set_username("Admin")

# 2. enter valid password
        login_page.set_password("admin123")

# 3. click login button
        login_page.click_login_button()

# 4. Verify that home page is displayed
        dashboard_page=Dashboard_Page(self.driver)
        result=dashboard_page.verify_dashboard_page_is_displayed(self.wait)
        assert result