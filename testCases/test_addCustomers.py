import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.addcustomerpage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    
    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")
        self.lp.closeCustomerStatisticsPopup()  #for closing the popup if it appears
        # time.sleep(5)

        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("********** Providing customer info **********")

        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setFirstName("John")
        self.addcust.setLastName("Doe")
        self.addcust.setDob("01/01/1990")
        self.addcust.setCompanyName("ABC Corp")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving customer info **********")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True ==True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.error("********** Add Customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
