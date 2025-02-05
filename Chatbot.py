import random

def greet_user():
    greetings = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!', 'How’s it going?']
    return random.choice(greetings)

def respond_to_question(question):
    if 'how are you' in question.lower():
        return "I'm just a program, but I'm doing great! How about you?"
    elif 'name' in question.lower():
        return "I am a chatbot created by your Python script."
    elif 'hello' in question.lower() or 'hi' in question.lower():
        return greet_user()
    elif 'bye' in question.lower() or 'exit' in question.lower():
        return "Goodbye! It was nice talking to you!"
    else:
        return "Sorry, I don't understand that. Can you ask something else?"

def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Ask me anything or type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if 'exit' in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = respond_to_question(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    chatbot()
