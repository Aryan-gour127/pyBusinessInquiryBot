from botResponses import Bot

while True:

    message = input("you : ")

    if message.lower() == "exit":
        print("Thank you For visting Us!")
        break

    response = Bot(message)

    print("bot :",response)