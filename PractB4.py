
import random

# Predefined rules and responses
rules = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "hi": ["Hi!", "Nice to meet you!"],
    "how are you": ["I am fine!", "I am doing great!"],
    "name": ["I am ChatBot.", "You can call me ChatBot."],
    "help": ["Sure! How can I help you?"],
    "thank": ["You're welcome!", "No problem!"],
    "bye": ["Goodbye!", "See you later!"]
}

print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()
    found = False

    # Match user input with predefined patterns
    for pattern in rules:
        if pattern in user:
            print("ChatBot:", random.choice(rules[pattern]))
            found = True
            break

    # Exit the chatbot
    if "bye" in user:
        break

    # Default response if no pattern matches
    if not found:
        print("ChatBot: Sorry, I don't understand that.")
