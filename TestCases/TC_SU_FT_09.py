from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("Nam")
lastName.send_keys("Nguyễn Văn")
email.send_keys("nguyenvannam@gmail.com")
password.send_keys("namnguyen")
toggle_checkbox(checkbox, True)
sign_up_button.click()
time.sleep(5)
try:
    error_popup = browser.find_element(By.XPATH, "//div[@title='error']")
    if (error_popup.text == "Email này đã được sử dụng"):
        print("pass")
    else:
        print("fail")
except:
    print("fail")

browser.quit()