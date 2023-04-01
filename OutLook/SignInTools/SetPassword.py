""" doc """
from Consts import Const, Xpath


class SetPassword(object):
	""" doc """

	def __init__(self, browser):
		self.browser = browser
		self.password = Const.PASSWORD

	def set_password(self):
		self.browser.wait_until_visible(Xpath.INPUT_PASSWORD).send_keys(self.password)
		self.browser.wait_until_visible(Xpath.NEXT_STEP_BOTTOM).click()
