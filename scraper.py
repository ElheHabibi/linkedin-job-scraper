from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.common.exceptions import TimeoutException


class Job_Listing_Scraper:
    def __init__(self, job_title, results_num=10):
        self.driver = webdriver.Chrome()
        self.job_title = job_title
        self.results_num = results_num  
        self.results = []

    def search_jobs(self):
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={self.job_title}")

        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))
        except TimeoutException:
            print("☹️  No jobs found for this title.")
            return

        for i in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
        return True


    def extract_data(self):
        cards = self.driver.find_elements(By.CLASS_NAME, 'base-card')[:self.results_num]
        print(f"\n💎 {len(cards)} jobs are found for '{self.job_title}'.\n")

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

            self.results.append({
                "Job Title": job,
                "Company": company,
                "Location": location,
                "Link": link
            })
            
        return True 

    def save_data(self, filename=None):
        if not self.results: 
            return 

        safe_title = "_".join(self.job_title.strip().split())
        filename = f"results/jobs_{safe_title}.csv"

        dataframe = pd.DataFrame(self.results)
        dataframe.to_csv(filename, index=False)
        print(f"\n😍  Jobs are saved in {filename}")

    def quit(self): 
        self.driver.quit()
        
        
def get_job_title():
    while True:
        title = input("🥸  Enter the job title (or type 'exit' to quit): ").strip()
        if not title:
            print("☹️  Job title can not be empty.")
            continue
        if title.lower() == "exit":
            return None
        return title

def get_results_num():
    while True:
        input_num = input("🥸  How many results do you want? (type 'back' to change job title, 'exit' to quit): ")
        if input_num.lower() == "back":
            return "back"
        if input_num.lower() == "exit":
            return None
        try:
            num = int(input_num)
            if num <= 0:
                print("☹️  Please enter a valid positive number.")
                continue
            return num
        except ValueError:
            print("☹️  Please enter a valid number.")


while True:
    job_title = get_job_title()
    if job_title is None:
        print("Exiting program...")
        break

    results_num = get_results_num()
    if results_num == "back":
        continue 
    if results_num is None:
        print("Exiting program...")
        break

    scraper = Job_Listing_Scraper(job_title, results_num)

    if not scraper.search_jobs():
        scraper.quit()
        continue

    if not scraper.extract_data():
        print("☹️  No jobs extracted.")
        scraper.quit()
        continue

    scraper.save_data()
    scraper.quit()

    choice = input("💎  Do you want to search for another job title? (y/n): ").lower()
    if choice != "y":
        print("Exiting program...")
        break
        
    

        
        

