from crewai import Agent, Task

class Researcher(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def perform_task(self, task: Task):
        # Implement the logic for the Researcher agent to perform a task
        pass