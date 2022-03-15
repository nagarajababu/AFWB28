import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#driver---> local variable
#self.driver ---> globle variable

class BaseTest:

    @pytest.fixture(autouse=True)
    def open_close_app(self):

        # create object of the properties open and load
        p_file = Properties()
        p_file.load(open("config.properties"))

        # make xl file as global file
        self.xl_path = p_file['XLPATH']
        #open the browser

        #1 driver=webdriver.Chrome("./../driver/chromedriver.exe")
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #2 Maximize browser
        self.driver.maximize_window()

        # Implicit wait and get from properties file
        ito=p_file['ITO']
        self.driver.implicitly_wait(ito)

        # Explicit wait and get from properties file
        eto=p_file['ETO']
        self.wait=WebDriverWait(self.driver,eto)

        #3 enter the URL
        url=p_file['URL']
        self.driver.get(url)
        #self.driver.get("https://opensource-demo.orangehrmlive.com/")

        # Last, Go, run the test and comes back
        yield

        #Close the browser
        self.driver.close()