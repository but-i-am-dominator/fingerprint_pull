#!/usr/bin/python3

import requests
import subprocess

# Get the Kernel Version
kernel = subprocess.getoutput('uname -r')

# Requests containing Header with Kernel version
headers = {'Kernel-Version': kernel}
url = 'http://162.243.3.85:65000'
requests.get(url, headers=headers)


# Headless Selenium Run conditional on OS Support
try:
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=fireFoxOptions)
    driver.get(url)
    driver.close()
except:
    print("Selenium not found.")

# Completion Message with Parks and Rec Reference built in.
print("Dunn and Done.")
