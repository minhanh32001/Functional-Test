from CommonElement import *
import time

time.sleep(5)

firstName.send_keys("!@#$%^&*")
lastName.send_keys("Nguyễn Thiện")
email.send_keys("nguyenthiennhan@gmail.com")
password.send_keys("thiennguyen")
toggle_checkbox(checkbox, True)
sign_up_button.click()
try:
    wait = wdw(browser, 10)
    error_popup = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@title='error']")))
    if (error_popup.text == "Bạn cần xác nhận đồng ý với điều khoản để đăng ký"):
        print("pass")
    else:
        print("fail")
except:
    print("fail")

browser.quit()