# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTesting1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testing1(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(976, 884)
    self.driver.find_element(By.ID, "searchBox").click()
    self.driver.find_element(By.ID, "searchBox").send_keys("dress")
    self.driver.find_element(By.ID, "searchBox").send_keys(Keys.ENTER)
  
