from crewai import Agent, Task

class Extractor:
    def __init__(self, llm):
        self.agent = Agent(
            role="Extractor Agent",
            goal="Analyzes collected pages to extract core information.",
            backstory="The agent visits URLs, extracts main content, detects keywords, and creates summaries.",
            llm=llm,
            verbose=True
        )

    def create_task(self, urls, output_file):
        return Task(
            description=f"Extract core information from the following URLs: {urls}.",
            expected_output="A JSON object containing extracted summaries and keywords.",
            output_file=output_file,
            agent=self.agent
        )
