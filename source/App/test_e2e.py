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

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test(self):
    # Test name: Test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:8501/")
    # 2 | setWindowSize | 1294x1040 | 
    self.driver.set_window_size(1294, 1040)
    # 3 | mouseDown | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 4 | mouseUp | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 5 | click | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div/div").click()
    # 6 | mouseDown | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 7 | mouseUp | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 8 | click | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[3]/div/div/div/div").click()
    # 9 | mouseDown | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 10 | mouseUp | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 11 | click | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[4]/div/div/div").click()
    # 12 | mouseDown | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 13 | mouseUp | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div/div/div/div | 
    element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div/div/div/div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 14 | click | xpath=//div[@id='root']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/section/div/div[2]/div/div/div/div/div[5]/div/div/div").click()
  
