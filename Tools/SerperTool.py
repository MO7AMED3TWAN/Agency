# Serper API Tool
import requests

class SerperTool:
    def search(self, query):
        # Example logic to perform a search using Serper API
        headers = {"Authorization": "Bearer YOUR_API_KEY"}
        response = requests.get(f"https://api.serper.dev/search?q={query}", headers=headers)
        return response.json()
