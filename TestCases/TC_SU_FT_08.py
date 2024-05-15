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
if (browser.title== "Login"):
    print ("pass")
else:
    print("fail")

browser.quit()