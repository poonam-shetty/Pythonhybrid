import pytest
from pageObject.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.loginpage1 import LoginPage
import os


class Test_Login():
    baseURL= "http://demo.opencart.com/"
    logger=LogGen.loggen()

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    # @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("***** starting test_002_login****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()


        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login")
            assert False

        self.driver.close()
        self.logger.info(" ***End of test_002_login ****")


