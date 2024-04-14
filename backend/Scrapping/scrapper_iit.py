import requests
from bs4 import BeautifulSoup

# URL of the directory page listing all professors
directory_url = 'https://www.iit.edu/directory/people'

# Function to fetch and parse a webpage
def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an exception for bad status
    return BeautifulSoup(response.text, 'html.parser')

# Fetch the directory page
directory_soup = get_soup(directory_url)

# Extract professor names and URLs
professors = []
for h3_tag in directory_soup.find_all('h3', class_='arrow-link'):  # Update class as per actual website
    name = h3_tag.get_text(strip=True).replace(' ', '-')
    professors.append(name)

# Collect content from each professor's page
all_content = []
for prof in professors:
    prof_url = f'{directory_url}/{prof}'
    prof_soup = get_soup(prof_url)
    # Assume we need all text from the professor's page
    text = prof_soup.get_text(separator=' ', strip=True)
    all_content.append(text)

# Write all contents to a single text file
with open('professors_content.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(all_content))

print("Content has been successfully written to professors_content.txt")