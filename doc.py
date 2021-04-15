# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:14:07 2021

@author: Solana
"""

import pandas as pd
import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select

for i in range(1,6):
    
    if i > 1:
        time.sleep(100)
    
    df = pd.read_csv("lst"+str(i)+".csv", index_col=0)
    acc= []
    
    for symbol in df["0"]:
        try:
            driver = webdriver.Chrome()
            driver.get("https://mops.twse.com.tw/mops/web/t163sb03")
        except:
            print(str(symbol))
            
            
        try:
            select = Select(driver.find_element_by_xpath('//*[@id="isnew"]'))
            select.select_by_value("false")
            
            element = driver.find_element_by_xpath('//*[@id="co_id"]')
            element.send_keys(str(symbol))
            
            year = driver.find_element_by_xpath('//*[@id="year"]')
            year.send_keys("103")
            
            season = Select(driver.find_element_by_xpath('//*[@id="season"]'))
            season.select_by_value("04")
            
            button = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input').click()
        except:
           print(str(symbol))
           
           
           
        time.sleep(2)
        
        try:
            acc.append(driver.find_element_by_xpath('//*[@id="table01"]/table[4]/tbody/tr[4]').text)
            driver.close()
            df = pd.DataFrame(acc)
            df.to_csv(os.getcwd()+"\\2014\\"+str(symbol)+".csv", encoding="utf_8_sig")
        except:
            print(str(symbol))
        
        time.sleep(5)
    
    
    
