"""
@packeage : tests->home:
file_name: login_test.py
"""
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

# here we use the two fixtures - ontTimeSetUp and setUP that we have created in conftest
@pytest.mark.usefixtures("oneTimeSetUp","setUp") # for using the fixture inside the class definition
class LoginTests(unittest.TestCase):

    """
    create a fixture method inside the class definition with
    auto use=True to setup another instance object to be used
    throughout your test class.
    """
    @pytest.fixture(autouse=True)
    def build_classSetup(self,oneTimeSetUp):# <-- oneTimeSetup reference here
        # Now we will use the LoginPage instance(because we only need it now) with the fixture,thats why
        #we use the fixture inside the class definition
        self.loginpage = LoginPage(self.driver)# pages object for our test class
        # To use the TestStatus class now we should create an object and instantiate with driver object
        self.test_status = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.loginpage.clearLoginFields()
        self.loginpage.login("test@email.com","abcabc")
        # Now call the mark method of Teststatus Class with parameter result and resultmessage
        result_1 = self.loginpage.verifyLoginTitle()
        self.test_status.mark(result_1,"Title Verification")
        result_2 = self.loginpage.verifyLoginSuccessful()
        self.test_status.markFinal("test_lets kode it",result_2,"Login Verification")



    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.loginpage.login("test@email.com","abc")
        result = self.loginpage.verifyLoginFailed()
        assert result == True











