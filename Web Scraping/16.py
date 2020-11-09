from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Edge()
browser.get("http://inventwithpython.com/")
link = browser.find_element_by_link_text("Read It Online")
link.click()

#for using keyboard
#link.sendKeys("Hello World")
#link.send_keys(Keys.END)