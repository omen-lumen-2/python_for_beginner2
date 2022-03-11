from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import Navigation
from fixture.session import Session


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.navigation = Navigation(self)
        self.contact = ContactHelper(self)

    def wd_quit(self):
        self.wd.quit()