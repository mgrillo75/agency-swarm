import os
import win32com.client
from zep_cloud.client import Zep
from zep_cloud.types import CreateDocumentRequest

def main():
    # Initialize the Zep client with your API key
    client = Zep(api_key="z_1dWlkIjoiMGE4MGI0NzAtODdhMS00M2JiLTlmYTgtYjNiZTdiMmE2ZWI2In0.5_ZtXnQJz_Xl6qKVltcZwt9h5G0hePNgTvEroq_0_3zCEuwY8WCswMt7xPQFY91-B_YYff8ouzJ6oyk9IFAKGQ")

    collection_name = "emails"
    
    # Load the existing collection
    collection = client.document.get_collection(collection_name)

    # Create an instance of the Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    customers_folder = namespace.Folders["miguel.grillo@awc-inc.com"].Folders.Item("Customers")
    sub_folder = customers_folder.Folders.Item("Dynamis")    

    # Get the most recent emails in the inbox folder
    messages = list(sub_folder.Items)
    messages.sort(key=lambda x: x.ReceivedTime, reverse=True)
    messages = messages[:20]

    # Define a batch size (e.g., 50 documents per batch)
    batch_size = 50

    # Iterate through the messages and add them to Zep in batches
    documents = []
    for i, message in enumerate(messages):
        try:
            sent_date = message.SentOn.strftime("%Y-%m-%d %H:%M:%S")
            if message.SenderEmailType == "EX":
                sender = message.Sender.GetExchangeUser().PrimarySmtpAddress
            else:
                sender = message.SenderEmailAddress
            
            document_id = f"{collection_name}-{i}"  # use an incrementing index to avoid long IDs
            # Ensure the document_id does not exceed 100 characters
            if len(document_id) > 100:
                document_id = document_id[:100]

            # Check if the content is not empty
            if not message.Body:
                print(f"Skipping email with empty body: {message.Subject}")
                continue

            documents.append(
                CreateDocumentRequest(
                    content=message.Body,
                    document_id=document_id,
                    metadata={
                        "date": sent_date,
                        "from": sender,
                        "subject": message.Subject,
                        "content_type": "email",
                    }
                )
            )

            # If the batch is full, send the documents
            if len(documents) == batch_size:
                try:
                    request = documents
                    uuids = client.document.add_documents(collection_name=collection_name, request=request)
                    print(f"Batch inserted with UUIDs: {uuids}")
                except Exception as e:
                    print(f"Error adding batch: {e}")
                # Clear the documents list for the next batch
                documents = []

        except Exception as e:
            print(f"Error processing message: {e}")

    # Add any remaining documents
    if documents:
        try:
            request = documents
            uuids = client.document.add_documents(collection_name=collection_name, request=request)
            print(f"Final batch inserted with UUIDs: {uuids}")
        except Exception as e:
            print(f"Error adding final batch: {e}")

if __name__ == "__main__":
    main()
