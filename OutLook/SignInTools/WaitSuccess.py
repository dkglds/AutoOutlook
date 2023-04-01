""" doc """
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Consts import Const, Xpath


class WaitSuccess(object):
	""" doc """

	def __init__(self, browser):
		self.browser = browser

	def wait_success(self):
		while True:
			try:
				self.browser.wait_until_visible(Xpath.NO_BOTTOM, 0.5).click()
				break
			except (TimeoutException, NoSuchElementException):
				continue
