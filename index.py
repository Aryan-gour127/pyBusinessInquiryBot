from botResponses import Bot


print("-" * 50)
print("     AI BY ARYAN - BUSINESS BOT")
print("-" * 50)
print("Type 'exit' to leave the chatbot.\n")


while True:

    message = input("You: ")

    if message.lower().strip() == "exit":
        print("Bot: Thank you for visiting AI by Aryan!")
        break

    response = Bot(message)

    print(f"Bot: {response}\n")