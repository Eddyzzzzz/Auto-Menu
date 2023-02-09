from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import datetime
import os

# Define driver
driverd = webdriver.Chrome() #Dewick
driverc = webdriver.Chrome() #Carm

#Define raw list
brunchd=[] 
dinnerd=[] 

brunchc=[] 
dinnerc=[] 

#Define new list
newbrunchd=[]
newdinnerd=[]

newbrunchc=[]
newdinnerc=[]

#Get date and day
dt = datetime.now()
day = dt.weekday()

#Get web
driverd.get("https://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=11&locationName=Dewick-MacPhie+Dining+Center&naFlag=1")
driverc.get("https://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1") #for carm

#Get elements
contentd = driverd.page_source
contentc = driverc.page_source
soupd  = BeautifulSoup(contentd, features="html.parser")
soupc  = BeautifulSoup(contentc, features="html.parser")

#Get day of the week
if day == 7:
    countd = 1
else:
    countd = 0

if day == 6:
    countc = 1
else:
    countc = 0

#Find dishes
for a in soupd.findAll('tr', attrs={'height':'5'}):
    for b in a.findAll('span'):
        # if count == 0 and b.text[0] != "-" and b.text != "\xa0":
        #     breakfast.append(b.text)
        if countd == 1 and b.text != "\xa0":
            brunchd.append(b.text)
        elif countd == 2 and b.text != "\xa0":
            dinnerd.append(b.text)
    countd += 1

for a in soupc.findAll('tr', attrs={'height':'5'}):
    for b in a.findAll('span'):
        # if count == 0 and b.text[0] != "-" and b.text != "\xa0":
        #     breakfast.append(b.text)
        if countc == 1 and b.text != "\xa0":
            brunchc.append(b.text)
        elif countc == 2 and b.text != "\xa0":
            dinnerc.append(b.text)
    countc += 1


#Rearrange for Dewick
for i in range(len(brunchd)):
    if brunchd[i] == "-- LUNCH ENTREE --":
        newbrunchd.append(brunchd[i])
        i += 1
        while (brunchd[i][0] != "-"):
            newbrunchd.append(brunchd[i])
            i += 1
        
for i in range(len(brunchd)):
    if brunchd[i] == "-- FRESH BAKED DESSERTS --":
        while (i < len(brunchd)):
            newbrunchd.append(brunchd[i])
            i += 1

for i in range(len(dinnerd)):
    if dinnerd[i] == "-- CARVED MEATS & POULTRY --":
        newdinnerd.append(dinnerd[i])
        i += 1
        while (dinnerd[i][0] != "-"):
            newdinnerd.append(dinnerd[i])
            i += 1

for i in range(len(dinnerd)):
    if dinnerd[i] == "-- DINNER ENTREES --":
        newdinnerd.append(dinnerd[i])
        i += 1
        while (dinnerd[i][0] != "-"):
            newdinnerd.append(dinnerd[i])
            i += 1

if "-- SUNDAE BAR --" in dinnerd:
    for i in range(len(dinnerd)):
        if dinnerd[i] == "-- FRESH BAKED DESSERTS --":
            newdinnerd.append(dinnerd[i])
            i += 1
            while (dinnerd[i][0] != "-"):
                newdinnerd.append(dinnerd[i])
                i += 1
else:
    for i in range(len(dinnerd)):
        if dinnerd[i] == "-- FRESH BAKED DESSERTS --":
            while (i < len(dinnerd)):
                newdinnerd.append(dinnerd[i])
                i += 1

#Rearrange for Carm
for i in range(len(brunchc)):
    if brunchc[i] == "-- LUNCH ENTREE --":
        newbrunchc.append(brunchc[i])
        i += 1
        while (brunchc[i][0] != "-"):
            newbrunchc.append(brunchc[i])
            i += 1
            
for i in range(len(brunchc)):
    if brunchc[i] == "-- LATE LUNCH --":
        newbrunchc.append(brunchc[i])
        i += 1
        while (brunchc[i][0] != "-"):
            newbrunchc.append(brunchc[i])
            i += 1

for i in range(len(brunchc)):
    if brunchc[i] == "-- BAKED FRESH DESSERTS --":
        while (i < len(brunchc)):
            newbrunchc.append(brunchc[i])
            i += 1

for i in range(len(dinnerc)):
    if dinnerc[i] == "-- DINNER ENTREES --":
        newdinnerc.append(dinnerc[i])
        i += 1
        while (dinnerc[i][0] != "-"):
            newdinnerc.append(dinnerc[i])
            i += 1

for i in range(len(dinnerc)):
    if dinnerc[i] == "-- BAKED FRESH DESSERTS --":
        while (i < len(dinnerc)):
            newdinnerc.append(dinnerc[i])
            i += 1

#If open dewick
if len(brunchd) <= 1:
    titled = "Dewick is closed today!\n"
    with open("Desktop/prac/menu.txt", 'w') as f:
        f.write(titled)
else:
    titled = "Dewick is open today!\n"
    with open("Desktop/prac/menu.txt", 'w') as f:
        f.write(titled)
        # f.write("\nBREAKFAST:\n")
        # for dish in breakfast:
        #     f.write(f'{dish}\n')
        f.write("\nBRUNCH:\n")
        for dish in newbrunchd:
            f.write(f"{dish}\n")
        f.write("\nDINNER:\n")
        for dish in newdinnerd:
            f.write(f"{dish}\n")
        f.write("\nBon Appétit!")

#If open carm
if len(brunchc) <= 1:
    titlec = "Carm is closed today!\n"
    with open("Desktop/prac/menuc.txt", 'w') as f:
        f.write(titlec)
else:
    titlec = "Carm is open today!\n"
    with open("Desktop/prac/menuc.txt", 'w') as f:
        f.write(titlec)
        # f.write("\nBREAKFAST:\n")
        # for dish in breakfast:
        #     f.write(f'{dish}\n')
        f.write("\nBRUNCH:\n")
        for dish in newbrunchc:
            f.write(f"{dish}\n")
        f.write("\nDINNER:\n")
        for dish in newdinnerc:
            f.write(f"{dish}\n")
        f.write("\nBon Appétit!")

# to end auto execution, terminal crontab -r

