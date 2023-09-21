import requests
import key
from bs4 import BeautifulSoup

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
#find company name
company_names = soup.find_all("span", class_="companyName")
for name in company_names:
    print(name.text)