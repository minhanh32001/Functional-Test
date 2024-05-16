from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("Nhân")
lastName.send_keys("Nguyễn Thiện")
email.send_keys("nguyenthiennhan")
password.send_keys("nam")
toggle_checkbox(checkbox, False)
sign_up_button.click()
try:
    wait = wdw(browser, 10)
    error_popup = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@title='error']")))
    close_button = error_popup.find_element(By.XPATH, "//button[@class='btn-close']")
    close_button.click()

    firstNameReCheck = browser.find_element(By.XPATH, "//input[@name='firstname']")
    lastNameReCheck = browser.find_element(By.XPATH, "//input[@name='lastname']")
    emailReCheck = browser.find_element(By.XPATH, "//input[@name='email']")
    passwordReCheck = browser.find_element(By.XPATH, "//input[@name='password']")
    checkboxReCheck = browser.find_element(By.ID, 'agree-check-box')

    if(firstName== firstNameReCheck and lastName == lastNameReCheck
    and password==passwordReCheck and checkbox == checkboxReCheck):
        print("pass")
except:
    print("fail")

browser.quit()