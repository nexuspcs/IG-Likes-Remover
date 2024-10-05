from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

# Set up your driver (make sure you have the appropriate web driver for your browser)

driver = webdriver.Chrome()

# Log in to Instagram

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

username_input = driver.find_element_by_name('username')

password_input = driver.find_element_by_name('password')

username_input.send_keys('your_username')

password_input.send_keys('your_password')

password_input.send_keys(Keys.RETURN)

time.sleep(5)

# Go to your likes

driver.get('https://www.instagram.com/your_username/saved/')

time.sleep(5)

# Unlike posts

posts = driver.find_elements_by_xpath('//article//button[contains(@aria-label, "Unlike")]')

for post in posts:

post.click()

time.sleep(1)

driver.quit()