from Setup import browser
from selenium.webdriver.common.by import By
import time

logo_element = browser.find_element(By.XPATH, "//a[@id='logo']")
logo_element.click()

time.sleep(5)

if (browser.title== "HMD home"):
    print ("pass")
else:
    print("fail")

browser.quit()