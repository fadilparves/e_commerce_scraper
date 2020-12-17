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

links = []
condition = True

while condition:
    time.sleep(5)
    wb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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


