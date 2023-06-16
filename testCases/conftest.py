import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions,Chrome
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture()
def setup():
    service_obj=Service("C:\\poonam\\pythonpractise\\chromedriver.exe")
    driver=webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    return driver
    

# @pytest.fixture()
# def setup(browser):
#     if browser=='edge':
#         driver=webdriver.Edge(EdgeChromiumDriverManager().install())
#         print("Launching Edge Browser....")



#     elif browser=='firefox':
#         driver=webdriver.Firefox(GeckoDriverManager().install())
#         print("Launching firefox browser......")
#     else:
#         driver=webdriver.Chrome(ChromeDriverManager().install())
#         print("Launching Chrome browser...")

# def pytest_adoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
