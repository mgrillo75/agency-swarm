import os
from zep_cloud.client import Zep

# Initialize the Zep client with your API key
client = Zep(api_key="z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ")

# Define the name for your new collection
collection_name = "emails"  # Collection names should be alphanumeric

# Create the "emails" collection in Zep
collection = client.document.add_collection(
    collection_name,  # Required: the name of the collection
    description="Collection dedicated to storing and managing email threads and communications",  # Optional: description of the collection
    metadata={
        "content_type": "email_threads", 
        "data_classification": "internal",
        "owner": "email_management_system",
        "retention_policy": "6_months",
        "encryption": "enabled",
        "access_control": {
            "read": ["support_team", "admin"],
            "write": ["support_team"],
            "delete": ["admin"]
        }
    }   # Optional: metadata describing the collection purpose
)

# Print the collection object to confirm creation
print("Collection created:", collection)
