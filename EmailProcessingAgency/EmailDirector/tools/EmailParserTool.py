from agency_swarm.tools import BaseTool
from pydantic import Field
from email import message_from_string
from typing import Dict

class EmailParserTool(BaseTool):
    """
    EmailParserTool extracts and parses the content from emails, identifying key information such as sender,
    recipient, subject, and body of the email.
    """

    email_content: str = Field(
        ..., description="The full content of the email as a raw string."
    )

    def run(self) -> Dict[str, str]:
        """
        Parses the email content and extracts the sender, recipient, subject, and body.
        
        Returns:
            A dictionary containing the sender, recipient, subject, and body of the email.
        """
        # Parse the email content into a message object
        message = message_from_string(self.email_content)
        
        # Extracting email details
        email_details = {
            "sender": message['from'],
            "recipient": message['to'],
            "subject": message['subject'],
            "body": self._get_email_body(message)
        }
        
        return email_details

    def _get_email_body(self, message) -> str:
        """
        Extracts the body of the email from the message object.
        
        Args:
            message: The parsed email message object.
        
        Returns:
            The body of the email as a string.
        """
        if message.is_multipart():
            # If the message is multipart, get the payload and join parts
            parts = [part.get_payload(decode=True).decode() for part in message.get_payload()]
            return "\n".join(parts)
        else:
            # If not multipart, just return the payload
            return message.get_payload(decode=True).decode()