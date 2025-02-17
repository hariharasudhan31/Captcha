from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import math
import statistics

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH

# Open the local HTML page
driver.get("file:///D:/projects/captcha/sih.html")  # Replace with your file path

# Initialize variables for tracking
start_time = time.time()
last_click_time = None
last_key_time = None
last_mouse_position = None
mouse_jitter_count = 0
mouse_tremor_count = 0
keyhold_durations = []
key_intervals = []
click_intervals = []
mouse_move_distances = []
field_times = []
backspace_count = 0
repeated_key_count = 0
field_change_intervals = []
mouse_angle_changes = []

# Function to simulate human-like typing and log data
def human_typing(element, text, typing_speed=0.1):
    global last_key_time, backspace_count, repeated_key_count
    prev_char = None
    for char in text:
        if last_key_time:
            key_intervals.append(time.time() - last_key_time)  # Interval between key presses
        last_key_time = time.time()

        # Track backspace and repeated keys
        if char == Keys.BACKSPACE:
            backspace_count += 1
        if prev_char == char:
            repeated_key_count += 1

        element.send_keys(char)
        time.sleep(random.uniform(typing_speed, typing_speed + 0.1))  # Random delay between keystrokes
        keyhold_durations.append(random.uniform(0.05, 0.2))  # Random key hold time

        prev_char = char

# Function to simulate human-like click behavior and log data
def human_click(element):
    global last_click_time
    if last_click_time:
        click_intervals.append(time.time() - last_click_time)  # Interval between clicks
    last_click_time = time.time()
    
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    time.sleep(random.uniform(1, 2))  # Random delay after clicking

# Function to calculate distance between two points for mouse movements
def calculate_distance(last_pos, current_pos):
    return math.sqrt((current_pos[0] - last_pos[0])**2 + (current_pos[1] - last_pos[1])**2)

# Function to update mouse position and track jitter
def update_mouse_position():
    global last_mouse_position, mouse_jitter_count, mouse_tremor_count, mouse_angle_changes
    # Get current mouse position (simulating mouse movement tracking)
    current_position = (random.randint(0, 1000), random.randint(0, 1000))  # Simulated position
    if last_mouse_position:
        distance = calculate_distance(last_mouse_position, current_position)
        if distance > 10:  # Threshold to detect jitter
            mouse_jitter_count += 1

        # Track mouse angle change (using a simplified method here)
        angle = math.degrees(math.atan2(current_position[1] - last_mouse_position[1], current_position[0] - last_mouse_position[0]))
        mouse_angle_changes.append(abs(angle))

    last_mouse_position = current_position

# Function to simulate bot behavior and log data
def bot_behavior():
    global last_mouse_position, mouse_jitter_count, start_time, field_times, field_change_intervals
    
    # Select Aadhaar Number radio button
    aadhaar_radio_button = driver.find_element(By.ID, 'aadhaar')
    human_click(aadhaar_radio_button)  # Simulating bot click (human-like behavior)
    update_mouse_position()  # Track mouse jitter and movement

    field_start_time = time.time()
    # Fill in the Aadhaar Number
    aadhaar_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Aadhaar Number']")
    aadhaar_input.send_keys('123456789012')
    field_times.append(time.time() - field_start_time)  # Time spent on the field

    field_change_intervals.append(time.time() - field_start_time)  # Time between fields

    # Select the Date of Birth
    dob_input = driver.find_element(By.ID, 'dob')
    dob_input.send_keys('2005-04-11')

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    update_mouse_position()  # Track mouse jitter and movement
    print("Bot behavior: Submitted form with Aadhaar number.")

# Function to simulate human behavior and log data
def human_behavior():
    global last_mouse_position, mouse_jitter_count, start_time, field_times, field_change_intervals
    
    # Select Enrolment ID radio button
    enrolment_radio_button = driver.find_element(By.ID, 'enrolment')
    human_click(enrolment_radio_button)  # Human click behavior
    update_mouse_position()  # Track mouse jitter and movement
    
    field_start_time = time.time()
    # Fill in the Enrolment ID
    enrolment_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Aadhaar Number']")
    human_typing(enrolment_input, '987654321098')  # Human typing behavior
    field_times.append(time.time() - field_start_time)  # Time spent on the field

    field_change_intervals.append(time.time() - field_start_time)  # Time between fields

    # Select Date of Birth
    dob_input = driver.find_element(By.ID, 'dob')
    dob_input.clear()
    dob_input.send_keys('2005-04-11')

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    human_click(submit_button)  # Human click behavior
    update_mouse_position()  # Track mouse jitter and movement
    print("Human behavior: Submitted form with Enrolment ID.")

# Function to calculate average and log statistics
def calculate_and_log_metrics():
    total_time_spent = time.time() - start_time
    print(f"Time spent on page: {total_time_spent:.2f} seconds")

    if key_intervals:
        avg_key_interval = sum(key_intervals) / len(key_intervals)
        print(f"Average interval between key strokes: {avg_key_interval:.2f} seconds")

    if keyhold_durations:
        avg_keyhold_duration = sum(keyhold_durations) / len(keyhold_durations)
        print(f"Average key hold duration: {avg_keyhold_duration:.2f} seconds")

    if click_intervals:
        avg_click_interval = sum(click_intervals) / len(click_intervals)
        print(f"Average click interval: {avg_click_interval:.2f} seconds")

    if mouse_move_distances:
        avg_mouse_speed = sum(mouse_move_distances) / len(mouse_move_distances)
        print(f"Average mouse speed: {avg_mouse_speed:.2f} pixels per move")

    if field_times:
        avg_field_time = sum(field_times) / len(field_times)
        print(f"Average time spent on fields: {avg_field_time:.2f} seconds")

    if field_change_intervals:
        avg_field_change_interval = sum(field_change_intervals) / len(field_change_intervals)
        print(f"Average interval between fields: {avg_field_change_interval:.2f} seconds")

    print(f"Mouse jitter count: {mouse_jitter_count}")
    print(f"Mouse tremors count: {mouse_tremor_count}")

    if mouse_angle_changes:
        avg_mouse_angle_change = sum(mouse_angle_changes) / len(mouse_angle_changes)
        print(f"Average mouse angle change: {avg_mouse_angle_change:.2f} degrees")

    # Calculate key hold duration deviation (standard deviation)
    if keyhold_durations:
        keyhold_stddev = statistics.stdev(keyhold_durations)
        print(f"Key hold duration standard deviation: {keyhold_stddev:.2f} seconds")

    print(f"Backspace count: {backspace_count}")
    print(f"Repeated key count: {repeated_key_count}")

# Choose Bot or Human behavior
is_bot = True  # Set to True for bot behavior, False for human behavior

if is_bot:
    bot_behavior()
else:
    human_behavior()

# Calculate and display all the metrics
calculate_and_log_metrics()

# Close the browser after a brief pause to observe the behavior
time.sleep(3)
driver.quit()
