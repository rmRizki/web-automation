from selenium import webdriver
from getpass import getpass

usernameKeyword = input("Username: ")
pwKeyword = getpass("Password: ")
repoKeyword = input("Repository Name: ")
print("""public/private?
1.public
2.private""")
visibility = int(input())

#replace with your own path to webdriver
browser = webdriver.Chrome("/opt/WebDriver/bin/chromedriver")

browser.get("https://github.com/new")

username = browser.find_element_by_name("login")
username.send_keys(usernameKeyword)

pw = browser.find_element_by_name("password")
pw.send_keys(pwKeyword)

login = browser.find_element_by_name("commit")
login.click()

repoName = browser.find_element_by_name("repository[name]")
repoName.send_keys(repoKeyword)

if visibility == 1:
    browser.find_element_by_css_selector("input[type='radio'][value='public']").click()
elif visibility == 2:
    browser.find_element_by_css_selector("input[type='radio'][value='private']").click()
else:
    browser.find_element_by_css_selector("input[type='radio'][value='private']").click()
