from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os

driver = webdriver.Chrome()

# name=[] #List
breakfast=[] #List
brunch=[] #List
dinner=[] #List

driver.get("https://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=11&locationName=Dewick-MacPhie+Dining+Center&naFlag=1")

content = driver.page_source
soup  = BeautifulSoup(content, features="html.parser")

# for a in soup.findAll('div', attrs={'class':'shortmenurecipes'}):
#     n = a.find('span')
#     name.append(n.text)

count = 0
for a in soup.findAll('tr', attrs={'height':'5'}):
    for b in a.findAll('span'):
        if count == 0:
            breakfast.append(b.text)
        elif count == 1:
            brunch.append(b.text)
        else:
            dinner.append(b.text)
    count += 1

# print(breakfast, brunch, dinner)

# df = pd.DataFrame({'dishes today':name}) 
# df.to_csv('dewick menu.csv', index=False, encoding='utf-8')
# # all arrays need same length
# df = pd.DataFrame({'Breakfast':breakfast, 'Brunch':brunch, 'Dinner':dinner}) 
# df.to_csv(file, index=False, encoding='utf-8')

title = "Dewick " + str(date.today()) + "\n"
with open("Desktop/prac/menu.txt", 'w') as f:
    f.write(title)
    f.write("Breakfast:\n")
    for dish in breakfast:
        f.write(f"{dish}\n")
    f.write("Brunch:\n")
    for dish in brunch:
        f.write(f"{dish}\n")
    f.write("Dinner:\n")
    for dish in dinner:
        f.write(f"{dish}\n")

# to end auto execution, terminal crontab -r
