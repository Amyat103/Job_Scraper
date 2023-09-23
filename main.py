import requests
import key
from bs4 import BeautifulSoup

# TODO: Pair all the info to each company
# TODO: Put them into excel
# TODO: Put everything in functions
# TODO: Make it search multiple pages


#requests
r = requests.get(f"https://api.scrapingant.com/v2/general?url=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3DPython%2BInternship%26l%3DBoston%252C%2BMA%26start%3D10%26pp%3DgQAPAAABimfNo-sAAAACESYLbQAcAQEBCBbB6hjtFyr5Z2-Pg3aki9oX2Kf9o1NJ-AAA%26vjk%3D66192889ae4b5af1&x-api-key={key.API_KEY}")
print(r.status_code) #keep till after changing link
response = r.content

#parse
soup = BeautifulSoup(response, "lxml")

#find job title
titles = soup.find_all("h2", class_="jobTitle")
for title in titles:
    print(title.text)

print()

def find_job(soup):
    num_job = len(soup.find_all("div", class_="cardOutline"))
    print(num_job)
    job_box = soup.find_all("div", class_="cardOutline")
    for job in num_job:
        company_names = soup.find("span", class_="companyName")
        company_locations = soup.find("div", class_="companyLocation")
        estimate_salaries = soup.find("span", class_="estimated-salary")
        attribute_snippets = soup.find("div", class_="attribute_snippet")
        description_snippets = soup.find("div", class_="job-snippet")
        job_dates = soup.find("span", class_="date")
        job_links = soup.find("h2", class_="jobTitle")
        link_div = a.find("a")
        pre_end_link = link_div.get("href")
        end_link = pre_end_link[7:]
        print(end_link)
        link_head = "https://www.indeed.com/viewjob"
        link = link_head + end_link
        job_result = {
            "Company Name": company_names,
            "Job Location": company_locations,
            "Estimated Salary": estimate_salaries,
            "Attribute Snippet": attribute_snippets,
            "Description Snippet": description_snippets,
            "Date Posted": job_dates,
            "Indeed Link": link
        }
        print(job_result)

#find company name
company_names = soup.find_all("span", class_="companyName")
for name in company_names:
    print(name.text)

print()
#find company location
company_locations = soup.find_all("div", class_="companyLocation")
for location in company_locations:
    print(location.text)

print()
#find estimate salary by indeed
estimate_salaries = soup.find_all("span", class_="estimated-salary")
for salary in estimate_salaries:
    print(salary.text)

print()
#find attribute snippet
attribute_snippets = soup.find_all("div", class_="attribute_snippet")
for attribute in attribute_snippets:
    print(attribute.text)

print()
#find description
description_snippets = soup.find_all("div", class_="job-snippet")
for description in description_snippets:
    print(description.text.strip())

print()
#date posted
job_dates = soup.find_all("span", class_="date")
for date in job_dates:
    print(date.text)

print()
#link
job_links = soup.find_all("h2", class_="jobTitle")
for a in job_links:
    link_div = a.find("a")
    pre_end_link = link_div.get("href")
    end_link = pre_end_link[7:]
    print(end_link)
    link_head = "https://www.indeed.com/viewjob"
    link = link_head + end_link
    print(link)

find_job(soup)