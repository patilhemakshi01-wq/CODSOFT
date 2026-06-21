import random

# Responses database
responses = {
    "hello": ["Hi!", "Hello there!", "Hey!"],
    "how are you": ["I'm doing great!", "All good here!", "I'm fine 😊"],
    "name": ["I am your AI chatbot.", "Call me ChatBot!", "I'm your virtual assistant."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I didn't understand that."

def chatbot():
    print("Chatbot: Hello! Ask me anything (type 'bye' to exit)")

    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break

        reply = get_response(user)
        print("Chatbot:", reply)

chatbot()
