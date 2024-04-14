import requests
from bs4 import BeautifulSoup
import urllib.robotparser

def scrape_website(url, depth, scraped_content, robots_txt):
    """
    Scrapes a website and its links recursively up to a specified depth,
    storing content in a text file and respecting robots.txt.

    Args:
        url (str): The URL of the website to scrape.
        depth (int): The maximum depth for recursive scraping.
        scraped_content (str): Accumulated scraped content.
        robots_txt (urllib.robotparser.RobotFileParser): Parsed robots.txt data.

    Returns:
        str: Updated scraped content.
    """

    if robots_txt.can_fetch("*", url):  # Respect robots.txt disallow
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and store content (replace with your specific logic)
        content = soup.get_text(separator='\n')  # Use '\n' for newline separation

        scraped_content += f"\n\n** URL: {url} **\n{content}\n"

        # Extract and process links recursively within allowed depth
        if depth > 0:
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/') and not href.startswith('/#'):  # Handle relative paths
                    absolute_url = urllib.robotparser.urljoin(url, href)
                    scraped_content = scrape_website(absolute_url, depth-1, scraped_content, robots_txt)

    return scraped_content

def main():
    """
    Prompts user for URL, depth, and output filename.
    Scrapes the website and stores content in a text file.
    """

    url = 'https://www.iit.edu/'
    depth = 2
    filename = 'scrpped.txt'

    robots_txt = urllib.robotparser.RobotFileParser()
    robots_txt.set_url(f"{url}/robots.txt")
    robots_txt.read()

    scraped_content = ""
    scraped_content = scrape_website(url, depth, scraped_content, robots_txt)

    with open(filename, 'w') as f:
        f.write(scraped_content)

    print(f"Scraped content saved to {filename}")

if __name__ == "__main__":
    main()
