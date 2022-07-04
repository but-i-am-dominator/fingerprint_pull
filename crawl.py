from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import subprocess as sp

# Get the Kernel Version
kernel = sp.getoutput('uname -r')

# Requests
headers = {'Kernel-Version': kernel}
url = 'http://162.243.3.85:65000'
requests.get(url, headers=headers)


# Selenium

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(executable_path=r'./geckodriver', firefox_options=fireFoxOptions)

driver.get(url)
print(driver.title)
print(driver.current_url)
sleep(5)
driver.close()