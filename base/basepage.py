"""
@package: base->pages
file_name:basepage.py

Base pages class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the pages classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)

"""

from base.custom_selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):# Inherit selenium driver

    # Lets create the constructor for the BasePage class,it takes the
    # driver instance and creating the instance of Util class
    def __init__(self,driver):
        """
        Inits BasePage class
        """
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.util = Util # make an instance of Util class and keep the same name as object

    def verifyPageTitle(self,titleToVerify):
        """
        Verify the pages title
        :param titleToVerify: Title on the pages that needs to be verified
        :return:
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle,titleToVerify)
        except:
            self.log.error("Failed to get pages title")
            print_stack()
            return False