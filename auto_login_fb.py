from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# init browser
browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

# open browser
browser.get("https://www.facebook.com/")

# delay web
sleep(random.randint(1, 3))

# auto add user and pass
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("abc@gmail.com")

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("yourpassword")

# Submit form
sleep(2)
txtPass.send_keys(Keys.ENTER)
sleep(3)

# close browser
browser.close()
