from agency_swarm.agents import Agent


class EmailDirector(Agent):
    def __init__(self):
        super().__init__(
            name="EmailDirector",
            description="Responsible for initial sorting and contextual awareness using Zep's Perpetual Memory Integration and Feedback and Continuous Improvement features.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
