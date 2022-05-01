from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Leave_Page:

    # Declaration(all elements as private)
    __Entitlements = (By.XPATH,"//a[@id='menu_leave_Entitlements']")
    __AddLeaveEntitlement = (By.XPATH,"//a[@id='menu_leave_addLeaveEntitlement']")
    __Employee = (By.XPATH,"//input[@id='entitlements_employee_empName']")
    __LeaveType = (By.XPATH,"//select[@id='entitlements_leave_type']")
    __SelectLeaveType = (By.XPATH,"//option[contains(text(),'CAN - Vacation')]")
    __Entitlement = (By.XPATH,"//input[@id='entitlements_entitlement']")
    __SaveButton =(By.XPATH,"//input[@id='btnSave']")
    __Apply = (By.XPATH, "//a[@id='menu_leave_applyLeave']")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def click_Entitlements_Button(self):
        self.driver.find_element(*self.__Entitlements).click()

    def click_Add_Leave_Entitlement(self):
        self.driver.find_element(*self.__AddLeaveEntitlement).click()

    def click_Employee(self, fn):
         self.driver.find_element(*self.__Employee).send_keys(fn)

    def set_LeaveType(self):
        self.driver.find_element(*self.__LeaveType).click()

    def click_SelectLeaveType(self):
        self.driver.find_element(*self.__SelectLeaveType).click()

    def set_Entitlement(self,en):
        self.driver.find_element(*self.__Entitlement).send_keys(en)

    def click_save(self):
        self.driver.find_element(*self.__SaveButton).click()

    def click_Apply(self):
        self.driver.find_element(*self.__Apply).click()