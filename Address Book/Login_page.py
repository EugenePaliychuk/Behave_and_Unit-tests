from selenium import webdriver

class Login_page(object):

    def __init__(self,driver):
        self.driver = driver

    def user_field(self,username):
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)

    def password_field(self, password):
        self.driver.find_element_by_name("pass").clear()
        self.driver.find_element_by_name("pass").send_keys(password)

    def login_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

