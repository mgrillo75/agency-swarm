from agency_swarm.agents import Agent


class NegativeResponseAgent(Agent):
    def __init__(self):
        super().__init__(
            name="NegativeResponseAgent",
            description="This agent drafts responses for emails categorized as negative, with access to sensitive handling protocols.",
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
