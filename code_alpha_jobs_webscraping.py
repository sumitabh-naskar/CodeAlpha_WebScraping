import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_data.append({
        "Job Title": title,
        "Company": company,
        "Location": location
    })

df = pd.DataFrame(job_data)
df.to_csv("job_data.csv", index=False)

print("✅ Data scraped successfully!")
