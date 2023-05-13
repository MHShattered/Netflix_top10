import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

n_weeks= 104
types=['films','films-non-english','tv','tv-non-english']
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver_path = 'Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path, options=options)

for type in types:
    #First page
    url_base= 'https://top10.netflix.com/'
    week=datetime.date(2023,4,16)

    url_driver= url_base + type + "?week=" + week.strftime('%Y-%m-%d')
    driver.get(url_driver)
    
    table_locator = (By.XPATH, "//table[@class='w-full text-sm table-fixed md:text-base ']")
    time.sleep(1)
    table = driver.find_element(*table_locator)
    
    Top10 = pd.read_html(table.get_attribute('outerHTML'))[0]
    Top10['Date']=week
    Top10 = Top10.rename(columns={Top10.columns[1]: 'Title'})

    print(f"Completata la settimana {week} di {type}")
    #Other pages
    for i in range(n_weeks):
        week= week - datetime.timedelta(days=7)
        
        url= url_base + type + "?week=" + week.strftime('%Y-%m-%d')
        url_driver= url_base + type + "?week=" + week.strftime('%Y-%m-%d')
        driver.get(url_driver)
        
        table_locator = (By.XPATH, "//table[@class='w-full text-sm table-fixed md:text-base ']")
        time.sleep(1)
        table = driver.find_element(*table_locator)
        
        if table:
            df = pd.read_html(table.get_attribute('outerHTML'))[0]
            df['Date']=week
            df = df.rename(columns={df.columns[1]: 'Title'})
            #print(df.iloc[:,1])
        else:
            print(f'Errore riscontrato alla settimana {week} di {type}')
            break

        Top10= pd.concat([Top10,df])
        print(f"Completata la settimana {week} di {type}")

    Top10.to_csv(f"Netflix_Top_10/{type}.csv", index=False)
    print(f"Completato il caricamento di {type}")


print("Caricamento completato")
