from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions,Chrome



class AccountRegistrationPage():
    txt_firstname_xpath="//input[@id='input-firstname']"
    txt_lastname_xpath="//input[@name='lastname']"
    txt_email_xpath="//input[@name='email']"
    txt_password_xpath="//input[@type='password']"
    radioBtn_Subscribe_xpath="(//input[@type='radio'])[2]"
    check_agree_xpath= "agree"
    btn_continue_xpath="//button[text()='Continue']"
    text_privacy_xpath="//a[text()='Privacy Policy']"
    
    def __init__(self,driver):
        self.driver=driver


    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
   
    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickSubscribe(self):
        self.driver.find_element(By.XPATH,self.radioBtn_Subscribe_xpath).click()

    def clickAgreeContinue(self):
        element=self.driver.find_element(By.NAME,self.check_agree_xpath)
        self.driver.execute_script("arguments[0].click();",element)

    def clickContinueBtn(self):
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH,self.btn_continue_xpath))

    def getconfirmationmsg(self):
        try:
             return self.driver.find_element(By.XPATH,self.text_privacy_xpath).text
        except:
             None

    
