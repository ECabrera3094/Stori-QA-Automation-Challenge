import unittest
import xmlrunner
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Locators.Locators import MyLocators
from TestCases.TestCases import MyTestCases


class Stori(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(MyLocators.rootDriver)
        cls.driver.get(MyLocators.URL)
        WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((By.XPATH, MyLocators.XPath_enterMessage)))
        
    def test_Stori(self):
        driver =self.driver
        tc = MyTestCases(driver)
        tc.Challenge()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/EmilianoCabreraPerez/Documents/Python/Stori/Reports')) 
    #unittest.main(xmlrunner.XMLTestRunner(output='/Users/EmilianoCabreraPerez/Documents/Python/Stori/Reports'))