# Readability Tool

from readability import Document

class ReadabilityTool:
    def simplify(self, html):
        doc = Document(html)
        return doc.summary()
