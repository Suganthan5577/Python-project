import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure Selenium to use headless Chrome
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# URL to scrape
url = 'https://www.olx.in/items/q-car-cover'

# Open the URL
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust as necessary for your connection speed

# Find all listing elements
listings = driver.find_elements(By.CSS_SELECTOR, 'li.EIR5N')

# Open CSV file for writing
with open('car_covers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])

    for listing in listings:
        try:
            title = listing.find_element(By.CSS_SELECTOR, 'span._2tW1I').text
            price = listing.find_element(By.CSS_SELECTOR, 'span._89yzn').text
            writer.writerow([title, price])
        except:
            continue

# Close the browser
driver.quit()
