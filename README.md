# Job Scraper
This Web Scraper scrapes Indeed.com for jobs based on the parameters <br>

## Why I Built This Bot
I've always been interested in space and love looking at pictures and articles about it. Making this bot that posts a space picture and has an explanation on the bottom is a way to share my interest with like-minded people since this is posted only in a subreddit about space.

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

## Example
### This is an example of Excel Sheet that is created in the same folder after running the program.
<br>
<img width="1394" alt="Screenshot 2023-10-11 at 2 35 58 PM" src="https://github.com/Amyat103/Job_Scraper/assets/109713601/7637ae0f-bf6a-4b61-867a-300e68fc8a1f">


