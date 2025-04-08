# BeautifulSoup Tool
from bs4 import BeautifulSoup

class BeautifulSoupTool:
    def extract_content(self, html):
        # Logic to extract content from HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()
