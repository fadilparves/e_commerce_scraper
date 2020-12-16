import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = "/usr/bin/google-chrome"
wb = wb.Chrome('/usr/lib/chromedriver', options=options)
wb.get('https://shopee.com.my/Computer-Accessories-cat.174')
wb.find_element_by_xpath("//button[contains(string(), 'English')]").click()




