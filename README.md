# Job Scraper
This Web Scraper scrapes a job posting site for jobs based on the parameters <br>

## Why I Built This Bot
Me and a lot of my friends are in the process of applying got internships and jobs, having to click on each posting, and scroll for information about each item is really time-consuming on top of applying to jobs. This program allows you to scrape multiple pages at once and put the main information in categories, examples can be found at the end of this README.

### Installing PRAW and Requests

These are the libraries you'll need

```
pip install pandas
pip install requests
pip install beautifulsoup4
```

###

### Convert to Excel using Pandas' PD
job_result is a list with dictionaries inside
```
def to_excel(job_result):
    df = pd.DataFrame(job_result)
    df.to_excel("result.xlsx", index=False)
    print(df)
```

### Each job posting is scraped and put into different categories like below
```
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
```

## Example
### This is an example of an Excel Sheet that is created in the same folder after running the program.
Putting things into categories is needed so Pandas can covert it into sheets clearly
<br>
<img width="1394" alt="Screenshot 2023-10-11 at 2 35 58 PM" src="https://github.com/Amyat103/Job_Scraper/assets/109713601/7637ae0f-bf6a-4b61-867a-300e68fc8a1f">


