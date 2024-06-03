from agency_swarm.tools import BaseTool
from pydantic import Field
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

MODEL = "gpt-4o"

class EmailSentimentAnalyzer(BaseTool):
    """
    A tool for analyzing the sentiment of email text using OpenAI's GPT model.
    It classifies the sentiment as positive, negative, or neutral.
    """

    email_text: str = Field(
        ..., description="The text content of the email to be analyzed for sentiment."
    )

    def run(self):
        """
        Analyze the sentiment of the email text using OpenAI's GPT model.
        """
        prompt = f"Analyze the sentiment of the following email text and classify it as positive, negative, or neutral, your response should only be one of those classification words:\n\n{self.email_text}\n\n"
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert in sentiment analysis."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )
        
        sentiment = response.choices[0].message.content.strip().lower()

        if sentiment in ["positive", "negative", "neutral"]:
            return sentiment
        else:
            return "neutral"

# Example usage:
# email_analyzer = EmailSentimentAnalyzer(email_text="I am very happy with your service!")
# result = email_analyzer.run()
# print(result)  # Output should be "positive", "negative", or "neutral"
