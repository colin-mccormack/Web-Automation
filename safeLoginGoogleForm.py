from selenium import webdriver
import time
import schedule
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
 
browser = webdriver.Chrome(executable_path='C:\\', options=option)
browser.get("")


def gmail_login(username_input, login_submit, pass_submit):
	browser.find_element_by_xpath(username_input).send_keys("")
	browser.find_element_by_xpath(login_submit).click()
	time.sleep(5)
	passWordBox = browser.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input') 
	passWordBox.send_keys("")
	time.sleep(5)
	browser.find_element_by_xpath(pass_submit).click()

gmail_login('//*[@id="identifierId"]', '//*[@id="identifierNext"]/div/button/span', '//*[@id="passwordNext"]/div/button/span')


time.sleep(5)

textboxes = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
radiobuttons = browser.find_elements_by_class_name('docssharedWizToggleLabeledContainer')

textboxes[0].send_keys("Doe, John")

radiobuttons[0].click()
radiobuttons[3].click()

time.sleep(5)

submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span';
browser.find_element_by_xpath(submit).click()

#browser.close()
