from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

job_title = input("🥸  Enter the job title: ")
input_num = input("🥸  How many results do you want? ")

try:
    num_results = int(input_num)
    if num_results <= 0:
        raise ValueError
except ValueError:
    raise SystemExit("☹️  Please enter a valid positive number.")

driver = webdriver.Chrome()

query = job_title.replace(" ", "%20")
driver.get(f"https://www.linkedin.com/jobs/search/?keywords={query}")

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

cards = driver.find_elements(By.CLASS_NAME, 'base-card')[:num_results]

print(f"\n💎 {len(cards)} jobs are found for '{job_title}'.\n")

results = []
for i, card in enumerate(cards, start=1):
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
driver.quit()

if results:
    safe_title = "_".join(job_title.strip().lower().split())
    filename = f"jobs_{safe_title}.csv"

    jobs = pd.DataFrame(results)
    jobs.to_csv(filename, index=False)
    print(f"\n😍  Jobs are saved in {filename}")
else:
    print("☹️  No jobs found.")
