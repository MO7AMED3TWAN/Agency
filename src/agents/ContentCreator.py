from crewai import Agent, Task

class ContentCreator(Agent):
    def __init__(self, name: str):
        super().__init__(name)

    def perform_task(self, task: Task):
        if task.type == "content_creation":
            return f"Creating content for {task.details}"
        else:
            return f"Task type {task.type} not supported by ContentCreator"