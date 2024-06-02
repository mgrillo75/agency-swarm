from agency_swarm.tools import BaseTool
from pydantic import Field
import datetime
from typing import List, Optional

class EnhancedSearchCapabilities(BaseTool):
    """
    EnhancedSearchCapabilities provides advanced search functionalities within the client management system,
    allowing users to query client interactions by keywords, date ranges, or interaction type.
    """

    keywords: Optional[List[str]] = Field(
        default=None, description="List of keywords to search within client interactions."
    )
    date_from: Optional[datetime.date] = Field(
        default=None, description="Start date for the search range."
    )
    date_to: Optional[datetime.date] = Field(
        default=None, description="End date for the search range."
    )
    interaction_type: Optional[str] = Field(
        default=None, description="Type of client interaction to filter by."
    )

    def run(self) -> List[dict]:
        """
        Executes a search query within the client management system based on the provided criteria.
        
        Returns:
            A list of dictionaries, each representing a client interaction that matches the search criteria.
        """
        # Simulate database or API call to retrieve client interactions
        # This is a placeholder for demonstration purposes
        all_interactions = [
            {'date': datetime.date(2023, 1, 15), 'type': 'email', 'content': 'Inquiry about product availability'},
            {'date': datetime.date(2023, 1, 20), 'type': 'call', 'content': 'Follow-up on previous support ticket'},
            {'date': datetime.date(2023, 1, 25), 'type': 'email', 'content': 'Request for product return'}
        ]

        # Filter interactions based on the provided criteria
        filtered_interactions = [
            interaction for interaction in all_interactions
            if (not self.keywords or any(keyword in interaction['content'] for keyword in self.keywords))
            and (not self.date_from or self.date_from <= interaction['date'])
            and (not self.date_to or interaction['date'] <= self.date_to)
            and (not self.interaction_type or interaction['type'] == self.interaction_type)
        ]

        return filtered_interactions

# Example usage of the tool with hypothetical search criteria
# tool_instance = EnhancedSearchCapabilities(
#     keywords=['product', 'return'],
#     date_from=datetime.date(2023, 1, 10),
#     date_to=datetime.date(2023, 1, 30),
#     interaction_type='email'
# )
# print(tool_instance.run())