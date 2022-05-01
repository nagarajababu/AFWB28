from generic.base_test import BaseTest
from generic.excel import Excel


class Test_Demo1(BaseTest):

    def test_demo1(self):
        print(self.driver.title)
        x = Excel.get_dat(self.xl_path, "Sheet3", 1,1)
        #n=Excel.get_data("./data/input.xlse","Sheet1",1,1)
        #v=Excel.get_dat("./data/input.xlsx","Sheet1",1,2)

        print("from excel:",x)
        self.driver.get_screenshot_as_file(".\\screenshoots3.png")