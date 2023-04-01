""" doc """
import os

from OutLook.OutLook import OutLook
from browser import get_browser
from Consts import Const


def main():
	"""
	主函数
	:return: 无
	"""
	outlook = OutLook(get_browser())
	result = outlook.signin()
	with open(os.path.abspath("resource/data.txt"), "a") as file:
		#print(os.path.abspath("resource/data.txt"))
		file.write(result + '\n')
	Const.wait(2)


if __name__ == "__main__":
	main()
