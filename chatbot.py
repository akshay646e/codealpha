import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"(.*) your name?",
        ["I'm a chatbot created to assist you. What's your name?", "You can call me Chatbot. What about you?"]
    ],
    [
        r"how are you(.*)",
        ["I'm just a program, but I'm here to help you! How can I assist you today?", "I'm doing well, thank you! What can I help you with?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer basic questions, and provide information to the best of my ability.", "I'm here to assist with any queries you have. Try me!"]
    ],
    [
        r"(.*) created you?",
        ["I was created by a developer learning how to build chatbots!", "Someone curious about natural language processing created me."]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm based in the digital world, but I'm here for you anywhere you are!", "I'm wherever you need me to be."]
    ],
    [
        r"quit",
        ["Goodbye! It was nice chatting with you. Have a great day!", "See you later! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Interesting... Could you elaborate?"]
    ]
]

# Reflections (used to make conversations feel natural)
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hi! I am your friendly chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
