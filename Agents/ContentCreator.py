from crewai import Agent, Task

class ContentCreator:
    def __init__(self, llm):
        self.agent = Agent(
            role="Content Creator Agent",
            goal="Generates original, SEO-optimized content with image description.",
            backstory="The agent produces original content, ensures logical flow, and optimizes for search engines.",
            llm=llm,
            verbose=True
        )

    def create_task(self, summaries, output_file):
        return Task(
            description=f"Create SEO-optimized content based on the following summaries: {summaries}.",
            expected_output="Generated content as a text file.",
            output_file=output_file,
            agent=self.agent
        )
