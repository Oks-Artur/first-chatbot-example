import random

# Begrüßungen und Antworten des Bots
greetings = ["Hallo!", "Hi!", "Willkommen!"]
goodbyes = ["Tschüss!", "Bis bald!", "Auf Wiedersehen!"]
responses = {
    "wie geht's": ["Gut, danke!", "Super!", "Nicht schlecht."],
    "was machst du": ["Ich chatte mit dir!", "Ich lerne Python."],
    "default": ["Das verstehe ich nicht...", "Kannst du das anders formulieren?"]
}

def chatbot():
    print(random.choice(greetings))
    while True:
        user_input = input("Du: ").lower()
        if user_input in ["bye", "tschüss"]:
            print(random.choice(goodbyes))
            break
        response_found = False
        for key in responses:
            if key in user_input:
                print("Bot:", random.choice(responses[key]))
                response_found = True
                break
        if not response_found:
            print("Bot:", random.choice(responses["default"]))

chatbot()