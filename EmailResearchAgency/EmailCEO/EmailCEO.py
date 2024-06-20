from agency_swarm.agents import Agent


class EmailCEO(Agent):
    def __init__(self):
        super().__init__(
            name="EmailCEO",
            description="This agent analyzes incoming emails to determine their sentiment, identifies the sender of the email, and interacts with the ResearchAgent to gather historical information related to the email.",
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
