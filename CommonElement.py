from Setup import browser
from selenium.webdriver.common.by import By
firstName = browser.find_element(By.XPATH, "//input[@name='firstname']")
lastName = browser.find_element(By.XPATH, "//input[@name='lastname']")
email = browser.find_element(By.XPATH, "//input[@name='email']")
password = browser.find_element(By.XPATH, "//input[@name='password']")
checkbox = browser.find_element(By.ID, 'agree-check-box')
sign_up_button = browser.find_element(By.XPATH, "//button[text()='Sign Up']")

def toggle_checkbox(checkbox, enable):
    if enable and not checkbox.is_selected():
        checkbox.click()
    elif not enable and checkbox.is_selected():
        checkbox.click()