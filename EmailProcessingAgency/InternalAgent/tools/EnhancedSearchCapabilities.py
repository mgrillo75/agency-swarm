from agency_swarm.tools import BaseTool
from pydantic import Field
from datetime import datetime
import json

class EnhancedSearchCapabilities(BaseTool):
    """
    A tool to enhance the search capabilities within the internal communication system.
    It provides advanced search options, including filtering by date, keyword, and relevance,
    to quickly retrieve specific communications or information.
    """

    communications_data: list = Field(
        ..., description="List of communications in JSON format."
    )
    search_keyword: str = Field(
        ..., description="Keyword to search within the communications."
    )
    start_date: datetime = Field(
        ..., description="Start date for filtering communications."
    )
    end_date: datetime = Field(
        ..., description="End date for filtering communications."
    )

    def run(self):
        """
        Filters and searches communications based on the provided keyword and date range.
        """
        # Filter communications by date range
        filtered_communications = [
            comm for comm in self.communications_data
            if self.start_date <= datetime.strptime(comm['date'], '%Y-%m-%d') <= self.end_date
        ]

        # Search for the keyword in the filtered communications
        search_results = [
            comm for comm in filtered_communications
            if self.search_keyword.lower() in comm['content'].lower()
        ]

        # Sort results by relevance (example: number of keyword occurrences)
        search_results.sort(key=lambda x: x['content'].lower().count(self.search_keyword.lower()), reverse=True)

        return json.dumps(search_results, indent=4)

# Example usage:
# communications_data = [
#     {"date": "2023-01-10", "content": "Meeting about the new project proposal."},
#     {"date": "2023-01-15", "content": "Please review the urgent invoice for the recent project."},
#     {"date": "2023-01-20", "content": "Updated contract details for review and feedback."},
# ]
# search_tool = EnhancedSearchCapabilities(
#     communications_data=communications_data,
#     search_keyword="project",
#     start_date=datetime(2023, 1, 10),
#     end_date=datetime(2023, 1, 20)
# )
# print(search_tool.run())