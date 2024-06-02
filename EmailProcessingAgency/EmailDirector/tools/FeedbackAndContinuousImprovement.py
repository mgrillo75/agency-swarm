from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class FeedbackAndContinuousImprovement(BaseTool):
    """
    FeedbackAndContinuousImprovement collects user feedback on email management and uses it to continuously
    improve the email sorting and classification algorithms.
    """

    feedback_api_url: str = Field(
        ..., description="The API endpoint for submitting feedback."
    )
    feedback_data: dict = Field(
        ..., description="User feedback data including user ID, feedback text, and related email ID."
    )
    improvement_api_url: str = Field(
        ..., description="The API endpoint for updating the email classification model."
    )
    model_update_data: dict = Field(
        ..., description="Data used to update the email classification model, including feedback insights and model parameters."
    )

    def run(self) -> dict:
        """
        Submits user feedback to the feedback API and sends data to the improvement API to update the email classification model.
        
        Returns:
            A dictionary containing the responses from both the feedback submission and model update processes.
        """
        # Submit feedback
        feedback_response = requests.post(self.feedback_api_url, json=self.feedback_data)
        feedback_result = feedback_response.json()

        # Update classification model
        if feedback_response.status_code == 200:
            update_response = requests.post(self.improvement_api_url, json=self.model_update_data)
            update_result = update_response.json()
        else:
            update_result = {'error': 'Feedback submission failed, model update not attempted'}

        return {
            'feedback_result': feedback_result,
            'model_update_result': update_result
        }

# Example usage of the tool with hypothetical API details and data
# tool_instance = FeedbackAndContinuousImprovement(
#     feedback_api_url="https://api.feedback.com/v1/feedback",
#     feedback_data={'user_id': '123', 'feedback_text': 'Sorting could be improved for urgent emails.', 'email_id': '456'},
#     improvement_api_url="https://api.improvement.com/v1/update_model",
#     model_update_data={'feedback_id': '789', 'new_parameters': {'urgency_threshold': 0.8}}
# )
# print(tool_instance.run())