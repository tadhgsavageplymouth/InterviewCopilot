import openai_interview.openai_api as openai_api
import nao_communication.nao_client as nao_client

class InterviewManager:
    def __init__(self, topic, nao_ip):
        self.topic = topic
        self.client = nao_client.NaoClient(nao_ip)
        self.previous_answer = None

    def conduct_interview(self):
        while True:
            question = openai_api.generate_question(self.topic, self.previous_answer)
            print(f"NAO asks: {question}")
            self.client.send_message(question)
            user_answer = input("Your answer (or type 'exit' to quit): ")
            if user_answer.lower() == 'exit':
                break
            self.previous_answer = user_answer

    def close(self):
        self.client.close()
