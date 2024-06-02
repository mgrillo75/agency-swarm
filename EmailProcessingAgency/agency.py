from agency_swarm import Agency
from InternalAgent import InternalAgent
from VendorAgent import VendorAgent
from ClientAgent import ClientAgent
from EmailDirector import EmailDirector

emailDirector = EmailDirector()
clientAgent = ClientAgent()
vendorAgent = VendorAgent()
internalAgent = InternalAgent()

agency = Agency([emailDirector, [emailDirector, clientAgent],
                 [emailDirector, vendorAgent],
                 [emailDirector, internalAgent]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)
                
if __name__ == '__main__':
    agency.run_demo()