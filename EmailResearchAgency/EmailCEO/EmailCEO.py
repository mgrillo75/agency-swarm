from agency_swarm.agents import Agent


class EmailCEO(Agent):
    def __init__(self):
        super().__init__(
            name="EmailCEO",
            description="This agent analyzes incoming emails to determine their sentiment, searches for historical information related to the email content using the Zep Long-Term Memory for AI Assistance framework, and sends a summary of the historical information back to the user",
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
