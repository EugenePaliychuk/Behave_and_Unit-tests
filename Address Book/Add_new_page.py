from selenium import webdriver

class Add_New_User(object):

    def __init__(self, driver):
        self.driver = driver

    def edit_add_new(self):
        self.driver.find_element_by_link_text('add new').click()

    def input_field(self, inputfield):
        self.driver.find_element_by_xpath('.//*[@name="address"]').send_keys(inputfield)

    def next_button(self):
        self.driver.find_element_by_xpath('.//*[@id=?"content"]/form/input[1]').click()

    def address_field1(self, addressInfo1):
        self.driver.find_element_by_xpath('.//*[@name="address"]').send_keys(addressInfo1)

    def first_name_field(self, firstName):
        self.driver.find_element_by_xpath('.//*[@name="firstname"]').send_keys(firstName)

    def middle_name_field(self, middleName):
        self.driver.find_element_by_xpath('.//*[@name="middlename"]').send_keys(middleName)

    def last_name_field(self, lastName):
        self.driver.find_element_by_xpath('.//*[@name="lastname"]').send_keys(lastName)

    def nickname_field(self, nickName):
        self.driver.find_element_by_xpath('.//*[@name="nickname"]').send_keys(nickName)

    def photo_browse_button(self):
        self.driver.find_element_by_xpath('.//*[@name="photo"]').click()

    def title_field(self, titleData):
        self.driver.find_element_by_xpath('.//*[@name="title"]').send_keys(titleData)

    def company_field(self, companyData):
        self.driver.find_element_by_xpath('.//*[@name="company"]').send_keys(companyData)

    def address_field2(self, addressInfo2):
        self.driver.find_element_by_xpath('.//*[@name="address"]').send_keys(addressInfo2)

    def home_telephone_field(self, homeNum):
        self.driver.find_element_by_xpath('.//*[@name="home"]').send_keys(homeNum)

    def mobile_telephone_field(self, mobileNum):
        self.driver.find_element_by_xpath('.//*[@name="mobile"]').send_keys(mobileNum)

    def work_telephone_field(self, workNum):
        self.driver.find_element_by_xpath('.//*[@name="work"]').send_keys(workNum)

    def fax_telephone_field(self, faxNum):
        self.driver.find_element_by_xpath('.//*[@name="fax"]').send_keys(faxNum)

    def email_field1(self, emailData1):
        self.driver.find_element_by_xpath('.//*[@name="email"]').send_keys(emailData1)

    def email_field2(self, emailData2):
        self.driver.find_element_by_xpath('.//*[@name="email2"]').send_keys(emailData2)

    def email_field3(self, emailData3):
        self.driver.find_element_by_xpath('.//*[@name="emai3"]').send_keys(emailData3)

    def homepage_field(self, homepageData):
        self.driver.find_element_by_xpath('.//*[@name="homepage"]').send_keys(homepageData)

    def enter_button(self):
        self.driver.find_element_by_xpath('.//*[@name="submit"]').click()
