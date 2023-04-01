""" doc """
from Consts import Const
from Chrome import Chrome


def get_browser():
	""" doc """
	browser = Chrome(executable_path='msedgedriver.exe')
	#browser.delete_all_cookies()
	browser.get(Const.URL)
	return browser
