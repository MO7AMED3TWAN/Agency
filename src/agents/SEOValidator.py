from crewai import Agent, Task

class SEOValidator(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def validate(self, task: Task) -> bool:
        # Implement validation logic here
        pass