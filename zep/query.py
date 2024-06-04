import os
from zep_cloud.client import Zep

# Initialize the Zep client with your API key
client = Zep(api_key="z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ")

# Define the name for your new collection
collection_name = "emails"  # Collection names should be alphanumeric

# search for documents using only a query string
#query = "Siemens"
#results = client.document.search(collection_name, text=query, limit=5)

# hybrid search for documents using a query string and metadata filter
#metadata_query = {
#    "where": {"jsonpath": '$[*] ? (@.baz == "qux")'},
#}
#results2 = client.document.search(
#    collection_name, text=query, metadata=metadata_query, limit=5
#)

query = "Steam Automation temperature feedback PID loop"
results = client.document.search(
    collection_name="emails",
    text=query,
    limit=2  # Adjust the limit as needed
)
print(results)

# Print the collection object to confirm creation
#print("Query Results:", results)
#print("Query Results2:", results2)
