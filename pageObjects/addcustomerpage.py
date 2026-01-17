# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# class AddCustomerPage:
#     # Add Customer Page Locators
#     lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"                                                           #"//a[@href='#']//p[contains(text(),'Customers')]" 
#     lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"                                    #"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
#     btnAddnew_xpath = "//a[@class='btn btn-primary']"

#     txtEmail_xpath = "//input[@id='Email']"
#     txtPassword_xpath = "//input[@id='Password']"

#     txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
#     lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
#     lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
#     lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
#     lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
#     drpmgrOfVendor_xpath = "//select[@id='VendorId']"

#     txtFirstName_xpath = "//input[@id='FirstName']"
#     txtLastName_xpath = "//input[@id='LastName']"
#     rdMaleGender_id = "Gender_Male"
#     rdFemaleGender_id = "Gender_Female"
#     textfirstname_xpath = "//input[@id='FirstName']"
#     textlastname_xpath = "//input[@id='LastName']"
#     txtDob_xpath = "//input[@id='DateOfBirth']"
#     txtCompanyName_xpath = "//input[@id='Company']"
#     txtAdminContent_xpath = "//textarea[@id='AdminComment']"
#     btnSave_xpath = "//button[@name='save']"
    

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 30)
    
#     def clickOnCustomersMenu(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menu_xpath))).click()
#         # self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
    
#     def clickOnCustomersMenuItem(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menuitem_xpath))).click()
#         # self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
    
#     def clickOnAddnew(self):
#         self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

#     def setEmail(self, email):
#         self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

#     def setPassword(self, password):
#         self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

#     def setCustomerRoles(self, role):
#         self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
#         time.sleep(3)
#         if role == 'Administrators':
#             self.driver.find_element(By.XPATH, "//span[@title='delete']").click()  # Remove default selection
#             self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
#         elif role == 'Guests':
#             self.driver.find_element(By.XPATH, "//span[@title='delete']").click()  # Remove default selection
#             self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
#         elif role == 'Registered':
#             self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
#         elif role == 'Vendors':
#             self.driver.find_element(By.XPATH, "//span[@title='delete']").click()  # Remove default selection
#             self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
#         else:
#             self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

#         time.sleep(3)
#         # Use JavaScript to click on the list item
#         self.driver.execute_script("arguments[0].click();", self.listitem)

#     def setManagerOfVendor(self, value):
#         drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
#         drp.select_by_visible_text(value)

#     def setGender(self, gender):
#         if gender == 'Male':
#             self.driver.find_element(By.ID, self.rdMaleGender_id).click()
#         elif gender == 'Female':
#             self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
#         else:
#             self.driver.find_element(By.ID, self.rdMaleGender_id).click()  # Default

#     def setFirstName(self, fname):
#         self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

#     def setLastName(self, lname):
#         self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

#     def setDob(self, dob):
#         self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

#     def setCompanyName(self, comname):
#         self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

#     def setAdminContent(self, content):
#         self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

#     def clickOnSave(self):
#         self.driver.find_element(By.XPATH, self.btnSave_xpath).click()









class AddCustomerPage:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[contains(@class,'btn-primary')]"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    roleDelete_xpath = "//span[@title='delete']"


    roleAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    roleRegistered_xpath = "//li[contains(text(),'Registered')]"
    roleGuests_xpath = "//li[contains(text(),'Guests')]"
    roleVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpVendor_xpath = "//select[@id='VendorId']"

    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMale_id = "Gender_Male"
    rdFemale_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompany_xpath = "//input[@id='Company']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"

    overlay_xpath = "//div[contains(@class,'modal-backdrop')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    # ---------- Helpers ----------
    def _wait_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _wait_send_keys(self, locator, value):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(value)

    def _wait_overlay_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.overlay_xpath)))

    # ---------- Actions ----------
    def clickOnCustomersMenu(self):
        self._wait_click((By.XPATH, self.lnkCustomers_menu_xpath))

    def clickOnCustomersMenuItem(self):
        self._wait_click((By.XPATH, self.lnkCustomers_menuitem_xpath))

    def clickOnAddnew(self):
        self._wait_click((By.XPATH, self.btnAddnew_xpath))

    def setEmail(self, email):
        self._wait_send_keys((By.XPATH, self.txtEmail_xpath), email)

    def setPassword(self, password):
        self._wait_send_keys((By.XPATH, self.txtPassword_xpath), password)

    def setCustomerRoles(self, role):
        self._wait_overlay_to_disappear()
        # Open the roles multiselect
        self._wait_click((By.XPATH, self.txtCustomerRoles_xpath))

        # Remove default selection if present
        try:
            delete_btn = self.driver.find_element(By.XPATH, self.roleDelete_xpath)
            if delete_btn.is_displayed():
                delete_btn.click()
        except Exception:
            pass

        role_map = {
            "Administrators": self.roleAdministrators_xpath,
            "Registered": self.roleRegistered_xpath,
            "Guests": self.roleGuests_xpath,
            "Vendors": self.roleVendors_xpath
        }

        role_xpath = role_map.get(role, self.roleGuests_xpath)
        # Wait until the option is clickable then click via JS (handles overlay/scroll issues)
        role_elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, role_xpath)))
        try:
            self.driver.execute_script("arguments[0].click();", role_elem)
        except Exception:
            # fallback to direct click
            role_elem.click()

    def setManagerOfVendor(self, vendor):
        Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, self.drpVendor_xpath)))) \
            .select_by_visible_text(vendor)

    def setGender(self, gender):
        if gender == "Female":
            self._wait_click((By.ID, self.rdFemale_id))
        else:
            self._wait_click((By.ID, self.rdMale_id))

    def setFirstName(self, fname):
        self._wait_send_keys((By.XPATH, self.txtFirstName_xpath), fname)

    def setLastName(self, lname):
        self._wait_send_keys((By.XPATH, self.txtLastName_xpath), lname)

    def setDob(self, dob):
        self._wait_send_keys((By.XPATH, self.txtDob_xpath), dob)

    def setCompanyName(self, cname):
        self._wait_send_keys((By.XPATH, self.txtCompany_xpath), cname)

    def setAdminContent(self, comment):
        self._wait_send_keys((By.XPATH, self.txtAdminComment_xpath), comment)

    def clickOnSave(self):
        self._wait_overlay_to_disappear()
        self._wait_click((By.XPATH, self.btnSave_xpath))
