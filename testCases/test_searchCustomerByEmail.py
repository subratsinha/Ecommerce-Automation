import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.addcustomerpage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Test_004_SearchCustomerByEmail **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Search Customer By Email Test **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Searching Customer by Email ID **********")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("jhon@nopcommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("jhon@nopcommerco.com")
        assert True == status
        self.logger.info("********** Search Customer By Email Test Finished **********")
        self.driver.close()