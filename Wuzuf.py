import requests
from bs4 import BeautifulSoup
import csv  
from itertools import zip_longest

job_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]
salary=[]

# use requests to fetch the URL
result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# save page ontect/markup
src=result.content
# print(src)

# create soup to parse content
soup=BeautifulSoup(src,"lxml")
# print(soup)

# find the elememts containing info we need
# -- job titles,job skills,company names, location names
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
# print(job_titles)
company_names=soup.find_all("a",{"class":"css-17s97q8"})
# print(company_names)
location_names=soup.find_all("span",{"class":"css-5wys0k"})
# print(location_names)
job_skills=soup.find_all("div",{"class":"css-y4udm8"})
# print(job_skills)


# create loop returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append( job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)

# print("job_titles",job_title)
# print("company_names",company_name)
# print("location_names",location_name)
# print("job_skills",skills)


# for link in links:
#     result=requests.get(link)
#     src=result.content
#     soup=BeautifulSoup(src,"lxml")
#     salaries=soup.find("span",{"class":"css-4xky9y"})
#     salary.append(salaries)

for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")

    salary_span = soup.find("span", {"class": "css-4xky9y"})
    
    if salary_span is not None:
        salary_text = salary_span.text.strip()
        print("confidental")
    else:
        salary_text = "Not available"

    salary.append(salary_text.strip())

# create csv file and fill ith values
file_list=[job_title,company_name,location_name,skills,links,salary]
exported=zip_longest(*file_list)
with open(r"D:\DEPI\Technical\2- Python\web scraping.csv","w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["job_title","company_names","location_names","job_skills","links","salary"])
    wr.writerows(exported)
