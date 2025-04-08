from crewai import Agent, Task

class SEOValidator:
    def __init__(self, llm):
        self.agent = Agent(
            role="SEO Validator Agent",
            goal="Verifies content meets search engine requirements.",
            backstory="The agent checks keyword usage, heading structure, readability, and meta elements.",
            llm=llm,
            verbose=True
        )

    def create_task(self, content, output_file):
        return Task(
            description=f"Validate the SEO quality of the following content: {content}.",
            expected_output="SEO analysis report as a JSON object.",
            output_file=output_file,
            agent=self.agent
        )
