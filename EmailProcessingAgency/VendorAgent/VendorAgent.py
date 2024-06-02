from agency_swarm.agents import Agent


class VendorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="VendorAgent",
            description="Handles vendor communications, automating responses and categorizing emails.",
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
