# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        # make the browser headless - https://pythonbasics.org/selenium-firefox-headless/
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        # brower = webdriver.Firefox(firefox_options=fireFoxOptions)
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Firefox(firefox_options=fireFoxOptions)
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_it_worked(self):
        self.browser.get('http://localhost:8000') # fails if the webserver isn't running
        self.assertIn('Django: the Web framework for perfectionists with deadlines.', self.browser.title)
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')