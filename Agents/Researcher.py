from crewai import Agent, Task

class Researcher:
    def __init__(self, llm):
        self.agent = Agent(
            role="Researcher Agent",
            goal="Performs targeted searches using provided keywords.",
            backstory="The agent searches Google and other sources, filters results by relevance and recency, and returns clean URLs with metadata.",
            llm=llm,
            verbose=True
        )

    def create_task(self, keywords, output_file):
        return Task(
            description=f"Search for the following keywords: {keywords}.",
            expected_output="A JSON object containing URLs and metadata.",
            output_file=output_file,
            agent=self.agent
        )
