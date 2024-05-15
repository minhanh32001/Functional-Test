from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("Nhân")
lastName.send_keys("!@#$%^&*")
email.send_keys("nguyenthiennhan@gmail.com")
password.send_keys("thiennguyen")
toggle_checkbox(checkbox, True)
sign_up_button.click()
time.sleep(5)
try:
    error_popup = browser.find_element(By.XPATH, "//div[@title='error']")
    if (error_popup.text == "Last Name không hợp lệ, vui lòng kiểm tra lại"):
        print("pass")
    else:
        print("fail")
except:
    print("fail")

browser.quit()