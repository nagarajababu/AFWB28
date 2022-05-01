from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
class Recruitment_Page:

    # Declaration(all elements as private)
    __candidates = (By.XPATH,"//a[@id='menu_recruitment_viewCandidates']")
    __vacancies = (By.XPATH,"//a[@id='menu_recruitment_viewJobVacancy']")
    __jobtitle = (By.XPATH,"//select[@id='candidateSearch_jobTitle']")
    __jobvacancy = (By.XPATH,"//select[@id='candidateSearch_jobVacancy']")
    __hiringmanager =(By.XPATH,"//select[@id='candidateSearch_hiringManager']")
    __status =(By.XPATH,"//select[@id='candidateSearch_status']")
    __search =(By.XPATH,"//input[@id='btnSrch']")

    # Initialization(using constructor)
    def __init__(self, driver):
        self.driver = driver

    # Utilization(using methods)
    def click_candidates(self):
        self.driver.find_element(*self.__candidates).click()

    def click_vacancies(self):
        self.driver.find_element(*self.__vacancies).click()

    def select_job_title(self):
        job_title = self.driver.find_element(*self.__jobtitle)
        select = Select(job_title)    # Change in future
        select.select_by_index(17)

    def select_Vacancy(self):
        job_vacancy = self.driver.find_element(*self.__jobvacancy)
        select =Select(job_vacancy)
        #select.select_by_index(3)
        select.select_by_value("3")
        #select.select_by_visible_text("agra")

    def select_hiringmanager(self):
        hiringmanager = self.driver.find_element(*self.__hiringmanager)
        select =Select(hiringmanager)
        select.select_by_visible_text("<Paul Collings")

    def select_status(self):
        status = self.driver.find_element(*self.__status)
        select =Select(status)
        select.select_by_value("1")
