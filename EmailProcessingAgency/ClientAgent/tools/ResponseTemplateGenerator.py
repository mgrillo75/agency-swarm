from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List

class ResponseTemplateGenerator(BaseTool):
    """
    ResponseTemplateGenerator generates response templates for various client interactions, allowing the agent
    to quickly and effectively communicate with clients based on predefined scenarios.
    """

    scenarios: List[str] = Field(
        ..., description="List of scenarios for which response templates are needed."
    )
    template_database: Dict[str, str] = Field(
        ..., description="A dictionary mapping scenarios to their respective response templates."
    )

    def run(self) -> Dict[str, str]:
        """
        Generates response templates based on the provided scenarios.
        
        Returns:
            A dictionary containing the scenarios and their corresponding response templates.
        """
        response_templates = {}
        for scenario in self.scenarios:
            template = self.template_database.get(scenario, "No template available for this scenario.")
            response_templates[scenario] = template
        return response_templates

# Example usage of the tool with hypothetical scenarios and a template database
# tool_instance = ResponseTemplateGenerator(
#     scenarios=['product_inquiry', 'service_feedback', 'appointment_request'],
#     template_database={
#         'product_inquiry': 'Thank you for your inquiry about our products. Here are the details...',
#         'service_feedback': 'We appreciate your feedback and are continuously working to improve our services.',
#         'appointment_request': 'Please let us know your preferred date and time for the appointment.'
#     }
# )
# print(tool_instance.run())