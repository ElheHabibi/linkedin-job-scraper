import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


class JobScraper:
    def __init__(self, job_title, results_num):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.job_title = job_title
        self.num_results = results_num
        self.results = []

    def search_jobs(self):
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={self.job_title}")
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'base-card'))
            )
        except:
            return True

        for i in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    def extract_data(self):
        cards = self.driver.find_elements(By.CLASS_NAME, 'base-card')[:self.num_results]
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
            self.results.append({"Job Title": job,"Company": company,"Location": location,"Link": link})

    def get_dataframe(self):
        return pd.DataFrame(self.results)

    def close(self):
        self.driver.quit()


st.title("LinkedIn Job Scraper")

job_title = st.text_input("Enter job title : (e.g : front end)")
results_num = st.number_input("How many results do you want?", min_value=1, step=1)

if st.button("Search Jobs"):
    with st.spinner("Scraping LinkedIn... please wait ⏳"):
        scraper = JobScraper(job_title, results_num)
        scraper.search_jobs()
        scraper.extract_data()
        df = scraper.get_dataframe()
        scraper.close()
    if df.empty:
        st.error("☹️ No jobs found.")
    else:
        st.success(f"😍 Found {len(df)} jobs!")
        st.dataframe(df)
        csv = df.to_csv(index=False)
        st.download_button(label="💾 Download as CSV",data=csv,file_name=f"jobs_{job_title.replace(' ', '_').lower()}.csv")
