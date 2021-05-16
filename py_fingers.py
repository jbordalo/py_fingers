import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

url = "https://10fastfingers.com/typing-test/english"
input_field_id = "inputfield"


def calculate_wpm():
	if len(sys.argv) == 1:
		return 0
	else:
		return 60 / int(sys.argv[1])


def type_word():
	try:
		# grab word to type
		curr_word = driver.find_element_by_class_name("highlight").text

		# type the word and hit space
		input_field.send_keys(curr_word)
		input_field.send_keys(Keys.SPACE)

		return True
	except NoSuchElementException:
		return False


# set up driver
driver = webdriver.Chrome()
driver.get(url)

sleep(2)

# bypass cookies
cookie = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
cookie.click()

# grab input field
input_field = driver.find_element_by_id(input_field_id)

WPM_SLEEP = calculate_wpm()

print(f"Printing a word every {WPM_SLEEP} seconds")

while type_word():
	sleep(WPM_SLEEP)

# quit
# sleep(2)
# driver.quit()
