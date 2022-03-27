from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Main_Page:

    # Declaration(all elements as private)
    __PIM = (By.XPATH,"//b[contains(text(),'PIM')]")
    __Leave = (By.XPATH, "//b[contains(text(),'Leave')]")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def click_PIM_button(self):
        self.driver.find_element(*self.__PIM).click()

    def click_Leave_button(self):
        self.driver.find_element(*self.__Leave).click()