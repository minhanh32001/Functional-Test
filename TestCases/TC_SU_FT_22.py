from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("Nhân")
lastName.send_keys("Nguyễn Thiện")
email.send_keys("nguyenthiennhan")
password.send_keys("nam")
toggle_checkbox(checkbox, True)

browser.refresh()

firstNameReCheck = browser.find_element(By.XPATH, "//input[@name='firstname']")
lastNameReCheck = browser.find_element(By.XPATH, "//input[@name='lastname']")
emailReCheck = browser.find_element(By.XPATH, "//input[@name='email']")
passwordReCheck = browser.find_element(By.XPATH, "//input[@name='password']")
checkboxReCheck = browser.find_element(By.ID, 'agree-check-box')

if(firstName== firstNameReCheck and lastName == lastNameReCheck
and password==passwordReCheck and checkbox == checkboxReCheck):
    print("pass")
else:
    print("fail")

browser.quit()