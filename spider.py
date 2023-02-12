import csv

import requests
from bs4 import BeautifulSoup

job_title = 'analyst'
region = 'Dubai'

url = f'https://www.linkedin.com/jobs/search/?currentJobId=3459202038&keywords=%7Banalyst%7D&location=%7Bdubai%7D'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

jobs = soup.find_all('li', class_='result-card')

job_data = []
for job in jobs:
    title = job.find('h3', class_='result-card__title').text.strip()
    company = job.find('a', class_='result-card__subtitle-link').text.strip()
    location = job.find('span', class_='job-result-card__location').text.strip()
    date_posted = job.find('time')['datetime']
    job_url = job.find('a', class_='result-card__full-card-link')['href']
    job_data.append({
        'title': title,
        'company': company,
        'location': location,
        'date_posted': date_posted,
        'job_url': job_url
    })

# Export job data to CSV file
with open('jobs.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'company', 'location', 'date_posted', 'job_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in job_data:
        writer.writerow(job)
