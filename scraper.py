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
productsList = wb.find_elements_by_class_name('col-xs-2-4.shopee-search-item-result__item')
test_href = productsList[0].find_element_by_tag_name('a')
print(test_href.get_property('href'))



