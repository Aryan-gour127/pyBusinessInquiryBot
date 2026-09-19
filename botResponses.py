import businessData

def Bot(message):

    message = message.lower()

    if any(word in message for word in['services','service','offer','provide','provides', 'service details','detail']):
        return f"WE PROVIDE : {businessData.SERVICES}"

    elif any(word in message for word in ['business', 'business name']):
        return f"WE ARE : {businessData.BUSINESS_NAME} {businessData.TAGLINE}"

    elif any(word in message for word in ['founder', 'owner', 'found', 'own', 'ceo', 'handles', 'handle', 'manage', 'manager']):
        return f"The {message} is : {businessData.FOUNDER}"

    elif any(word in message for word in ['address', 'place', 'office location', 'location']):
        return f"WE ARE SITUATED AT : {businessData.ADDRESS}"

    elif any(word in message for word in ['phone number','number', 'contact details','contact', 'email', 'mail', 'web', 'website', '']):
        return f"The {message} is : {businessData.PHONE}{businessData.EMAIL}{businessData.WEBSITE}"

    elif any(word in message for word in ['business time', 'time', 'timing', 'business hour', 'business hours']):
        return f"WE are open ate : {businessData.BUSINESS_HOURS}"

    elif any(word in message for word in ['pricing', 'prices', 'price', 'costing', 'cost', 'ammount', 'money']):
        return f"The {message} : {businessData.PRICING}"

    elif any(word in message for word in ['about business', 'about', 'business idea', 'idea']):
        return f" WE ARE : {businessData.ABOUT}"

    elif any(word in message for word in ['faq', 'question', 'queries', 'querry']):
        return f"THE FAQ : {businessData.FAQ}"