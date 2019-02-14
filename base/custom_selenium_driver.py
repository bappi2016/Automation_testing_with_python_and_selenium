"""
@packeage :base->pages
file_name: custom_selenium_driver
"""

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def takescreenShot(self,resultMessage):
        """
        Takes screen shot of the current open web pages
        :param resultMessage:
        :return:
        """
        # At first create a file name for the screenshot file with the specific result messages
        filename = resultMessage + "." + str(round(time.time() * 1000))+ ".png"
        screenshotDirectory = "/home/bappi/Documents/workspace_python/Automation_framework/screenshots/"
        # First we need to Find the current directory where our script is located
        currentDirectory = os.path.dirname(__file__)
        # Because we need to append our filename to the screen shot directory,
        #in order to get the real file, so temporaly lets put it somewhere in order to find it with path variable
        filePath = screenshotDirectory + filename
        # To get the actual file we have to show the computer the where the destination file located
        destinationPath = os.path.join(currentDirectory,filePath)
        # Now get the destination directory
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationPath)
            self.log.info("Screenshot save to directory " + destinationPath)
        except:
            self.log.error("### Exception Occurred")
            print_stack()


    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElementList(self,locator,locatorType="id"):
        """

        :param locator: name of the locator
        :param locatorType: Type of the locator
        :return: list of elements
        """
        element = None # initially List is empty
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType,locator)
            self.log.info("Element List found with locator: " + locator +
                          "and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: "+ locator+
                          "and locatorType: "+ locatorType)
        return element

    def elementClick(self, locator, locatorType="id",element = None):
        # Either provide element or a combination of locator and locatorType
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id",element=None):
        # Either provide element or a combination of locator and locatorType
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: "
                          + locator + " locatorType: " + locatorType)
            print_stack()

    def getText(self,locator="",locatorType="id",element=None,info=""):
        """
        Get text on an element
        :param locator: locator name of the element which text we wanna find
        :param locatorType:
        :param element: if we explicitly given an element as argument to find its text
        :param info: partial information about the text
        :return: Text on the element
        """
        try:
            if locator: # If locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator,locatorType)
            self.log.debug("Before finding text")
            text = element.text # helping method provided by selenium to find the text in an element
            self.log.debug("After finding element,The text size is: "+ str(len(text)))
            if len(text)==0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + " '")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element" + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator, locatorType="id",element = None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self,locator="",locatorType="id",element=None):

        isDisplayed = False # assume there is not element in the display
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            if element is not None:
                isDisplayed = element.is_displayed() # boolean statement
                self.log.info("Element is displayed with locator: "+ locator +
                              "locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              "locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False


    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web pages")
        except:
            self.log.info("Element not appeared on the web pages")
            print_stack()
        return element

    def scrollPage(self,direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0,-1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
