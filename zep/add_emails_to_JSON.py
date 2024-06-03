import os
import json
import win32com.client

def main():
    # Initialize the JSON structure
    data = []

    # Create an instance of the Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    customers_folder = namespace.Folders["miguel.grillo@awc-inc.com"].Folders.Item("Customers")
    sub_folder = customers_folder.Folders.Item("Dynamis")    

    # Get the most recent emails in the inbox folder
    messages = list(sub_folder.Items)
    messages.sort(key=lambda x: x.ReceivedTime, reverse=True)
    messages = messages[:20]

    # Iterate through the messages and add them to the data list
    for i, message in enumerate(messages):
        try:
            sent_date = message.SentOn.strftime("%Y-%m-%d %H:%M:%S")
            if message.SenderEmailType == "EX":
                sender = message.Sender.GetExchangeUser().PrimarySmtpAddress
            else:
                sender = message.SenderEmailAddress

            # Ensure the document_id does not exceed 100 characters
            document_id = f"email-{i}"  
            if len(document_id) > 100:
                document_id = document_id[:100]

            # Check if the content is not empty
            if not message.Body:
                print(f"Skipping email with empty body: {message.Subject}")
                continue

            # Append email data to the JSON structure
            data.append({
                "document_id": document_id,
                "content": message.Body,
                "metadata": {
                    "date": sent_date,
                    "from": sender,
                    "subject": message.Subject,
                    "content_type": "email",
                }
            })

        except Exception as e:
            print(f"Error processing message: {e}")

    # Save the data to a JSON file
    with open("email_training_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Email data saved to email_training_data.json")

if __name__ == "__main__":
    main()
