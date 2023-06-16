from pageObject.HomePage import HomePage
from pageObject.AccountRegistrationPage import AccountRegistrationPage
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen




class Test_001_Account:
    baseURL="http://demo.opencart.com/"
    logger=LogGen.loggen() #for logging





    def test_account_reg(self,setup): 
        self.logger.info("**** test_001_Account started**")
        self.driver=setup

        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing customer details for registration")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.regpage.setEmail("abc0951776091@gmail.com")
        self.regpage.setPassword("abcxyz")
        self.regpage.clickSubscribe()
        time.sleep(10)
        self.regpage.clickAgreeContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account registration is passed")
            assert True
            self.driver.close()
        else:
            # capturing screenshot
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account registartion is failed")
            self.driver.close()
            assert  False
        self.logger.info("*** test_001_Account finished**")  


