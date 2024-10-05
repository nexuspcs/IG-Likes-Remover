from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up your driver (make sure you have the appropriate web driver for your browser)
driver = webdriver.Chrome()

# Define user variables
username = 'your_username'  # Replace with your actual username
password = 'your_password'  # Replace with your actual password
max_unlikes_per_hour = 100  # Limit of unlikes per hour
time_interval = 3600 / max_unlikes_per_hour  # Pause time to ensure we stay within the 100 unlikes per hour limit

# Log in to Instagram
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')

username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

time.sleep(5)

# Go to your saved posts (change to liked posts if needed)
driver.get(f'https://www.instagram.com/{username}/saved/')
time.sleep(5)

# Unlike posts
posts = driver.find_elements_by_xpath('//article//button[contains(@aria-label, "Unlike")]')

unliked_count = 0  # Counter for unliked posts

for post in posts:
    if unliked_count >= max_unlikes_per_hour:
        print(f"Reached the limit of {max_unlikes_per_hour} unlikes per hour.")
        break  # Exit the loop if the limit is reached

    post.click()
    unliked_count += 1
    print(f"Unliked post {unliked_count}")

    # Wait between unliking each post to stay within the rate limit
    time.sleep(time_interval)

# Close the browser after unliking
driver.quit()