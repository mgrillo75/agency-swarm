from zep_cloud.client import AsyncZep

# Initialize the Zep client with your API key
client = AsyncZep(api_key="z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ")

# Define the users
users = [
    {
        "user_id": "client_agent",
        "email": "client.agent@agency.com",
        "first_name": "Client",
        "last_name": "Agent",
        "metadata": {"role": "Client Agent", "department": "Client Services"}
    },
    {
        "user_id": "internal_agent",
        "email": "internal.agent@agency.com",
        "first_name": "Internal",
        "last_name": "Agent",
        "metadata": {"role": "Internal Agent", "department": "Internal Affairs"}
    },
    {
        "user_id": "vendor_agent",
        "email": "vendor.agent@agency.com",
        "first_name": "Vendor",
        "last_name": "Agent",
        "metadata": {"role": "Vendor Agent", "department": "Vendor Relations"}
    }
]

# Function to add users
async def add_users():
    for user in users:
        new_user = await client.user.add(
            user_id=user['user_id'],
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            metadata=user['metadata']
        )
        print(f"Added user: {new_user.user_id}")

# Run the function to add users
import asyncio
asyncio.run(add_users())
