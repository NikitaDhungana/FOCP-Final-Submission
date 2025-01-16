import random
import json
import time

# Load keywords and responses from a configuration file
def load_responses(file_path):
    with open(file_path, 'r') as file:
        return json.load(file) 

# Randomly choose an agent name
def get_random_agent():
    agents = ["Sam", "Michael", "Alex", "Vivian", "Lixy"]
    return random.choice(agents)

# Respond to user input based on keywords or randomly
def get_response(user_input, responses, random_responses, user_name):
    for keyword, reply in responses.items():
        # Match whole words only
        if keyword.lower() in user_input.lower().split():
            return random.choice(reply).format(name=user_name)
    return random.choice(random_responses).format(name=user_name)

# Chat loop
def chat():
    user_name = input("Hello! Welcome to the University of Poppleton. What's your name? ").strip()
    if not user_name:
        print("Please enter your name to proceed.")
        return

    agent_name = get_random_agent()
    print(f"Hi {user_name}, I'm {agent_name}. How can I help you today?")

    # Predefined responses
    responses = {
        "cafe": ["The cafe is open from 8 AM to 5 PM, {name}."],
        "library": ["The library is open 24/7 for students."],
        "admissions": ["Admissions can be reached at admissions@poppleton.edu."],
        "sports": ["Our sports facilities are top-notch! Do you like football, {name}?"],
        "events": ["Check out the events calendar on our website."],
        "fees": ["Fees vary by course. Visit the finance section of our website, {name}."],
        "parking": ["Parking passes can be obtained from the transport office."],
        "health": ["The health center is open 9 AM to 4 PM, {name}.", "Counseling services are available by appointment, {name}."],
        "clubs": ["We have different clubs for student, {name}. Join one today!", "Want to start your own club, {name}? Visit the student activities office."],
        "exam": ["The timely schedule for exams of respective department can be found in student portal"]
    }

    # Generic fallback responses
    random_responses = [
        "Interesting! Tell me more, {name}.",
        "I'm not sure about that, {name}.",
        "Let me check on that for you, {name}.",
        "That's outside my expertise, {name}, but I can try to help!"
    ]

    while True:
        user_input = input("> ").strip()
        
        if not user_input:
            print("Please ask a question, {name}.".format(name=user_name))
            continue

        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Goodbye! Have a great day!")
            break

        print(get_response(user_input, responses, random_responses, user_name))

if __name__ == "__main__":
    chat()
