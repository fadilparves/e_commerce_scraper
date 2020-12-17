import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import time
import numpy as np

options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("window-size=1440,1080")
wb = wb.Chrome('/usr/lib/chromedriver', options=options)
wb.get('https://shopee.com.my/Computer-Accessories-cat.174')
time.sleep(2)
wb.find_element_by_xpath("//button[contains(string(), 'English')]").click()

links = []
condition = True

while condition:
    time.sleep(2)
    total_height = int(wb.execute_script("return document.body.scrollHeight"))
    for i in np.arange(0.1,1,0.1):
        wb.execute_script("window.scrollTo(0, "+ str(total_height*i) +");")
        time.sleep(3)
    
    productsList = wb.find_elements_by_class_name('col-xs-2-4.shopee-search-item-result__item')
    for i in range(len(productsList)):
        print(i)
        href_finder = productsList[i].find_element_by_tag_name('a')
        links.append(href_finder.get_property('href'))

    condition=False

    
df = pd.DataFrame()
df['links'] = links
df.to_csv("test_links.csv")


