from selenium.webdriver.common.by import By


class User_Leave_page:

        # Declaration(all elements as private)
    __Apply = (By.XPATH, "//a[@id='menu_leave_applyLeave']")
    __Addemployee = (By.XPATH, "//a[.='Add Employee']")
    __Firstname = (By.XPATH, "//input[@id='firstName']")
    __Lastname = (By.XPATH, "//input[@id='lastName']")

        # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def __Apply(self):
        self.driver.find_element(*self.__Apply).click()

    
