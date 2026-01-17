import pytest
from pageObjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\loginData.xlsx"
    # username = ReadConfig.getUseremail()  #Not needed in DDT
    # password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Verifying Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)


        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        lst_status = []             # Empty list variable to store the status of each login attempt
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Passed Test Case for user: " + self.user + " **********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.error("********** Failed Test Case for user: " + self.user + " **********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.error("********** Failed Test Case for user: " + self.user + " **********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********** Passed Test Case for user: " + self.user + " **********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********** DDT Login Test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********** DDT Login Test Failed **********")
            self.driver.close()
            assert False
        self.logger.info("********** Completed TC_LoginDDt_002 **********")
                    

        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # act_title = self.driver.title
        # if act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.logger.info("********** Login Test is Passed **********")
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        #     self.logger.error("********** Login Test is Failed **********")
        #     self.driver.close()
        #     assert False