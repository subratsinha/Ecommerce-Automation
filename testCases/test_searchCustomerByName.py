import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.addcustomerpage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Test_005_SearchCustomerByName **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Search Customer By Name Test **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Searching Customer by Name **********")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("jhon")
        self.searchcust.setLastName("deo")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByName("jhon deo")
        assert True == status
        self.logger.info("********** Search Customer By Name Test Finished **********")
        self.driver.close()