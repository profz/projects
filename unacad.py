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
    print(f"Found {len(headings)} h5 headings")

    for heading in headings:
        heading_text = heading.txt.strip()
        print(f"Heading: {heading_text}")

        paragraph = heading.find_next('p')
        paragraph_text = paragraph.text.strip() if paragraph else 'N/A'
        print(f"Paragraph: {paragraph_text}")

        data.append({
            'Class': heading_text,
            'Subject': paragraph_text
        })

    return data


url = 'https://unacademy.com/goal/jee-main-and-advanced-preparation/TMUVD/planner'

html_content = fetch_page(url)
data = parse_page(html_content)

if not data:
    print("No data found. Please check the URL or the HTML structure.")

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)

print("data was saved to output.csv")
