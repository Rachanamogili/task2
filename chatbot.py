import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r'hi|hello|hey',
     ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you ?',
     ['I am fine, thank you!', 'Fine, and you?', 'I feel great!']),
    (r'(.*) your name ?',
     ['I am a chatbot.', 'My name is Chatbot.']),
    (r'(.) help (.)',
     ['Sure, I can help you.', 'What do you need help with?']),
   ]
def chatbot():
    print("Hello! I am a chatbot. How can I help you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Bot:", response)

if _name_ == "_main_":
    chatbot()