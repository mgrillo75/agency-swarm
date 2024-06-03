from agency_swarm.tools import BaseTool
from pydantic import Field
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

MODEL = "gpt-4o"

class SensitiveTextGenerationTool(BaseTool):
    """
    SensitiveTextGenerationTool generates text responses for emails categorized as negative.
    It uses OpenAI's latest GPT model to ensure the responses are sensitive and contextually appropriate,
    considering the negative sentiment of the email.
    """

    email_body: str = Field(
        ..., description="The body of the email to which the tool will generate a sensitive response."
    )
    tone: str = Field(
        default="empathetic", description="The tone of the response, which is empathetic by default."
    )

    def run(self):
        """
        Generates a sensitive response to the provided email body using the latest OpenAI GPT model.
        This method uses the chat completion API to simulate a conversation for generating responses.
        """
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a sensitive assistant."},
                {"role": "user", "content": f"Email: {self.email_body}"},
                {"role": "user", "content": f"Tone: {self.tone}"}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()

# Example usage:
# tool = SensitiveTextGenerationTool(email_body="I am unhappy with your service.", tone="empathetic")
# print(tool.run())