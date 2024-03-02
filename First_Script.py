from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

def check_in():
    driver = webdriver.Chrome()
    driver.get("https://www.southwest.com/")

    # Define the maximum amount of time to wait (in seconds)
    max_wait_time = 10
    loginFormButtonXPATH = "//button[@id = 'login-form--submit-button']"
    loginButtonXPATH =  '//div[@class="flyout-trigger header-control--login-button-trigger"]/button'
    usernameBoxXPATH =  "//input[@id='username']"
    passwordBoxXPATH =  "//input[@id='password']"

    loginButton = WebDriverWait(driver, max_wait_time).until(
        EC.element_to_be_clickable((By.XPATH, loginButtonXPATH))
    )

    loginButton.click()

    usernameBox = WebDriverWait(driver, max_wait_time).until(
        EC.visibility_of_element_located((By.XPATH, usernameBoxXPATH))
    )
    #usernameBox.click()
    usernameBox.send_keys("jackcoon4")

    passwordBox = WebDriverWait(driver, max_wait_time).until(
        EC.visibility_of_element_located((By.XPATH, passwordBoxXPATH))
    )
    #passwordBox.click()
    passwordBox.send_keys("Kate3456")


    # Wait until the element is clickable
    loginFormButton = WebDriverWait(driver, max_wait_time).until(
        EC.element_to_be_clickable((By.XPATH, loginFormButtonXPATH))
    )

    # Once the element is clickable, you can perform the click action
    loginFormButton.click()

    driver.quit()


def run():
    # Your flight check-in code here
    check_in


if __name__ == "__main__":
    # Schedule the task for 24 hours before your flight
    schedule.every().day.at("15:18").do(run)

    while True:
        schedule.run_pending()
        time.sleep(30)  # Check every minute
