# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time


class test_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.set_window_size(1366, 768)


    def test1(self):
        driver = self.driver
        self.driver.get("https://time.sc")
        #Change language, because of bug, that I reported earlier
        driver.find_element_by_css_selector(".landing__lang-variant.landing__lang-variant--en.landing__lang-variant--active").click()
        driver.find_element_by_css_selector(".landing__lang-variant.landing__lang-variant--rus").click()
        #Click Sign In
        driver.find_element_by_css_selector(".landing__enter-popup").click()
        time.sleep(2)
        #Put data into e-mail and password fields
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/div/div/div/div/form/div[1]/div[1]/label/input").send_keys("skdev10@mail.ru")
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/div/div/div/div/form/div[1]/div[2]/label/input").send_keys("skdev123")
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/div/div/div/div/form/div[4]/button").click()
        time.sleep(5)
        #Close menu Locations
        driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[3]/div[1]").click()
        time.sleep(2)
        #Click at Profile and Settings
        driver.find_element_by_xpath("html/body/div[2]/div[3]/div/div/div[4]/div[1]").click()
        time.sleep(2)
        #Click Edit
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[3]/div[3]/a[1]").click()
        time.sleep(2)
        #Insert new data
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[1]/label/input").send_keys("123")
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/label/input").send_keys('456')
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/div/button[2]").click()
        time.sleep(2)
        #make assert to shure that changes were saved
        self.assertEqual("tester123 tester456", driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[3]/div[1]/div[1]/div[2]").text)
        #make all data as it was at the begining, for next tests
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[3]/div[3]/a[1]").click()
        time.sleep(2)
        #Insert old data
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[1]/label/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[1]/label/input").send_keys("tester")
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/label/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/label/input").send_keys('tester')
        driver.find_element_by_xpath("html/body/div[2]/div[5]/div/div[2]/div/div[2]/div/button[2]").click()



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()