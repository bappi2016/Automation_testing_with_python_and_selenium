"""
@package utilities
file_name : util.py
Util class implementation

All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()

"""

import time
import traceback
import random,string
import utilities.custom_logger as cus_log
import logging

class Util(object): # New style class definition , where directly inherit
    # form object as base class
    log = cus_log.customLogger(logging.INFO)

    def sleep(self,sec,info = ""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '"+ str(sec)+ "'seconds for "+ info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self,length,type="letters"):
        """
        Get random string of characters
        :param length: Length of string,number of characters string should have
        :param type:Type of characters string should have.Default is letters
        :return: lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self,charCount=10): # default char count =10
        return self.getAlphaNumeric(charCount,'lower')# will return an alphanumeric name with default char 10 and in lower case

    def getUniqueNameList(self,listSize=5,itemLength=None):
        """
        Get a list of valid email ids
        :param listSize: Number of names.Default is 5 names in a list
        :param itemLength: It should be a list containing number of items equal to the
        list size
        :return: the length of the each item in the list -> [1,2,3,4,5]
        """
        nameList = [] # initially empty
        for i in range(0,listSize): # Create a loop to append name in the nameList
            nameList.append(self.getUniqueName(itemLength[i]))# will generate a namelist of requered item
            return nameList

    def verifyTextContains(self,actualText,expectedText):
        """
        Verify actual text contains with expected text string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI--> ::" + actualText)
        self.log.info("Expected Text From Application Web UI-->::" + expectedText)
        if expectedText.lower() in actualText.lower(): # partial match with substring
            self.log.info("### TEXT VERIFICATION PASSED !!!")
            return True
        else:
            self.log.info("### TEXT VERIFICATION DOESN'T PASSED ")
            return False

    def verifyTextMatch(self,actualText,expectedText):
        """
        verify text match
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI--> ::" +actualText)
        self.log.info("Expected Text From Application Web UI-->::" + expectedText)
        if actualText.lower()== expectedText.lower():
            self.log.info("### TEXT VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### TEXT VERIFICATION DOES NOT MATCHED ")
            return False

    # For exact match
    def verifyListMatch(self,expectedList,actualList):
        """
        verify two list matches
        :param expectedList: Expected List
        :param actualList: Actual List
        :return:
        """
        return set(expectedList) == set(actualList) # By using built-in function set()

    def verifyListContains(self,expectedList,actualList): # For partial match
        """
        Verify actual list contains elements of expected list
        :param expectedList:
        :param actualList:
        :return:
        """
        length = len(expectedList)
        for i in range(0,length): # from o index to length of the string
            if expectedList[i] not in actualList:# if not match
                return False
            else:
                return True



