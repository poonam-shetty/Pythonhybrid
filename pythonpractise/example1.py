import pytest
from selenium import webdriver


driver=webdriver.Chrome("C:\\poonam\\pythonpractise\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")