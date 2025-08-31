from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


class JobScraper:
    def __init__(self, job_title, results_num):
        self.driver = webdriver.Chrome()
        self.job_title = job_title
        self.num_results = results_num
        self.results = []

    def search_jobs(self):
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={job_title}")

        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))

        for i in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            

    def extract_data(self):
        cards = self.driver.find_elements(By.CLASS_NAME, 'base-card')[:self.results_num]

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
            except:
                location = "not found"

            try:
                link = card.find_element(By.CSS_SELECTOR, 'a.base-card__full-link').get_attribute("href")
            except:
                link = "not found"

    def save_data(self, filename):
        if not self.results: 
            print("☹️  No jobs found for this title.")
            return 

        safe_title = "_".join(self.job_title.strip().lower().split())
        filename = f"jobs_{safe_title}.csv"

        dataframe = pd.DataFrame(self.results)
        dataframe.to_csv(filename, index=False)
        print(f"\n😍  Jobs are saved in {filename}")


job_title = input("🥸  Enter the job title: ")
input_num = input("🥸  How many results do you want? ")

try:
    results_num = int(input_num)
    if results_num <= 0:
        raise ValueError
except ValueError:
    raise SystemExit("☹️  Please enter a valid positive number.")

scraper = JobScraper(job_title, results_num)
scraper.search_jobs()
scraper.extract_data()
scraper.save_data()
scraper.close()

        
                
                
                

# job_title = input("🥸  Enter the job title: ")
# input_num = input("🥸  How many results do you want? ")

# try:
#     num_results = int(input_num)
#     if num_results <= 0:
#         raise ValueError
# except ValueError:
#     raise SystemExit("☹️  Please enter a valid positive number.")

# driver = webdriver.Chrome()

# query = job_title.replace(" ", "%20")
# driver.get(f"https://www.linkedin.com/jobs/search/?keywords={query}")

# WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))

# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# cards = driver.find_elements(By.CLASS_NAME, 'base-card')[:num_results]

# print(f"\n💎 {len(cards)} jobs are found for '{job_title}'.\n")


# i = 1
# results =[]
# for card in cards:
#     try:
#         job = card.find_element(By.CSS_SELECTOR, 'h3.base-search-card__title').get_attribute("innerText").strip()
#     except:
#         job = "not found"

#     try:
#         company = card.find_element(By.CSS_SELECTOR, 'h4.base-search-card__subtitle a').get_attribute("innerText").strip()
#     except:
#         company = "not found"

#     try:
#         location = card.find_element(By.CSS_SELECTOR, 'span.job-search-card__location').get_attribute("innerText").strip()
#         if "," in location:
#             location = location.split(",")[0].strip()
#     except:
#         location = "not found"

#     try:
#         link = card.find_element(By.CSS_SELECTOR, 'a.base-card__full-link').get_attribute("href")
#     except:
#         link = "not found"

#     results.append({
#         "Job Title": job,
#         "Company": company,
#         "Location": location,
#         "Link": link
#     })
#     i += 1
    
# driver.quit()

# if results:
#     safe_title = "_".join(job_title.strip().lower().split())
#     filename = f"jobs_{safe_title}.csv"

#     jobs = pd.DataFrame(results)
#     jobs.to_csv(filename, index=False)
#     print(f"\n😍  Jobs are saved in {filename}")
# else:
#     print("☹️  No jobs found.")
