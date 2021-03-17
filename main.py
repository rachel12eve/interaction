from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE="http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(WEBSITE)

#click on css selector
# count=driver.find_element_by_css_selector("#articlecount a")
# print(count.text)
#count.click()


#click in link text
# all_portals=driver.find_element_by_link_text("All portals")
# all_portals.click()
#
# type in boxes #with keeps
# search=driver.find_element_by_name("search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

first_name=driver.find_element_by_name("fName")
first_name.send_keys("Rachel")
last_name=driver.find_element_by_name("lName")
last_name.send_keys("Fong")
email=driver.find_element_by_name("email")
email.send_keys("rachel12eve@hotmail.com")
confirm=driver.find_element_by_class_name("btn-block")#css selector "form button"
confirm.click()
