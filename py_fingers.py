from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://10fastfingers.com/typing-test/english"
input_field_id = "inputfield"

# set up driver
driver = webdriver.Chrome()
driver.get(url)

sleep(3)

# bypass cookies
cookie = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
cookie.click()

# grab input field
input_field = driver.find_element_by_id(input_field_id)


def type_word():
	# grab word to type
	curr_word = driver.find_element_by_class_name("highlight").text
	print(curr_word)

	# type the word and hit space
	input_field.send_keys(curr_word)
	input_field.send_keys(Keys.SPACE)

while True:
	type_word()

# quit
sleep(2)
driver.quit()
