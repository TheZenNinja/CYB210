from selenium import webdriver
from selenium.webdriver.common.keys import Keys

page = "https://google.com/"

browser = webdriver.Edge()

browser.get(page)
#browser.get("http://inventwithpython.com/")
#link = browser.find_element_by_link_text("Read It Online")
#link.click()

#for using keyboard
#link.sendKeys("Hello World")
#link.send_keys(Keys.END)