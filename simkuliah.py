from selenium import webdriver
from getpass import getpass

nimKeyword = input("Masukkan NIM: ")
pwKeyword = getpass("Masukkan Password: ")

#replace with your own path of webdrivers
browser = webdriver.Chrome("/opt/WebDriver/bin/chromedriver")

browser.get("https://simkuliah.unsyiah.ac.id/")

nim = browser.find_element_by_name("username")
nim.send_keys(nimKeyword)

pw = browser.find_element_by_name("password")
pw.send_keys(pwKeyword)

login = browser.find_element_by_class_name("btn")
login.click()

browser.get('https://simkuliah.unsyiah.ac.id/index.php/login/logout')
