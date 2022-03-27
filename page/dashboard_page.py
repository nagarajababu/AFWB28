from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Dashboard_Page:

    # Declaration(all elements as private)
    __dashboard = (By.XPATH,"//b[contains(text(),'Dashboard')]")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def verify_dashboard_page_is_displayed(self):
        self.driver.find_element(*self.__dashboard)
