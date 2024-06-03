from agency_swarm.tools import BaseTool
from pydantic import Field
import random

class ResponseTemplateGenerator(BaseTool):
    """
    A tool to automatically generate response templates based on the input context and keywords.
    It can create diverse templates for different types of internal communications, ensuring that
    the responses are personalized and contextually appropriate.
    """

    context: str = Field(
        ..., description="The context or scenario for which the response is needed."
    )
    keywords: list = Field(
        ..., description="List of keywords that should be included in the response."
    )

    def run(self):
        """
        Generates a response template based on the provided context and keywords.
        """
        # Template database simulation
        templates = {
            "greeting": [
                "Hello {name}, hope you're doing well!",
                "Hi {name}, thank you for reaching out!"
            ],
            "feedback": [
                "Thank you for your feedback regarding {topic}, we will consider it carefully.",
                "We appreciate your thoughts on {topic} and will discuss it in our next meeting."
            ],
            "request": [
                "Could you please provide more details on {detail}?",
                "We need additional information about {detail} to proceed."
            ]
        }

        # Select templates based on context
        selected_templates = templates.get(self.context, ["Thank you for your message."])

        # Personalize templates with keywords
        personalized_templates = [
            template.format(name=random.choice(self.keywords), topic=random.choice(self.keywords), detail=random.choice(self.keywords))
            for template in selected_templates
        ]

        return personalized_templates

# Example usage:
# generator = ResponseTemplateGenerator(
#     context="feedback",
#     keywords=["project Alpha", "timeline adjustment", "John Doe"]
# )
# print(generator.run())