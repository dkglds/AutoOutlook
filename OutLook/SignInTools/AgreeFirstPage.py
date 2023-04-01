""" doc """
import time

from Consts import Const, Xpath


class AgreeFirstPage(object):
    """ doc """

    def __init__(self, browser):
        self.browser = browser

    def agree_first_page(self):
        self.browser.wait_until_visible(Xpath.NEXT_STEP_BOTTOM).click()
