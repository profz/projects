import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []

    headings = soup.find_all('h5')
    for heading in headings:
        heading_text = heading.txt.strip()

        paragraph = heading.find_next('p')
        paragraph_text = paragraph.text.strip() if paragraph else 'N/A'

        data.append({
            'Class': heading_text,
            'Subject': paragraph_text
        })

    return data


url = 'https://unacademy.com/goal/jee-main-and-advanced-preparation/TMUVD/planner'

html_content = fetch_page(url)
data = parse_page(html_content)


df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)

print("data was saved to output.csv")
