from crewai import Agent, Task

class ImageGenerator(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def generate_image(self, prompt: str) -> str:
        task = Task("generate_image", {"prompt": prompt})
        result = self.execute_task(task)
        return result.get("image_url", "")