from selenium import webdriver
import time

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://accounts.google.com/")

#get the username textbox
login_field = driver.find_element_by_name("identifier")
login_field.clear()

#enter username
login_field.send_keys("ENTER USERNAME HERE")
login_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

#get the password textbox
password_field = driver.find_element_by_name("password")
password_field.clear()

#enter password
password_field.send_keys("ENTER PASSWORD HERE")
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(10)

#navigate to gmail
driver.get("https://mail.google.com/")




