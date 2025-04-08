import requests

class GoogleSearchTool:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()