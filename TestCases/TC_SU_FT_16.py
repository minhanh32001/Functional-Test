from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("")
lastName.send_keys("Nguyễn Thiện")
email.send_keys("nguyenthiennhan@gmail.com")
password.send_keys("thiennguyen")
toggle_checkbox(checkbox, False)
sign_up_button.click()
time.sleep(5)
try:
    error_popup = browser.find_element(By.XPATH, "//div[@title='error']")
    if (error_popup.text == "Bạn cần điền đầy đủ các trường để đăng ký"):
        print("pass")
    else:
        print("fail")
except:
    print("fail")

browser.quit()