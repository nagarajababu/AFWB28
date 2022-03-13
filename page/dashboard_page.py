from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Dashboard_Page:

    # Declaration(all elements as private)
    __dashboard = (By.XPATH,"//b[contains(text(),'Dashboard')]")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def set_username(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__dashboard))
            print("Home page is displayed")
            return True
        except:
            print("Home page is not diaplayed")
            return False