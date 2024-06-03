from agency_swarm.tools import BaseTool
from pydantic import Field
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

MODEL = "gpt-4o"

class PositiveTextGenerationTool(BaseTool):
    """
    PositiveTextGenerationTool generates text responses for emails categorized as positive or neutral.
    It uses OpenAI's latest GPT model to ensure the responses are coherent and contextually appropriate.
    """

    email_body: str = Field(
        ..., description="The body of the email to which the tool will generate a response."
    )
    tone: str = Field(
        ..., description="The desired tone of the response, should be 'positive' or 'neutral'."
    )

    def run(self):
        """
        Generates a response to the provided email body using the latest OpenAI GPT model.
        This method uses the chat completion API to simulate a conversation for generating responses.
        """
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Email: {self.email_body}"},
                {"role": "user", "content": f"Tone: {self.tone}"}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

# Example usage:
# tool = PositiveTextGenerationTool(email_body="Thank you for your inquiry about our services.", tone="positive")
# print(tool.run())