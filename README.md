# 🍽️ Auto-Menu: Smart Dining Hall Menu Scraper  

**Auto-Menu** is a Python script that automates the process of filtering **long, repetitive dining hall menus** by scraping and extracting only the **daily-updated main courses and desserts**. It simplifies menu browsing for users, especially in areas with slow internet, by condensing **200+ items** into only the most relevant options. Each morning, it **automatically sends filtered menus via text message** to over 20 users, saving time and effort.  

🔗 **Project Documentation:** [Dining Hall Menu Reminder](https://narrow-theory-18d.notion.site/Dining-Hall-Menu-Reminder-1b9436c3d41a81a2ba6bd60e1ed76cd5)  

## 🔧 Key Features  
- **Web Scraping** – Uses **Selenium** and **BeautifulSoup** to extract dining hall menus.  
- **Data Filtering** – Condenses over 200 items into relevant main courses and desserts.  
- **Automation** – Sends filtered menu updates via **SMS** every morning to over 20 users.  
- **Optimized for Slow Internet** – Reduces data load for quick and easy menu browsing.  

## 🌐 Data Source  
Menus are scraped from:  
- [Dewick-MacPhie Dining Center](https://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=11&locationName=Dewick-MacPhie+Dining+Center&naFlag=1)  
- [Carmichael Dining Center](https://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate=2%2f19%2f2023)  

## 🚀 How It Works  
1. **Scrapes Menus** – Extracts menu data from the provided dining hall websites.  
2. **Filters New Items** – Condenses menus to show only main courses and desserts that have been updated for the day.  
3. **Sends SMS Updates** – Sends the filtered menus to over 20 users each morning.  

📌 *For more details and usage instructions, check the project documentation linked above.*  
