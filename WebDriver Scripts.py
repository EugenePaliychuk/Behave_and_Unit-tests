# coding=utf-8
import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = "C:/Users/Evgen/PycharmProjects/Drivers/chromedriver.exe"
firefoxdriver = "C:/Users/Evgen/PycharmProjects/Drivers/geckodriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
os.environ["webdriver.firefox.driver"] = firefoxdriver


class MyTests(TestCase):

    def test_MailBox(self):
        print('Started Successfully')
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        driver.implicitly_wait(25)
        driver.get("https://www.ukr.net/ua/")
        driver.maximize_window()
        element = driver.find_element_by_xpath('.//*[@id=\'user-login-form\']/input[2]')
        element.send_keys("eugenepaliychuk") #Логін
        element = driver.find_element_by_xpath('.//*[@id=\'user-login-form\']/input[3]')
        element.send_keys("julia25") #Пароль
        element = driver.find_element_by_xpath('.//*[@id=\'user-login-form\']/div[2]/div/button').click()# Увійти
        time.sleep(5)
        element = driver.find_element_by_xpath('.//a[@href=\'https://mail.ukr.net/q/start#msglist\']').click() # Листи
        time.sleep(5)
        inbox = (item for item in driver.window_handles if item != driver.current_window_handle).next()
        driver.switch_to.window(inbox)
        element = driver.find_element_by_xpath('//*[@class="compose-message-link"]').click() # Написати Листа
        element = driver.find_element_by_xpath('.//*[@id="sendmsg_form"]/div[1]/div[2]')
        time.sleep(5)
        element.send_keys("blah-blah-blah!!! :) :) :)".decode('utf-8'))
        time.sleep(4)
        element = driver.find_element_by_xpath('.//*[@id="toField"]')
        element.send_keys("julialat10@ukr.net")
        time.sleep(4)
        element = driver.find_element_by_name("subject")
        element.send_keys("лист відправлений роботом".decode('utf-8'))
        time.sleep(4)
        element = driver.find_element_by_name('to').click() # Надіслати
        time.sleep(5)
        print('I Made It')
        driver.quit()

    def test_switchTabs(self):
        print('Started Successfully')
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://www.ukr.net/ua/")
        driver.maximize_window()
        tab1 = driver.find_element_by_class_name('sinoptik').click()
        time.sleep(2)
        tab2 = driver.find_element_by_class_name('currency').click()
        time.sleep(2)
        tab3 = driver.find_element_by_class_name('fuel').click()
        time.sleep(2)
        tab3 = driver.find_element_by_class_name('orakul').click()
        time.sleep(2)
        aries = driver.find_element_by_link_text('Овен').click()
        time.sleep(15)
        print('I Made It')
        driver.quit()

    def test_BusTours(self):
        print('Started Successfully')
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        driver.implicitly_wait(20)
        driver.get("http://www.akkord-tour.com.ua/store.php/lang/ua")
        driver.maximize_window()
        element = driver.find_element_by_xpath('.//*[@id=\'context_str\']')
        time.sleep(5)
        element.send_keys("Іспанія".decode('utf-8'), Keys.RETURN) # Пошук
        time.sleep(5)
        item = driver.find_element_by_link_text('Ніжність іспанського сонця!').click()
        time.sleep(10)
        tour = (item for item in driver.window_handles if item != driver.current_window_handle).next()
        driver.switch_to.window(tour)
        item = driver.find_element_by_id('tab_price').click()
        time.sleep(10)
        print('I Made It')
        driver.quit()

    def test_Dropdowns(self):
        print('Started Successfully')
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://www.bigmir.net/")
        driver.maximize_window()
        dropdown = driver.find_element_by_class_name('b-header-trigger__icon').click()
        time.sleep(2)
        dropdown = driver.find_element_by_xpath('.//a[@href=\'//techno.bigmir.net\']').click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print('I Made It')
        driver.quit()