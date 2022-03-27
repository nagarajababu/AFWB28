from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Pim_Page:

    # Declaration(all elements as private)
    __PIM = (By.XPATH,"//b[contains(text(),'PIM')]")
    __Addemployee = (By.XPATH,"//a[.='Add Employee']")
    __Firstname = (By.XPATH,"//input[@id='firstName']")
    __Lastname = (By.XPATH,"//input[@id='lastName']")
    __Employeeid =(By.XPATH,"//input[@id='employeeId']")
    __CreateLogin =(By.XPATH,"//input[@id='chkLogin']")
    __Save =(By.XPATH,"//input[@id='btnSave']")
    __UserName =(By.XPATH,"//input[@id='user_name']")
    __Userpassword =(By.XPATH,"//input[@id='user_password']")
    __ConfirmPassword =(By.XPATH,"//input[@id='re_password']")
    __Employeelist =(By.XPATH,"//a[@id='menu_pim_viewEmployeeList']")
    __Edit =(By.XPATH,"//input[@id='btnSave']")
    __Gender =(By.XPATH,"//input[@id='personal_optGender_2']")
    __SavePersonalDetails =(By.XPATH,"//body/div[@id='wrapper']/div[@id='content']/div[@id='employee-details']/div[@id='pdMainContainer']/div[2]/div[1]")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def click_PIM_button(self):
        self.driver.find_element(*self.__PIM).click()

    def click_Add_Employee(self):
        self.driver.find_element(*self.__Addemployee).click()

    def set_firestname(self):
        self.driver.find_element(*self.__Firstname).sendkey()

    def set_firestname(self,fn):
        self.driver.find_element(*self.__Firstname).send_keys(fn)

    def set_lastname(self,ln):
        self.driver.find_element(*self.__Lastname).send_keys(ln)

    def set_employeeid(self,eid):
        self.driver.find_element(*self.__Employeeid).send_keys(eid)

    def click_createlogin(self):
        self.driver.find_element(*self.__CreateLogin).click()

    def set_Username(self,cun):
        self.driver.find_element(*self.__UserName).send_keys(cun)

    def set_userpassword(self,upw):
        self.driver.find_element(*self.__Userpassword).send_keys(upw)

    def set_ConfirmPassword(self,psd):
        self.driver.find_element(*self.__ConfirmPassword).send_keys(psd)

    def click_save(self):
        self.driver.find_element(*self.__Save).click()

    def click_Employeelist(self):
        self.driver.find_element(*self.__Employeelist).click()

    def click_Edit(self):
        self.driver.find_element(*self.__Edit).click()

    def click_Gender(self):
        self.driver.find_element(*self.__Gender).click()

    def click_SavePersnaldetails(self):
        displayedtext =self.driver.find_element(*self.__SavePersonalDetails).is_displayed()
        assert displayedtext is True