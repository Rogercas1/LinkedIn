import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

#url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
df = pd.DataFrame()
Title = []
Company = []
Location = []

for i in range(10):

                url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position='
                url = url + str(i) + '&pageNum=0'
                print(url)

                response = requests.get(url)
                print(response)

                soup = BeautifulSoup(response.content, 'html.parser')

                jobs = soup.find_all('div',
                                        class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
                for job in jobs:
                    job_title = job.find('h3', class_='base-search-card__title').text.strip()
                    job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
                    location = job.find('span', class_='job-search-card__location').text.strip()
                    if job_company not in Company:
                        Title.append(job_title)
                        Company.append(job_company)
                        Location.append(location)
                    else:
                        continue

df['title'] = Title
df['company'] = Company
df['location'] = Location
df.drop_duplicates()
print(df)
df.to_csv('test.csv', index=False)






