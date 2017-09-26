from urllib import localhost
from selenium import webdriver
from unittest import TestCase
import time
from Login_page import Login_page
from Home_page import Home_page
from Add_new_page import Add_New_User
from Delete_user import Delete_user

class AddressBook(TestCase):
    TEST_USER = {'First Name': 'asdasd',
                'Last Name': 'asdasd',
                 'Address': 'asdasdasdasd',
                 }

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_page(self):

        self.driver.get("http://localhost/index.php")

        login = Login_page(self.driver)

        login.user_field("admin")
        login.password_field("admin")
        time.sleep(3)
        login.login_button()
        login.expected_url = "http://localhost/index.php"
        assert self.driver.current_url == login.expected_url, 'current URL is not valid'

    def test_home_page(self):

         self.driver.get("http://localhost/index.php")

         homepage = Home_page(self.driver)

         homepage.home_link()
         homepage.expected_url = "http://localhost/index.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.add_new_link()
         homepage.expected_url = "http://localhost/edit.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.groups_link()
         homepage.expected_url = "http://localhost/group.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.next_birthdays_link()
         homepage.expected_url = "http://localhost/birthdays.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.print_all_link()
         homepage.expected_url = "http://localhost/view.php?all&print"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.print_phones_link()
         homepage.expected_url = "http://localhost/view.php?all&print&phones"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.map_link()
         homepage.expected_url = "http://localhost/map.php?"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.export_link()
         homepage.expected_url = "http://localhost/export.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

         homepage.import_link()
         homepage.expected_url = "http://localhost/import.php"
         assert self.driver.current_url == homepage.expected_url
         time.sleep(1)

    def test_add_new_user(self):

          self.driver.get("http://localhost/index.php")
          user = self.TEST_USER
          user['email'] = 'TestUser-{}@mail.com'.format(randomstring(23))
          userdata = Add_New_User(self.driver)

          userdata.edit_add_new()
          time.sleep(1)
          userdata.input_field("Fernando")
          userdata.input_field(self.TEST_USER['First Name'])
          time.sleep(1)
          userdata.next_button()
          time.sleep(1)
          userdata.last_name_field("Diaz")
          time.sleep(1)
          userdata.title_field("CFO")
          time.sleep(1)
          userdata.company_field("Procter&Gamble")
          time.sleep(1)
          userdata.address_field2("Illinois")
          time.sleep(1)
          userdata.home_telephone_field("+188800629")
          time.sleep(1)
          userdata.enter_button()
          userdata.expected_url = "http://localhost/edit.php"
          assert self.driver.current_url == userdata.expected_url
          time.sleep(1)
          userdata.expexted_name = self.driver.find_element_by_xpath('.//*[@id="maintable"]/tbody/tr[2]/td[3]').getText()
          current_users = [{}]

          assert userdata.expexted_name == "Diaz Fernando"

    def test_delete_user(self):

        self.driver.get("http://localhost/index.php")

        login = Login_page(self.driver)

        login.user_field("admin")
        login.password_field("admin")
        login.login_button()
        remove = Delete_user(self.driver)

        remove.checkbox()
        time.sleep(1)
        remove.delete_button()
        home_page = Home_page(self.driver)

        # users_table = self.driver.find_element_by_xpath('.//*[@id="maintable"]')
        users = home_page.users_table.get_all_users()
        emails = [existing_user['All E-mail'] for existing_user in users]
        assert 'fernando.diaz@procter&gamble'['email'] not in emails


    def tearDown(self):
        self.driver.quit()
