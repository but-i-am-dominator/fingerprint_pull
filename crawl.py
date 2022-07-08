#!/usr/bin/python3

import requests
import subprocess
import sys

# Get the Kernel Version
kernel = subprocess.getoutput('uname -r')

# Requests containing Header with Kernel version
headers = {'Kernel-Version': kernel}
url = sys.argv[1:].pop()
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