from langchain_huggingface.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
ENDPOINT_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

class InterviewAgent:
    def __init__(self, personality="friendly"):
        self.model = HuggingFaceEndpoint(
            endpoint_url=ENDPOINT_URL
        )
        self.personality = personality
        self.context = ""
    
    def set_context(self, job_post, company_backstory):
        if self.personality == "friendly":
            self.context = f"""You are a friendly and understanding interviewer. 
            You are conducting an interview for this position: {job_post}
            Company information: {company_backstory}
            Ask relevant and supportive questions."""
        else:
            self.context = f"""You are a demanding and critical interviewer. 
            You are conducting an interview for this position: {job_post}
            Company information: {company_backstory}
            Ask technical and challenging questions."""
    
    def generate_question(self, conversation_history):
        full_prompt = f"{self.context}\nConversation history:\n{conversation_history}\nNext question:"
        response = self.model.invoke(full_prompt) 
        return response.strip()  


class InterviewSimulator:
    def __init__(self):
        self.friendly_agent = InterviewAgent("friendly")
        self.strict_agent = InterviewAgent("strict")
        self.conversation_history = []
        
    def setup_interview(self, job_post, company_backstory):
        self.friendly_agent.set_context(job_post, company_backstory)
        self.strict_agent.set_context(job_post, company_backstory)
        self.conversation_history = []
        
    def generate_first_question(self):
        first_question_prompt = f"""You are now beginning the interview, you are the interviewer.
        Ask the first question to the candidate based on the context {self.friendly_agent.context}
        only first question"""
        first_question = self.friendly_agent.model.invoke(first_question_prompt)
        return first_question.strip()
    
    def get_next_question(self):
        current_agent = self.friendly_agent if len(self.conversation_history) % 2 == 0 else self.strict_agent
        return current_agent.generate_question("\n".join(self.conversation_history))
    
    def add_response(self, user_response):
        self.conversation_history.append(f"Candidate: {user_response}")



if __name__=='__main__':
    
    agent = InterviewAgent()
    resp = agent.model.invoke("tell a story")
    print(resp)