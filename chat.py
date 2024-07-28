import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":

    print("Hi! I'm PyChat, how can I help you today?")
    print("To exit the chat, you can type 'quit', 'exit', or 'bye'.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bye! Have a great day!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)