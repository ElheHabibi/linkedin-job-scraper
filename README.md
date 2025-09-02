# LinkedIn Job Scraper

## 📄 Overview
This project is a **simple web scraper built with Python and Selenium** that allows users to search for job titles on **LinkedIn** and extract information about job opportunities (such as job title, company, location, and job link).  
The results are saved in a CSV file.

---

## 🦋 Features
- Search for job titles on LinkedIn  
- Extract key information for each job posting:
  - Job Title  
  - Company Name  
  - Location  
  - Direct Job Link  
- Save results into a CSV file  
- Object-Oriented (OOP) design for clean and maintainable code  

---

## 🛠 Requirements
1. **Python 3.8+**  
2. **Selenium** → for browser automation  
3. **ChromeDriver** → to connect Selenium with Chrome  
4. **pandas** → for saving results into CSV  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/linkedin-job-scraper.git
cd linkedin-job-scraper
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver
- Check your Chrome version:  
  **Help → About Chrome**  
- Download the matching ChromeDriver version from the official site:  
  🔗 https://sites.google.com/chromium.org/driver/  
- Extract the file and place it inside the `chromedriver-win64` folder.

---

## ▶ Usage
The results will be shown in terminal
Run the script:
```bash
python scraper.py
```

Then:  
1. Enter the job title (e.g., `Data Scientist`)  
2. Enter the number of results you want (e.g., `10`)  
3. The scraper will extract the jobs and save them automatically in:  

```
results/jobs_<job_title>.csv
```

---

## 📂 Project Structure
```bash
LINKEDIN-JOB-SCRAPER
├── .venv/                  
├── chromedriver-win64/    
├── results/                
├── .gitignore
├── README.md            
├── requirements.txt        
└── scraper.py       
```

---

## 💡 Possible Improvements
- Filter jobs by location (e.g., Tehran or Remote)  
- Filter by experience level (Entry, Mid, Senior)  
- Store results in an SQLite database instead of CSV  
- Add a simple web interface using **Streamlit**  
