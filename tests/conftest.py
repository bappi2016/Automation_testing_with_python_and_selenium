"""
@packages: tests->home:
file_name:conftest.py
"""


import pytest
import os
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.yield_fixture()# yield_fixture will run the method twice as setup and teardown
def setUp():
    print("Running Method Level setUp")
    yield
    print("Running Method Level teardown")


@pytest.yield_fixture(scope="class")
#use the scope attribute to determine when the instance of the other
#object is created.
# to automatically called at the starting and in the end
# we can use this fixture or dependency by just inputting  the arguments in any class definition
def oneTimeSetUp(request,browser):#This fixture gets the browser value from another
    # fixture (request and browser) which is reading the command line option.
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    # add driver attribute to the class under test -->
    if request.cls is not None:
        request.cls.driver = driver
    yield driver # to return the driver instance in the test and base class so
    # we can access the driver as a class attribute
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):# Fixture which is reading the command line option.
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")