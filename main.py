import requests
import key
from bs4 import BeautifulSoup
import pandas as pd


def find_job(soup):
    job_boxes = soup.find_all("div", class_="cardOutline")
    result = []
    for job in job_boxes:
        title = job.find("h2", class_="jobTitle").text
        company_names = job.find("span", class_="companyName").text
        company_locations = job.find("div", class_="companyLocation").text
        try:
            estimate_salaries = job.find("span", class_="estimated-salary").text
        except:
            estimate_salaries = "None"
        try:
            attribute_snippets = job.find("div", class_="attribute_snippet").text
        except:
            attribute_snippets = "None"
        description_snippets = job.find("div", class_="job-snippet").text.strip()
        job_dates = job.find("span", class_="date").text
        job_div = job.find("h2", class_="jobTitle")
        link_div = job_div.find("a")
        pre_end_link = link_div.get("href")
        end_link = pre_end_link[7:]
        link_head = "https://www.indeed.com/viewjob"
        link = link_head + end_link
        result_sin = {
            "Job Title": title,
            "Company Name": company_names,
            "Job Location": company_locations,
            "Estimated Salary": estimate_salaries,
            "Attribute Snippet": attribute_snippets,
            "Description Snippet": description_snippets,
            "Date Posted": job_dates,
            "Indeed Link": link
        }
        result.append(result_sin)

    return result


def request(page, location, job_type):
    link = f"https://api.scrapingant.com/v2/general?url=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3D{job_type}%26l%3D{location}%26start%3D{page}%26pp%3DgQAPAAABimfNo-sAAAACESYLbQAcAQEBCBbB6hjtFyr5Z2-Pg3aki9oX2Kf9o1NJ-AAA%26vjk%3D66192889ae4b5af1&x-api-key={key.API_KEY}"
    r = requests.get(link, timeout=200)
    response = r.content
    soup = BeautifulSoup(response, "lxml")
    print(link)
    return soup


def to_excel(job_result):
    df = pd.DataFrame(job_result)
    df.to_excel("result.xlsx", index=False)
    print(df)


def main():
    # final list
    job_result = []
    job_type = "Python Internship"
    location = "San Francisco CA"
    for page in range(0, 30, 10):
        soup = request(page, location, job_type)
        page_result = find_job(soup)
        job_result.extend(page_result)
        print("Scraping")
    to_excel(job_result)


if __name__ == "__main__":
    main()
