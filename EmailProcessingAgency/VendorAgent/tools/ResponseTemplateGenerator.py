from agency_swarm.tools import BaseTool
from pydantic import Field
import random

class ResponseTemplateGenerator(BaseTool):
    """
    A tool to automatically generate response templates based on the input context and keywords.
    It creates diverse templates for different types of vendor communications, ensuring that the responses
    are personalized and contextually appropriate.
    """

    context: str = Field(
        ..., description="The context or scenario for which the response is needed."
    )
    keywords: list = Field(
        ..., description="List of keywords that should be included in the response template."
    )

    def run(self):
        """
        Generates a response template based on the context and keywords provided.
        """
        # Example templates
        templates = {
            "order": [
                "Thank you for your order of {keywords}. We will process it and send you a confirmation soon.",
                "We have received your order for {keywords} and are preparing it for shipment."
            ],
            "complaint": [
                "We are sorry to hear about your issue with {keywords}. We are looking into it and will get back to you shortly.",
                "Thank you for bringing this matter to our attention. We are actively working on resolving the issue with {keywords}."
            ],
            "inquiry": [
                "Thank you for your inquiry about {keywords}. Here's the information you requested.",
                "We appreciate your interest in {keywords}. I've gathered the information you need and am happy to assist you."
            ]
        }

        # Selecting a template based on context
        if self.context in templates:
            selected_template = random.choice(templates[self.context])
            response = selected_template.format(keywords=', '.join(self.keywords))
        else:
            response = "Thank you for reaching out. We will get back to you soon."

        return response

# Example usage:
# generator = ResponseTemplateGenerator(context="order", keywords=["product X", "product Y"])
# print(generator.run())