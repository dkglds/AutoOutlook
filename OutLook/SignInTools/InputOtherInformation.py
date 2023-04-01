""" doc """
from Consts import Const, Xpath
from selenium.webdriver.support.select import Select
from random import randint


class InputOtherInformation(object):
	""" doc """
	def __init__(self, browser):
		self.browser = browser

	def input_other_information(self):
		Select(self.browser.wait_until_visible(Xpath.COUNTRY)).select_by_value(Const.COUNTRY_VALUE)
		self.browser.wait_until_visible(Xpath.BIRTH_YEAR).send_keys(
			str(randint(Const.MIN_YEAR, Const.MAX_YEAR))
		)
		self.browser.wait_until_visible(Xpath.BIRTH_MONTH).send_keys(
			str(randint(Const.MIN_MONTH, Const.MAX_MONTH))
		)
		self.browser.wait_until_visible(Xpath.BIRTH_DAY).send_keys(
			str(randint(Const.MIN_DAY, Const.MAX_DAY))
		)
		self.browser.wait_until_visible(Xpath.NEXT_STEP_BOTTOM).click()
