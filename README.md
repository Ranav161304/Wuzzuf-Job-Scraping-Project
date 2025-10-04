# Wuzzuf Job Scraping Project  

A Python web scraping project that extracts job postings from **Wuzzuf.net** using Selenium and BeautifulSoup, then stores the data (job title, company, location, experience, skills, and link) in a CSV file for further analysis.  

---

## Features  
- Scrapes job postings automatically from Wuzzuf.  
- Collects essential details: title, company, location, experience, skills, and link.  
- Cleans and organizes the data into a structured CSV file.  

---

## Tools & Technologies  
- Python  
- Selenium  
- BeautifulSoup  
- CSV  

---

## Installation & Usage  

1. Clone this repository:  
   ```bash
   git clone https://github.com/username/wuzzuf-job-scraping.git
   cd wuzzuf-job-scraping
   ```

2. Install the required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:  
   ```bash
   python wuzzuf_scraper.py
   ```

4. The output will be saved as a CSV file (e.g., `jobs.csv`) in the project folder.  

---

## Output Example  

| Job Title           | Company         | Location   | Experience   | Skills                  | Link        |  
|---------------------|----------------|------------|--------------|-------------------------|-------------|  
| Data Analyst        | XYZ Tech       | Cairo, EG  | 1-3 years    | Python, SQL, Excel      | [View Job]() |  
| Software Engineer   | ABC Solutions  | Giza, EG   | 0-2 years    | Java, Spring Boot, Git  | [View Job]() |  

---

## Author  
Created by [Your Name].  
