import businessData

def Bot(message):

    message = message.lower()

    if any(word in message for word in['services','service','offer','provide','provides']):
        return f"WE PROVIDE : {businessData.SERVICES}"