"""
@package base->pages:
file_name:webdriverfactory.py
WebDriver factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
import os
from selenium import webdriver
class WebDriverFactory():
    def __init__(self,browser): # __init__ constructor
        """
        Here we construct the init method with browser arguments because we will use this method in another class method
        Inits WebDriverFactory class
        :param browser:
        Returns:
        None
        """
        self.browser = browser


    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration
        :return: WebDriver Instance
        """
        baseURL = "https://learn.letskodeit.com"
        if self.browser == "iexplorar":
            # Set InterNet Explorar
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            # Set Firefox
            driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
            # Instantiate Firefox Browser Command
            driver = webdriver.Firefox(executable_path=driverlocation)
            driver = webdriver.Firefox()
        else:
            # Set chrome driver
            # At First We Have To Show The Path Where Is The Cromedriver Located
            # Set chrome driver environment based on OS
            driverlocation = "/usr/local/bin/chromedriver"
            # Now we have to set the environment variable for chrome
            os.environ["webdriver.chrome.driver"] = driverlocation
            driver = webdriver.Chrome()
        # Setting Driver Implicit Time out for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver


