print("Chatbot started. Type 'exit' to stop.")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")
    
    elif user == "how are you":
        print("Bot: I am fine!")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    elif user == "exit":
        break
    
    else:
        print("Bot: I don't understand.")
