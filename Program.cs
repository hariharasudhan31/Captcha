from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH

# Open the local HTML page
driver.get("file:///D:/projects/captcha/sih.html")
 # Replace with your file path

# Function to simulate human-like typing
def human_typing(element, text, typing_speed=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(typing_speed, typing_speed + 0.1))  # Random delay between keystrokes

# Function to simulate human-like click behavior
def human_click(element):
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(random.uniform(1, 2))  # Random delay after clicking

# Simulating Bot Behavior (Straightforward, no pauses)
def bot_behavior():
    # Select Aadhaar Number radio button
    aadhaar_radio_button = driver.find_element(By.ID, 'aadhaar')
    aadhaar_radio_button.click()
    print("Bot behavior: Selected Aadhaar Number radio button")
    
    # Fill in the Aadhaar Number
    aadhaar_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Aadhaar Number']")
    aadhaar_input.send_keys('123456789012')
    print("Bot behavior: Entered Aadhaar Number")

    # Select the Date of Birth
    dob_input = driver.find_element(By.ID, 'dob')
    dob_input.send_keys('1990-01-01')
    print("Bot behavior: Entered Date of Birth")

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    print("Bot behavior: Submitted form with Aadhaar number.")

# Simulating Human Behavior
def human_behavior():
    # Select Enrolment ID radio button
    enrolment_radio_button = driver.find_element(By.ID, 'enrolment')
    human_click(enrolment_radio_button)  # Human click behavior
    print("Human behavior: Selected Enrolment ID radio button")

    # Fill in the Enrolment ID
    enrolment_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Aadhaar Number']")
    human_typing(enrolment_input, '987654321098')  # Human typing behavior
    print("Human behavior: Typed Enrolment ID")

    # Select Date of Birth
    dob_input = driver.find_element(By.ID, 'dob')
    dob_input.clear()
    dob_input.send_keys('1985-06-15')
    print("Human behavior: Entered Date of Birth")

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    human_click(submit_button)  # Human click behavior
    print("Human behavior: Submitted form with Enrolment ID.")

# Choose Bot or Human behavior
is_bot = True  # Set to True for bot behavior, False for human behavior

if is_bot:
    bot_behavior()
else:
    human_behavior()

# Close the browser after a brief pause to observe the behavior
time.sleep(3)
driver.quit()
