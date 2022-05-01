from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Dashboard_Page:

    # Declaration(all elements as private)
    __dashboard = (By.XPATH,"//b[contains(text(),'Dashboard')]")
    __welcome = (By.XPATH,"//a[@id='welcome']")
    __logout = (By.XPATH,"//a[contains(text(),'Logout')]")
    __recruitment = (By.XPATH,"//b[contains(text(),'Recruitment')]")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def verify_dashboard_page_is_displayed(self):
        self.driver.find_element(*self.__dashboard)

    def click_welcome(self):
        self.driver.find_element(*self.__welcome).click()

    def click_logout(self):
        self.driver.find_element(*self.__logout).click()

    def click_recruitment(self):
        self.driver.find_element(*self.__recruitment).click()