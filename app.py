from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.apartments.com/")

    # lookup the location user inputted
    def lookup_searchbox(self, location):
        element_quickSearch = self.driver.find_element(By.ID, "quickSearchLookup")
        element_quickSearch.clear()
        element_quickSearch.send_keys(location)
        element_quickSearch.send_keys(Keys.RETURN)

    def close_app(self):
        self.driver.close()

if __name__ == "__main__":
    obj = Application()
    location = input("Please enter a location: ")
    obj.lookup_searchbox(location)
    input("Press enter to end program: ")