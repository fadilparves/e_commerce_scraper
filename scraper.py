import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/google-chrome"    #chrome binary location specified here
options.add_argument("--start-maximized") 
wb = wb.Chrome('/usr/lib/chromedriver', options=options)
wb.get('https://shopee.com.my/-FREE-GIFTS-A6-Thermal-Sticker-Thermal-Paper-Shopee-Waybill-Shipping-Label-Consignment-Note-Sticker-100*150mm-10*15cm-i.17814982.6229533411')
