""" doc """

from OutLook.SignInTools import \
	AgreeFirstPage, InputEmail, SetPassword, InputName, InputOtherInformation, WaitSuccess


class OutLook(object):
	""" doc """

	def __init__(self, browser):
		self.browser = browser
		self.agree_first_page_tool = None
		self.input_email_tool = None
		self.set_password_tool = None
		self.input_name_tool = None
		self.input_other_information_tool = None
		self.wait_success_tool = None
		self._init_tools()

	def _init_tools(self):
		self.agree_first_page_tool = AgreeFirstPage(self.browser)
		self.input_email_tool = InputEmail(self.browser)
		self.set_password_tool = SetPassword(self.browser)
		self.input_name_tool = InputName(self.browser)
		self.input_other_information_tool = InputOtherInformation(self.browser)
		self.wait_success_tool = WaitSuccess(self.browser)

	def signin(self):
		self.agree_first_page_tool.agree_first_page()
		self.input_email_tool.input_email()
		self.set_password_tool.set_password()
		self.input_name_tool.input_name()
		self.input_other_information_tool.input_other_information()
		print(self.input_email_tool.name + "@outlook.com" + " - " + self.set_password_tool.password)
		self.wait_success_tool.wait_success()
		return self.input_email_tool.name + "@outlook.com" + " - " + self.set_password_tool.password

