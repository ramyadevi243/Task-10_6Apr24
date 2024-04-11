from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Initialize Firefox webdriver
driver = webdriver.Firefox()

# Maximize window
driver.maximize_window()

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the page to load
time.sleep(3)

# Located the username and password input fields and login button and storing them in objects
username_input = driver.find_element(By.XPATH, "//input[@name='username'][@type='text']")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Enter username and password
username_input.send_keys("sramyadevi83")
time.sleep(2)
password_input.send_keys("demo@123")
time.sleep(3)

# Click on the login button
login_button.click()

# Wait for login to complete
time.sleep(5)

# Navigate to the Instagram profile page
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the profile page to load
time.sleep(3)

# Extract the total number of followers
followers = driver.find_element(By.XPATH, "//*[contains(text(),'followers')]/span").text
print(("Total Number of Followes and Following in Guvi Official Instagram Page: "))
print("Followers:", followers)

# Extract the total number of following
following = driver.find_element(By.XPATH,"//*[contains(text(),'following')]/span").text
print("Following:", following)

# Close the browser
driver.quit()
