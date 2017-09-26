from selenium import webdriver
from lxml import etree

class Home_page(object):

    def __init__(self, driver):
        self.driver = driver
        self.users_table = Users_table(driver)

    def home_link(self):
        self.driver.find_element_by_link_text("home").click()

    def add_new_link(self):
        self.driver.find_element_by_link_text("add new").click()

    def groups_link(self):
        self.driver.find_element_by_link_text("groups").click()

    def next_birthdays_link(self):
        self.driver.find_element_by_link_text("next birthdays").click()

    def print_all_link(self):
        self.driver.find_element_by_link_text("print all").click()

    def print_phones_link(self):
        self.driver.find_element_by_link_text("print phones").click()

    def map_link(self):
        self.driver.find_element_by_link_text("map").click()

    def export_link(self):
        self.driver.find_element_by_link_text("export").click()

    def import_link(self):
        self.driver.find_element_by_link_text("import").click()


class Users_table(object):

    contacts = """<table>
    <tr> <th>Photo</th> <th>Name</th> <th>Address</th> <th>All E-mail</th> <th>All phones</th> </tr>
    <tr> <td></td> <td>Diaz Fernando</td> <td>Illinois</td> <td>fernando.diaz@procter&gamble</td> <td>+188800629</td> </tr>
    <tr> <td></td> <td>Might Gregory</td> <td>NY</td> <td>gregory.might@general-electric</td> <td>18883180062</td>
    </table>
    """

 n n     def __init__(self, driver):
        self.driver = driver


    def get_all_users(self):
        # contacts = self.driver.find_element_by_id('maintable')
        # rows = contacts.find_elements_by_tag_name('tr')
        # e = rows[0].find_elements_by_tag_name('td')

        contacts = self.driver.find_element_by_id('maintable')
        table = etree.HTML(str(contacts.get_attribute('innerHTML'))).find("body/table")
        rows = iter(table)
        headers = [col.text for col in next(rows)]
        users = []
        for row in rows:
            values = [col.text for col in row]
            users.append(dict(zip(headers, values)))
        return users













            #    def table_parse(self):
            #
            #        users_table = self.driver.find_element_by_id("maintable")
            #
            #        table_rows = users_table.self.driver.find_element_by_tag_name("tr")
            #
            #        column_names = ['Photo', 'Name', 'Address', 'All e-mail', 'All phones']
            #
            #        for column in column_names:
            #            print column
            #
            #        contacts = []
            #            for row in table_rows:
            #                print contacts[]
            #
            #        param_name = column_names[id]
            #
            #        contact[param_name] = cell.text
            #
            #        contact.append(contact)