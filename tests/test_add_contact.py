# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from model.сontact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        self.login(login="admin", password="secret")
        self.create_new_contact(Contact(
            firstname="Test_first_name",
            middlename="Test_middle_name",
            email="test@test.test"
        ))
        self.go_to_home_page()
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.wd
        # move to create new contact
        wd.find_element_by_link_text("add new").click()
        # input firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # input middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # input email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self,login, password):
        wd = self.wd
        # open authorize page
        wd.get("http://localhost/addressbook/group.php?delete=Delete+group%28s%29&selected%5B%5D=1")
        # input login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_id("LoginForm").click()
        # input password
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # submit
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
