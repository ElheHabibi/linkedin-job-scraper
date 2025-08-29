from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# A basic code for searching job titles for frond-end jobs and printing them

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?keywords=front")

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'base-card')))

for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

cards = driver.find_elements(By.CLASS_NAME, 'base-card')

print("\nFront-End jobs : \n")

i = 1
for card in cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, 'h3.base-search-card__title').get_attribute("innerText").strip()
    except:
        title = "not found"
    
    print(f"{i}. {title}")
    i += 1  
    
driver.quit()
