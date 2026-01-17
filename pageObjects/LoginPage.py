# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class LoginPage:
#     # Login Page
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login_xpath = "//button[@type='submit']"   #//input[@value='Log in']
#     link_logout_linktext = "Logout"  

#     def __init__(self,driver):
#         self.driver=driver

#     btnNoStatistics_xpath = "//div[@id='loadCustomerStatisticsAlert-action-alert']//button[contains(text(),'No')]"

#     def closeCustomerStatisticsPopup(self):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, self.btnNoStatistics_xpath))
#             ).click()
#         except:
#             pass  # popup may not appear every time

#     def setUserName(self, username):
#         self.driver.find_element(By.ID,self.textbox_username_id).clear()
#         self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

#     def setPassword(self, password):
#         self.driver.find_element(By.ID,self.textbox_password_id).clear()
#         self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

#     def clickLogin(self):
#         self.driver.find_element(By.XPATH,self.button_login_xpath).click()

#     def clickLogout(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    btnNoStatistics_xpath = "//div[@id='loadCustomerStatisticsAlert-action-alert']//button[contains(text(),'No')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def setUserName(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_username_id))
        )
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_password_id))
        )
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        login_btn.click()

        # Wait for page transition after login
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Handle popup if it appears
        self.closeCustomerStatisticsPopup()

    def closeCustomerStatisticsPopup(self):
        try:
            popup_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.btnNoStatistics_xpath))
            )
            popup_btn.click()
        except:
            pass  # Popup does not appear every time

    def clickLogout(self):
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext))
        )
        logout_link.click()
