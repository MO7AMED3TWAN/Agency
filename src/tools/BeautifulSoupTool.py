from bs4 import BeautifulSoup

class BeautifulSoupTool:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def find_element_by_id(self, element_id):
        return self.soup.find(id=element_id)

    def find_elements_by_class(self, class_name):
        return self.soup.find_all(class_=class_name)

    def get_text(self, element):
        return element.get_text() if element else None

    def get_attribute(self, element, attribute):
        return element.get(attribute) if element else None