from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class AutomatedCommunicationScripts(BaseTool):
    """
    A tool to create and manage automated communication scripts using the Zep platform.
    This tool integrates with Zep to facilitate the creation, modification, and deployment of scripts
    that can handle routine vendor inquiries and responses.
    """

    zep_api_url: str = Field(
        ..., description="The API endpoint for the Zep platform."
    )
    zep_api_key: str = Field(
        ..., description="API key for authenticating requests to the Zep platform."
    )
    script_name: str = Field(
        ..., description="Name of the script to be created or modified."
    )
    script_content: str = Field(
        ..., description="Content of the script in Zep's specified format."
    )
    operation: str = Field(
        ..., description="Operation to perform: 'create', 'update', or 'deploy'."
    )

    def run(self):
        """
        Connects to the Zep platform and performs the specified operation on the communication script.
        """
        headers = {
            "Authorization": f"Bearer {self.zep_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "name": self.script_name,
            "content": self.script_content
        }
        if self.operation == "create":
            response = requests.post(f"{self.zep_api_url}/scripts", headers=headers, json=data)
        elif self.operation == "update":
            response = requests.put(f"{self.zep_api_url}/scripts/{self.script_name}", headers=headers, json=data)
        elif self.operation == "deploy":
            response = requests.post(f"{self.zep_api_url}/deploy/{self.script_name}", headers=headers)
        else:
            return "Invalid operation specified."

        if response.status_code in [200, 201]:
            return f"Script {self.operation} successful: {response.json()}"
        else:
            return f"Error {self.operation} script: {response.text}"

# Example usage:
# scripts_tool = AutomatedCommunicationScripts(
#     zep_api_url="https://api.zepplatform.com",
#     zep_api_key="your_api_key_here",
#     script_name="VendorInquiryHandler",
#     script_content="print('Hello, world!')",
#     operation="create"
# )
# print(scripts_tool.run())