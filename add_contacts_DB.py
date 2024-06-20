import os
import sqlite3
import win32com.client

# Database connection setup
db_path = 'contact_management.db'
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"Successfully connected to the database: {db_path}")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Function to determine classification from company name or contact name
def determine_classification(name, company, entity_list):
    for entity in entity_list:
        if entity.lower() in name.lower() or entity.lower() in company.lower():
            return entity
    return None

def main():
    # Lists of entities
    customers = [
        "BeUSA Energy", "Cameron", "CAM", "C-A-M", "Cameron (Singapore) Pte Ltd", "Cameron Intl Corp", "Cameron Italy Srl",
        "Cameron Romania S.R.L.", "Cameron Solutions Inc", "Cameron Technologies Us", "Champion Technology", "Dynamis Power Solutions, LLC",
        "Dynamis", "Electro-Quip Service", "Electro-Tech Industries, Inc", "Eml Manufacturing", "En Engineering, Llc Tx",
        "Enquest Energy Solutions", "Evolution Well Serv Oper Taxable", "Evolution Well Services Llc", "Evolution Well Services",
        "HMH", "HMHW", "Hydril Pcb Limited", "Hydril Usa Distri - Ers Acct", "Hydril Usa Distribution Llc", "Hydril Usa, Distri - Ers Orders",
        "Jelec Usa", "Jelec", "Kinetic Pressure Control Limited", "Shear Anything", "Mako Deepwater Inc", "M-I  L.L.C", "M-I, Llc",
        "Nextier Completion Solutions", "Quadvest", "Schlumberger Middle East, S.A.Saudi", "Schlumberger Rig Technology Inc.",
        "Schlumberger Tech Co", "Schlumberger Tech Corp-Taxable Acct", "Schlumberger Technology Corp", "Schlumberger", "SLB",
        "Sensia -Cameron Technologies Us Llc", "Sweco (M-I, Llc)", "Trendsetter Engineering"
    ]
    vendors = [
        "Adalet Enclosures", "Appleton Group", "Banner Engineering", "Burndy USA Inc.", "c3controls", "Cashco, Inc.",
        "Cooper Industries", "Dynapar", "Eaton", "Electrical Div Misc.", "Electrical Mfgs.", "Engineering Services",
        "Erico/Caddy", "E-T-A", "Farris", "Finder", "Gyrolok", "Hammond Mfg. Co.", "Hoke Inc.", "Iboco", "Instrumentation Misc",
        "Jamesbury", "Kenco Engineering", "Killark", "Linc - Milton Roy", "Littelfuse", "Mersen", "Metso Repair Parts",
        "Mission Communicatio", "Moxa", "Pepperl+Fuchs", "Phoenix Contact", "Pulsar", "R STAHL", "Red Lion", "Repair Items",
        "Rittal Corporation", "Siemens", "Siemens Instruments", "Specialized Mfg", "Stonel Division", "Training", "Turck Inc.",
        "Valve Miscellaneous", "Weidmuller", "WIKA Instrument Corp", "WIKA Temperature", "Worcester Controls"
    ]

    # Create an instance of the Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    contacts_folder = namespace.GetDefaultFolder(10)  # 10 corresponds to the Contacts folder

    # Get all contacts in the contacts folder
    contacts = contacts_folder.Items

    for contact in contacts:
        try:
            name = contact.FullName
            email = contact.Email1Address
            company = contact.CompanyName
            phone = contact.BusinessTelephoneNumber

            classification = None
            if company:
                if determine_classification(name, company, customers):
                    classification = "Customer"
                    table = "customers"
                elif determine_classification(name, company, vendors):
                    classification = "Vendor"
                    table = "vendors"
                elif "AWC" in name or "AWC" in company:
                    classification = "AWC"
                    table = "awc_contacts"

                if classification:
                    print(f"Adding {classification}: {name}, {email}, {phone}, {company}")
                    if table == "customers":
                        cursor.execute(f'''
                        INSERT OR IGNORE INTO {table} (customer_name, customer_email, phone, address, city, state, postal_code, country)
                        VALUES (?, ?, ?, ?, '', '', '', '')
                        ''', (name, email, phone, company))
                    elif table == "vendors":
                        cursor.execute(f'''
                        INSERT OR IGNORE INTO {table} (vendor_name, vendor_email, phone, address, city, state, postal_code, country)
                        VALUES (?, ?, ?, ?, '', '', '', '')
                        ''', (name, email, phone, company))
                    elif table == "awc_contacts":
                        cursor.execute(f'''
                        INSERT OR IGNORE INTO {table} (contact_name, contact_email, phone, department)
                        VALUES (?, ?, ?, ?)
                        ''', (name, email, phone, company))
                    conn.commit()
                    print(f"Contact {name} added to {table} table.")

        except Exception as e:
            print(f"Failed to process contact: {str(e)}")

    print("Contacts have been added to the database.")
    conn.close()

if __name__ == "__main__":
    main()
