import os
from zep_cloud.client import Zep

# Initialize the Zep client with your API key
client = Zep(api_key="z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ")

# Define the name for your new collection
collection_name = "emails"  # Collection names should be alphanumeric

# Create the "emails" collection in Zep
collection = client.document.delete_collection(collection_name)

