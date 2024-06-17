from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from zep_cloud.client import Zep

# Define the constant variables
API_KEY = "z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ"
COLLECTION_NAME = "emails"

class ZepEmailSearchTool(BaseTool):
    """
    A tool to interact with the Zep collection named 'emails' for searching through 12 months' worth of email history using vector similarity search and metadata filtering.
    """
    query: str = Field(..., description="The search query to find relevant emails.")
    metadata_filter: dict = Field(None, description="Optional metadata filter to refine search results.")
    limit: int = Field(5, description="The maximum number of results to return.")

    def run(self):
        """
        The implementation of the run method to search the 'emails' collection based on the provided query, metadata filter, and limit.
        """
        client = Zep(api_key=API_KEY)

        # Load the existing collection
        collection = client.document.get_collection(COLLECTION_NAME)
        if not collection:
            return "The 'emails' collection does not exist."

        # Perform the search
        search_params = {
            "text": self.query,
            "limit": self.limit
        }
        if self.metadata_filter:
            search_params["metadata"] = self.metadata_filter

        results = client.document.search(COLLECTION_NAME, **search_params)
        
        # Process and return the results
        if not results:
            return "No results found for the given query."
        
        return results

# Example usage:
# search_tool = ZepEmailSearchTool(query="project update", metadata_filter={"where": {"jsonpath": '$[*] ? (@.sender == "john.doe@example.com")'}}, limit=5)
# results = search_tool.run()
# print(results)
