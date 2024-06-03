from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import requests

class AutomatedCommunicationScripts(BaseTool):
    """
    AutomatedCommunicationScripts automates the creation and execution of communication scripts, enabling the
    agent to handle routine client interactions without manual input.
    """

    script_api_url: str = Field(
        ..., description="The API endpoint for retrieving and executing communication scripts."
    )
    client_interaction_type: str = Field(
        ..., description="The type of client interaction for which the script is needed (e.g., 'greeting', 'follow-up')."
    )
    client_details: dict = Field(
        ..., description="Details about the client that may influence the script's content."
    )

    def run(self) -> str:
        """
        Retrieves and executes a communication script based on the client interaction type and client details.
        
        Returns:
            A string containing the executed script or an error message if the script could not be retrieved.
        """
        # Prepare the request payload
        payload = {
            'interaction_type': self.client_interaction_type,
            'client_details': json.dumps(self.client_details)
        }
        
        # Make the API request to retrieve the script
        response = requests.post(self.script_api_url, json=payload)
        if response.status_code == 200:
            script_content = response.json().get('script', 'No script available for this interaction type.')
            # Simulate script execution (in a real scenario, this might involve sending an email or message)
            executed_script = f"Script executed: {script_content}"
        else:
            executed_script = "Failed to retrieve script due to an error with the script service."

        return executed_script

# Example usage of the tool with hypothetical API details and client interaction type
# tool_instance = AutomatedCommunicationScripts(
#     script_api_url="https://api.scriptservice.com/v1/scripts",
#     client_interaction_type='greeting',
#     client_details={'client_name': 'John Doe', 'client_status': 'new'}
# )
# print(tool_instance.run())