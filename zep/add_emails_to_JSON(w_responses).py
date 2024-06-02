import os
import json
import win32com.client

def main():
    # Initialize the JSON structure
    data = []

    # Create an instance of the Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    sent_folder = namespace.GetDefaultFolder(5)  # 5 corresponds to the Sent Items folder

    # Get the most recent emails in the sent folder
    messages = list(sent_folder.Items)
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

            # Find the original email this message is responding to if it exists
            original_email = None
            for original_message in messages:
                if message.Subject.startswith("Re:") and message.ConversationID == original_message.ConversationID:
                    original_email = original_message
                    break

            # Append email data to the JSON structure
            email_entry = {
                "document_id": document_id,
                "response": {
                    "content": message.Body,
                    "metadata": {
                        "date": sent_date,
                        "from": sender,
                        "subject": message.Subject,
                        "content_type": "email",
                    }
                },
                "original_email": None
            }

            if original_email:
                original_date = original_email.SentOn.strftime("%Y-%m-%d %H:%M:%S")
                if original_email.SenderEmailType == "EX":
                    original_sender = original_email.Sender.GetExchangeUser().PrimarySmtpAddress
                else:
                    original_sender = original_email.SenderEmailAddress

                email_entry["original_email"] = {
                    "content": original_email.Body,
                    "metadata": {
                        "date": original_date,
                        "from": original_sender,
                        "subject": original_email.Subject,
                        "content_type": "email",
                    }
                }

            data.append(email_entry)

        except Exception as e:
            print(f"Error processing message: {e}")

    # Save the data to a JSON file
    with open("email_training_data_with_responses.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Email data with responses saved to email_training_data_with_responses.json")

if __name__ == "__main__":
    main()
