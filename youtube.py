from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searchKeyword = input("Input video titles : ")

#replace with your own path to webdriver
browser = webdriver.Chrome("/opt/WebDriver/bin/chromedriver")

browser.get("https://www.youtube.com/")

searchBar = browser.find_element_by_name("search_query")
searchBar.send_keys(searchKeyword + Keys.ENTER)

result = browser.find_elements_by_class_name('style-scope ytd-video-renderer')
result[0].click()

browser.maximize_window()
