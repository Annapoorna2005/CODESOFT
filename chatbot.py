import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! 👋 How can I help you today?"

    # Asking name
    elif "your name" in user_input:
        return "I am CodSoft AI Chatbot 🤖"

    # Help
    elif "help" in user_input:
        return "I can help you with orders, products, and general queries."

    # Order related
    elif "order" in user_input:
        return "You can track your order in the 'My Orders' section."

    # Products
    elif "product" in user_input:
        return "We have a wide range of gifts 🎁. Visit the shop page!"

    # Goodbye
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a nice day 😊"

    # Default
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def chat():
    print("🤖 Chatbot: Hello! Type 'exit' to stop.")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    chat()