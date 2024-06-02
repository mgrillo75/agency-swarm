from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Optional
import datetime

class EnhancedSearchCapabilities(BaseTool):
    """
    EnhancedSearchCapabilities provides advanced search functionalities within the email system, allowing users
    to query emails by keywords, date ranges, sender, or content type.
    """

    emails: List[dict] = Field(
        ..., description="A list of emails, where each email is a dictionary containing details like sender, recipient, date, subject, and body."
    )
    keywords: Optional[List[str]] = Field(
        default=None, description="List of keywords to search for in the email body or subject."
    )
    date_from: Optional[datetime.date] = Field(
        default=None, description="Start date for filtering emails."
    )
    date_to: Optional[datetime.date] = Field(
        default=None, description="End date for filtering emails."
    )
    sender: Optional[str] = Field(
        default=None, description="Email address of the sender to filter by."
    )
    content_type: Optional[str] = Field(
        default=None, description="Type of content to filter by (e.g., 'text/plain', 'text/html')."
    )

    def run(self) -> List[dict]:
        """
        Searches through the provided list of emails and filters them based on the specified criteria.
        
        Returns:
            A list of emails that match the search criteria.
        """
        filtered_emails = self.emails

        # Filter by sender
        if self.sender:
            filtered_emails = [email for email in filtered_emails if email['sender'] == self.sender]

        # Filter by date range
        if self.date_from and self.date_to:
            filtered_emails = [
                email for email in filtered_emails
                if datetime.datetime.strptime(email['date'], '%Y-%m-%d').date() >= self.date_from
                and datetime.datetime.strptime(email['date'], '%Y-%m-%d').date() <= self.date_to
            ]

        # Filter by keywords
        if self.keywords:
            filtered_emails = [
                email for email in filtered_emails
                if any(keyword.lower() in (email['subject'] + " " + email['body']).lower() for keyword in self.keywords)
            ]

        # Filter by content type
        if self.content_type:
            filtered_emails = [email for email in filtered_emails if email['content_type'] == self.content_type]

        return filtered_emails

# Example usage of the tool with hypothetical email data and search parameters
# tool_instance = EnhancedSearchCapabilities(
#     emails=[{'sender': 'example@example.com', 'date': '2023-01-01', 'subject': 'Meeting', 'body': 'Please confirm your attendance.', 'content_type': 'text/plain'}],
#     keywords=['meeting', 'attendance'],
#     date_from=datetime.date(2023, 1, 1),
#     date_to=datetime.date(2023, 1, 31),
#     sender='example@example.com',
#     content_type='text/plain'
# )
# print(tool_instance.run())