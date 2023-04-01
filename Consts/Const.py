""" doc """
import time

from random import randint

URL = r'https://signup.live.com/' \
	  r'signup?' \
	  r'lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1680324836&rver=7.0.6737.0&wp=MBI_SSL&' \
	  r'wreply=https%3a%2f%2foutlook.live.com%' \
	  r'2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3da3710828-9f15-0e3a-f937-41a93b136105&' \
	  r'id=292841&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&' \
	  r'lic=1&uaid=c8ba417cdbac465e9a676c8a30f0b5fa'
CAPITALS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'

LETTER_DICT = CAPITALS + LOWERCASES
CHAR_DICT = CAPITALS + LOWERCASES + NUMBERS

USERNAME_LENGTH = 10

PASSWORD = "dkglds_outlook"

NAME_LENGTH = 5

COUNTRY_VALUE = 'US'
MIN_YEAR = 1950
MAX_YEAR = 2000
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 28

with open("resource/phonenum.txt", "r") as file:
	PHONE_NUMBER = file.read()

WAIT_TIME = 0.5
MAX_WAIT_TIME = 10


def wait(wait_time=WAIT_TIME):
	""" doc """
	time.sleep(wait_time)


def random_char(char_dict):
	""" doc """
	return char_dict[randint(0, len(char_dict) - 1)]
