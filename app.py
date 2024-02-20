from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.apartments.com/")

location = input("Press Enter to close the browser: ")

element_quickSearch = driver.find_element(By.ID, "quickSearchLookup")
element_quickSearch.clear()
element_quickSearch.send_keys(location)
element_quickSearch.send_keys(Keys.RETURN)

driver.close()
