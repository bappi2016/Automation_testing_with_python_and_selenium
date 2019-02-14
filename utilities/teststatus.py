"""
@package: utilities
file: teststatus.py
In this class we will gonna test a series of test which is a test list and keep
track of all the result without bother others execution and in the end of the test
we will verify if all the test are passed or not ,if a single test failed
then we will verify the hole test as a failure

"""
import logging
from base.custom_selenium_driver import SeleniumDriver
import utilities.custom_logger as cl

class TestStatus(SeleniumDriver): #inherit the class SeleniumDriver

    log = cl.customLogger(logging.INFO)# for log messages
    # Now at first we need the driver instances as a super class instance
    # to initialize the class

    def __init__(self,driver):
        #here the super function is used to gain access to inherited methods-
        #from a parent or sibling class that has been overwritten in a class object
        super(TestStatus,self).__init__(driver)
        self.resultList = [] # create a list for storing all test result

    def sawResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION PASSED :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
                    # And when the test is failed , take a screeshot
                    self.takescreenShot(resultMessage)
            else:
                self.resultList.append("FAILED")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.takescreenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURED :: + " + resultMessage)
            self.takescreenShot(resultMessage)


    def mark(self,result,resultMessage):
        """
        Mark the result of the verification point in a test case

        """
        self.sawResult(result,resultMessage)

    def markFinal(self,testName,result,resultMessage):
        """
        Mark the final result of the verification point in e test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        :param result:
        :param resultMessage:
        :return:
        """

        self.sawResult(result,resultMessage)
        # Now check if the result pass of failed
        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            # Clear the result list
            self.resultList.clear()
            # Assert statement
            assert True == False # Because its a failure test
        else:
            self.log.info(testName + "### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True