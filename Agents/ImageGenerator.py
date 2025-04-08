from crewai import Agent, Task

class ImageGenerator:
    def __init__(self, llm):
        self.agent = Agent(
            role="Image Generator Agent",
            goal="Creates visuals based on content descriptions.",
            backstory="The agent generates images, ensures proper dimensions, and maintains brand consistency.",
            llm=llm,
            verbose=True
        )

    def create_task(self, description, output_file):
        return Task(
            description=f"Generate an image based on the following description: {description}.",
            expected_output="Generated image file.",
            output_file=output_file,
            agent=self.agent
        )
