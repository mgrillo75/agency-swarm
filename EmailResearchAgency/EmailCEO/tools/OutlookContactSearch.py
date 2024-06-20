from agency_swarm.tools import BaseTool
from pydantic import Field
import win32com.client

class OutlookContactSearch(BaseTool):
    """
    A tool to search for a contact in Outlook's Contacts folder based on the first and last name,
    and display all available information for the found contact.
    """
    first_name: str = Field(
        ..., description="First name of the contact to search for."
    )
    last_name: str = Field(
        ..., description="Last name of the contact to search for."
    )

    def find_contact_by_name(self, namespace, first_name, last_name):
        """
        Searches for a contact in the Contacts folder based on the first and last name.
        """
        contacts_folder = namespace.GetDefaultFolder(10)  # 10 refers to the Contacts folder
        contacts = contacts_folder.Items

        for contact in contacts:
            if contact.FirstName == first_name and contact.LastName == last_name:
                return contact

        return None

    def display_contact_info(self, contact):
        """
        Displays all available information for the given contact.
        """
        contact_info = {
            "Full Name": contact.FullName,
            "Email": contact.Email1Address,
            "Business Phone": contact.BusinessTelephoneNumber,
            "Mobile Phone": contact.MobileTelephoneNumber,
            "Home Phone": contact.HomeTelephoneNumber,
            "Company": contact.CompanyName,
            "Job Title": contact.JobTitle,
            "Mailing Address": contact.MailingAddress,
        }
        return contact_info

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method utilizes the fields defined above to perform the task.
        """
        # Create an instance of the Outlook application
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        # Search for the contact
        contact = self.find_contact_by_name(namespace, self.first_name, self.last_name)

        if contact:
            return self.display_contact_info(contact)
        else:
            return f"No contact found with name {self.first_name} {self.last_name}"

# Example usage:
# tool = OutlookContactSearch(first_name="John", last_name="Doe")
# result = tool.run()
# print(result)
