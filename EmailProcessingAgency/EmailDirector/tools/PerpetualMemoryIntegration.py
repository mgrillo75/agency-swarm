from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class PerpetualMemoryIntegration(BaseTool):
    """
    PerpetualMemoryIntegration integrates with Zep's Perpetual Memory to store and recall email interactions
    and preferences continuously.
    """

    api_url: str = Field(
        ..., description="The API endpoint for Zep's Perpetual Memory system."
    )
    api_key: str = Field(
        ..., description="API key for authenticating requests to Zep�s Perpetual Memory."
    )
    email_data: dict = Field(
        ..., description="Email interaction data to be stored or recalled."
    )
    operation: str = Field(
        ..., description="Specify the operation: 'store' to save data or 'recall' to retrieve data."
    )

    def run(self) -> dict:
        """
        Communicates with Zep�s Perpetual Memory API to store or recall email interactions and preferences.
        
        Returns:
            A dictionary containing the response from the Perpetual Memory API.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        if self.operation == 'store':
            response = requests.post(self.api_url, json=self.email_data, headers=headers)
        elif self.operation == 'recall':
            response = requests.get(f"{self.api_url}/{self.email_data['id']}", headers=headers)
        else:
            return {'error': 'Invalid operation specified'}

        return response.json()

# Example usage of the tool with hypothetical API details and email data
# tool_instance = PerpetualMemoryIntegration(
#     api_url="https://api.zepmemory.com/v1/emails",
#     api_key="your_api_key_here",
#     email_data={'id': '12345', 'subject': 'Important Meeting', 'body': 'Please confirm your attendance.'},
#     operation='store'
# )
# print(tool_instance.run())