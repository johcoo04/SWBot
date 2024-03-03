import schedule
import time
import json

from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_in(config, username, password):
    driver = webdriver.Chrome()
    driver.get(config['loginURL'])

    # Define the maximum amount of time to wait (in seconds)
    max_wait_time = 10

    # Click the log in button
    loginButton = WebDriverWait(driver, max_wait_time).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
    )
    loginButton.click()

    # Wait until username box is visible
    usernameBox = WebDriverWait(driver, max_wait_time).until(
        EC.visibility_of_element_located((By.XPATH, config['usernameBoxXPATH']))
    )
    # Enter username data
    usernameBox.send_keys(username)

    # Wait until password box is visible
    passwordBox = WebDriverWait(driver, max_wait_time).until(
        EC.visibility_of_element_located((By.XPATH, config['passwordBoxXPATH']))
    )
    # Enter password data
    passwordBox.send_keys(password)

    # Wait until the element is clickable
    loginFormButton = WebDriverWait(driver, max_wait_time).until(
        EC.element_to_be_clickable((By.XPATH, config['loginFormButtonXPATH']))
    )

    # Perform the click action
    loginFormButton.click()
    
    my_account_link = WebDriverWait(driver, max_wait_time).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
    
    # Click the link
    my_account_link.click()
    
    driver.quit()


if __name__ == "__main__":
   
    with open('/Users/jackcoon/Documents/Python/SWBot/config.json', 'r') as file:
        config = json.load(file)

    print("Which user do you want to log in?")
    user = input().upper()
    
    username = config["users"][user]["username"]
    password = config["users"][user]["password"]

    target_time = datetime.now() + timedelta(minutes=1)

    schedule.every().day.at('1:11').do(lambda: check_in(config=config, username=username, password=password))

    while True:
        schedule.run_pending()
        time.sleep(1) #polling check
