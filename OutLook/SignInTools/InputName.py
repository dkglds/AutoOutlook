""" doc """
from Consts import Const, Xpath


class InputName(object):
	""" doc """

	def __init__(self, browser):
		self.browser = browser
		self.last_name = str()
		self.first_name = str()

	@staticmethod
	def random_name_str():
		name_str = str()
		name_str += Const.random_char(Const.CAPITALS)
		for name_length in range(1, Const.NAME_LENGTH):
			name_str += Const.random_char(Const.LOWERCASES)
		return name_str

	def random_self_name(self):
		self.last_name = self.random_name_str()
		self.first_name = self.random_name_str()

	def input_name(self):
		self.random_self_name()
		self.browser.wait_until_visible(Xpath.LAST_NAME).send_keys(self.last_name)
		self.browser.wait_until_visible(Xpath.FIRST_NAME).send_keys(self.first_name)
		self.browser.wait_until_visible(Xpath.NEXT_STEP_BOTTOM).click()
