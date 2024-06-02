from agency_swarm.agents import Agent


class InternalAgent(Agent):
    def __init__(self):
        super().__init__(
            name="InternalAgent",
            description="Manages internal communications and task distribution within the organization.",
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
