import openai
import os
import re
import string

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def exit_command(input_text):
    cleaned_input = input_text.lower().strip()
    exit_keywords = r"\b(quit|exit|bye)\b"
    return re.search(exit_keywords, cleaned_input) is not None

if __name__ == "__main__":
    print("Hi! I'm PyChat, how can I help you today?")
    print("To exit the chat, you can type 'quit', 'exit', or 'bye'.")

    while True:
        user_input = input("You: ")
        if exit_command(user_input):
            print("Bye! Have a great day!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)