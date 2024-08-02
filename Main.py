# Define greetings the chatbot can respond to
greetings = ["hi", "hello", "hey"]

# Define questions the chatbot can answer
questions = {
    "how are you": "I'm doing well, thanks for asking!",
    "what's your name": "My name is Chatty!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "tell me about yourself": "I am Chatty, your virtual assistant. I am 0 years old. I am new to the cyberworld. I am everyone's friend!",
    "what can you do": "I can answer basic questions and hold simple conversations for now."
}

# Define a default response
default_response = "That's Interesting, tell me more about it!"

print("Chatty: Hello there! I am Chatty, your virtual assistant!")

# Start the chat loop
while True:
  # Get user input
  user_input = input("You: ").lower()

  # Check if user wants to quit
  if user_input == "bye":
    break

  # Check if user input is a greeting
  if user_input in greetings:
    response = "Hello my friend!"
    # Ask the first question
    response += "\nWhat is your favorite color?"

  # Check if user input is a question
  elif user_input in questions:
    response = questions[user_input]
    # Ask the second question after some responses
    if user_input in ["how are you", "tell me about yourself"]:
      response += "\nWhat do you like to do for fun?"

  # Otherwise provide a default response
  else:
    response = default_response
    # Ask the third question after some user input
    if len(user_input) > 5:  # You can adjust the condition here
      response += "\nWow ! What is your favorite movie?"

  # Print chatbot response
  print("Chatty: " + response)

print("Chatty: Bye! Have a nice day!")

'''import json

# Define the filename to store user data
user_data_file = "user_data.json"

# Define the user data structure (example)
user_data = {"name": None, "favorite_color": None}

def load_user_data():
  """Loads user data from the file if it exists."""
  global user_data
  try:
    with open(user_data_file, "r") as f:
      user_data = json.load(f)
  except FileNotFoundError:
    pass  # Ignore if file doesn't exist

def save_user_data():
  """Saves user data to the file."""
  global user_data
  with open(user_data_file, "w") as f:
    json.dump(user_data, f)

# Load user data on program start
load_user_data()


# Define greetings the chatbot can respond to
greetings = ["hi", "hello", "hey"]

# Define questions the chatbot can answer
questions = {
    "how are you": "I'm doing well, thanks for asking!",
    "what's your name": "My name is Chatty!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "tell me about yourself": "I am Chatty, your virtual assistant. I am 0 years old. I am new to the cyberworld. I am everyone's friend!",
    "what can you do": "I can answer basic questions and hold simple conversations for now. I can also remember some things you tell me."
}

# Define a default response
default_response = "That's Interesting, tell me more about it!"

print("Chatty: Hello there! I am Chatty, your virtual assistant!")

# Start the chat loop
while True:
  # Get user input
  user_input = input("You: ").lower()

  # Check if user wants to quit
  if user_input == "bye":
    break

  # Check if user input is a greeting
  if user_input in greetings:
    if "name" in user_data and user_data["name"] is not None:  # Check if name is stored
      response = f"Hello again, {user_data['name']}! What is your favorite color?"
    else:
      response = "Hello my friend!"
      response += "\nWhat is your name?"  # Ask for the name

  # Check if user input is a question
  elif user_input in questions:
    response = questions[user_input]
    # Ask the second question after some responses
    if user_input in ["how are you", "tell me about yourself"]:
      response += "\nWhat do you like to do for fun?"

  # Otherwise provide a default response
  else:
    response = default_response
    # Ask the third question after some user input
    if len(user_input) > 5:
      response += "\nThat's interesting! What is your favorite movie?"

  # Update user memory with name (if provided)
  if "what's your name" in user_input and len(user_input.split()) > 3:
    name = user_input.split()[2]  # Extract the name
    user_data["name"] = name

  # Print chatbot response
  print("Chatty: " + response)

# Save user data on program exit
save_user_data()

print("Chatty: Bye! Have a nice day!")
'''