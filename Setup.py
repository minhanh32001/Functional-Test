import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
firefox_driver = 'D:\Job\HMDTest\Drivers\geckodriver.exe'
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', user_agent)

browser = webdriver.Firefox(service=firefox_service, options= firefox_options)

url = 'https://itviec.com/sign_up'

browser.get(url)
browser.maximize_window()