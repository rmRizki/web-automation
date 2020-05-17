from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#replace with your own path to webdriver
browser = webdriver.Chrome("/opt/WebDriver/bin/chromedriver")

browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

target = input("Input target contact : ")
string = input("Input message : ")

x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name("_1Plpp")
for i in range(10):
    input_box.send_keys(string + Keys.ENTER)
