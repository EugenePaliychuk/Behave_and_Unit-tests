from selenium import webdriver

class Delete_user(object):

    def __init__(self, driver):
        self.driver = driver

    def checkbox(self):
        self.driver.find_element_by_xpath('.//*[@id="12"]').click

    def delete_button(self):
        self.driver.find_element_by_xpath('.//*[@value="Delete"]').click

