from agency_swarm import Agency
from NegativeResponseAgent import NegativeResponseAgent
from PositiveResponseAgent import PositiveResponseAgent
from EmailCEO import EmailCEO

email_ceo = EmailCEO()
positive_response_agent = PositiveResponseAgent()
negative_response_agent = NegativeResponseAgent()

agency = Agency([email_ceo, positive_response_agent, negative_response_agent, [email_ceo, positive_response_agent],
                 [email_ceo, negative_response_agent]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.run_demo()