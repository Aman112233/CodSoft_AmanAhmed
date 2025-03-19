import re

rules = {
    r'.*(hi|hello|hey|greetings).*': ['Hello!', 'Hi there!', 'Hey!'],
    r'.*(how are you|how are you doing|what\'s up|how\'s it going).*': ['I am just a computer program, so I don\'t have feelings, but I\'m here to assist you!', 'I don\'t have feelings, but I\'m here and ready to help!'],
    r'.*(bye|goodbye|see you|farewell).*': ['Goodbye!', 'See you later!', 'Have a great day!'],
    r'.*(name|your name|who are you).*': ['I am a chatbot created to assist you!'],
    r'.*(help me|assist me).*': ['Of course! What do you need assistance with?'],
    r'.*(joke|tell me a joke).*': [
        'Sure, here\'s a joke: Why did the chicken cross the road? To get to the other side!',
        'Here\'s one: Why don\'t scientists trust atoms? Because they make up everything!',
        'How about this one: Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them!'
    ],
    r'.*(thanks|thank you|appreciate it).*': ['You\'re welcome!', 'No problem, happy to help!', 'Anytime!'],
    r'.*(weather|forecast|temperature).*': ['Sorry, I can\'t provide real-time weather updates, but you can check your local weather app!'],
    r'.*(tell me a fact|interesting fact).*': [
        'Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!',
        'Here\'s an interesting fact: A group of flamingos is called a "flamboyance."',
        'Did you know? Sloths can hold their breath longer than dolphins can, up to 40 minutes!'
    ],
    r'.*(who won|who\'s the winner|who won the game).*': ['I\'m not sure about that! You can check the latest sports news for updates.'],
    r'.*(time|current time).*': ['I can\'t give you the current time, but you can easily check your device for that!'],
    r'.*(good morning|morning).*': ['Good morning! How can I assist you today?'],
    r'.*(good night|night).*': ['Good night! Sleep well and take care!'],
    r'.*(what is your purpose|what do you do).*': ['I am here to assist with any questions or tasks you have, from simple chat to providing information!'],
    r'.*(can you sing|sing).*': ['I can\'t sing, but I can share a song lyric with you! Want me to do that?'],
    r'.*(what is ai|define ai).*': ['AI, or Artificial Intelligence, is the simulation of human intelligence in machines that are programmed to think and learn like humans.'],
    r'.*(what is your favorite color).*': ['I don\'t have a favorite color, but I think blue looks calming.'],
    r'.*(who made you).*': ['I was created by developers to assist with various tasks and provide helpful responses.'],
    r'.*(how can I learn programming).*': ['There are many ways to learn programming! You can start with languages like Python, JavaScript, or Java. There are great resources online like Codecademy, freeCodeCamp, and Coursera.'],
    r'.*(tell me about computers).*': ['Computers are devices that can store, retrieve, and process data. They are made up of hardware and software that work together to perform tasks and solve problems.'],
}

def simple_chatbot(user_input):
    for pattern, responses in rules.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            # Return a random response from the matched rule
            return responses[0]
    return "I didn't quite understand that. Could you try again?"

def interactive_conversation():
    print("Chatbot: Hi! How can I assist you today? (type 'exit' to end)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = simple_chatbot(user_input)
            print("Chatbot:", response)

interactive_conversation()