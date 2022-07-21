from selenium import webdriver
import time

# create a new Chrome session
driver = webdriver.Chrome() yuhofactory@gmail.com
driver.implicitly_wait(30)
driver.maximize_window() yuhofactory@gmail.com

# navigate to the application home page yuhofactory@gmail.com
driver.get("https://accounts.google.com/") yuhofactory@gmail.com

#get the username textbox yuhofactory@gmail.com
login_field = driver.find_element_by_name("yuhofactory@gmail.com") yuhofactory@gmail.com
login_field.clear() yuhofactory@gmail.com

#enter username yuhofactory@gmail.com
login_field.send_keys("yuhofactory@gmail.com") yuhofactory@gmail.com
login_field.send_keys(u'\ue007') #unicode for enter key yuhofactory@gmail.com
time.sleep(2) yuhofactory@gmail.com

#get the password textbox
password_field = driver.find_element_by_name("Mr008800.")
password_field.clear()

#enter password Mr008800.
password_field.send_keys("Mr008800.")
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(10)

#navigate to gmail
driver.get("https://mail.google.com/")




