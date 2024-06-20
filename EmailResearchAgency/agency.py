from agency_swarm import Agency
from ResearchAgent import ResearchAgent
from EmailCEO import EmailCEO

email_ceo = EmailCEO()
research_agent = ResearchAgent()

agency = Agency([email_ceo, research_agent,
                 [email_ceo, research_agent]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    #completion_output = agency.get_completion("Hello, I have been tring to reach someone from your company for several days with no response.  I need to speak with someone as soon as possible!", yield_messages=False)
    #agency.run_demo()
    agency.demo_gradio()