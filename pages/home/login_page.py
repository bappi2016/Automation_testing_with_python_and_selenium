"""
@packages: pages->home:
file_name:login_page
"""


import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):# Inherit BasePage as parent class or super class
    log = cl.customLogger(logging.DEBUG)

    # make a constructor with driver instance
    def __init__(self, driver):
        #initialize the parent class with driver object
        super().__init__(driver) # super is used to return a proxy object and here driver is the argument
        #that is used as the object of the init method
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):# make optional arguments for making different scenario
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("gravatar",locatorType="class")
        return result
    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",locatorType="xpath")
        return result
    def clearLoginFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("google")

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)
    #
    # def clickLoginLink(self):
    #     self.getLoginLink().click()
    #
    # def enterEmail(self, email):
    #     self.getEmailField().send_keys(email)
    #
    # def enterPassword(self, password):
    #     self.getPasswordField().send_keys(password)
    #
    # def clickLoginButton(self):
    #     self.getLoginButton().click()

