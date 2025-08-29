from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?keywords=front")

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))

for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

cards = driver.find_elements(By.CLASS_NAME, 'base-card')

print("\nFront-End jobs : \n")

i = 1
results =[]
for card in cards:
    try:
        job = card.find_element(By.CSS_SELECTOR, 'h3.base-search-card__title').get_attribute("innerText").strip()
    except:
        job = "not found"

    try:
        company = card.find_element(By.CSS_SELECTOR, 'h4.base-search-card__subtitle a').get_attribute("innerText").strip()
    except:
        company = "not found"

    try:
        location = card.find_element(By.CSS_SELECTOR, 'span.job-search-card__location').get_attribute("innerText").strip()
        if "," in location:
            location = location.split(",")[0].strip()
    except:
        location = "not found"

    try:
        link = card.find_element(By.CSS_SELECTOR, 'a.base-card__full-link').get_attribute("href")
    except:
        link = "not found"

    results.append({
        "Job Title": job,
        "Company": company,
        "Location": location,
        "Link": link
    })
    i += 1  
    
    if results:
        df = pd.DataFrame(results)
        df.to_csv("jobs_frontend.csv", index=False, encoding="utf-8-sig")
        print("\n😍 Jobs are saved in jobs_frontend.csv")
    else:
        print("☹️ No jobs found.")
        
driver.quit()
