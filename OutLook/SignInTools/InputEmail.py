""" doc """
import time

from Consts import Const, Xpath
from selenium.common.exceptions import NoSuchElementException


class InputEmail(object):
	""" doc """

	def __init__(self, browser):
		self.browser = browser
		self.name = str()

	def random_name(self):
		name_str = str()
		name_str += Const.random_char(Const.LETTER_DICT)
		for name_length in range(1, Const.USERNAME_LENGTH):
			name_str += Const.random_char(Const.CHAR_DICT)
		self.name = name_str
		return self.name

	def check_name_error(self):
		try:
			self.browser.find_element_by_xpath(Xpath.MEMBER_NAME_ERROR)
			return False
		except NoSuchElementException:
			return True

	def input_email_once(self):
		self.random_name()
		self.browser.wait_until_visible(Xpath.INPUT_EMAIL_NAME).send_keys(self.name)
		self.browser.wait_until_visible(Xpath.NEXT_STEP_BOTTOM).click()
		Const.wait()

	def input_email(self):
		self.input_email_once()
		while not self.check_name_error():
			self.input_email_once()
