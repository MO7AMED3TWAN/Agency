from crewai import Agent, Task

class Extractor(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def perform_task(self, task: Task):
        # Implement the logic for performing the task
        pass