""" doc """
from Consts import Const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Chrome(webdriver.Edge):
	""" doc """

	def wait_until_visible(self, xpath, max_time = Const.MAX_WAIT_TIME):
		"""等待指定元素出现并可见."""
		return WebDriverWait(self, max_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
