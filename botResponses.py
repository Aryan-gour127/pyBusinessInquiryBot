import businessData


def Bot(message):

    message = message.lower().strip()

    if any(word in message for word in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):
        return (
            f"Hello! 👋 Welcome to {businessData.BUSINESS_NAME}. "
            "How can I help you today?"
        )

    if any(word in message for word in [
        "service",
        "services",
        "offer",
        "offers",
        "provide",
        "provides"
    ]):

        for service in businessData.SERVICES:

            service_words = service.lower().split()

            if all(word in message for word in service_words):
                return (
                    f"{service}: "
                    f"{businessData.SERVICE_DETAILS[service]}"
                )

        return (
            f"We provide: {', '.join(businessData.SERVICES)}"
        )

    if (
        "business name" in message
        or "company name" in message
        or "what is your business" in message
        or message.strip() == "business"
    ):
        return (
            f"We are {businessData.BUSINESS_NAME}.\n"
            f"{businessData.TAGLINE}"
        )

    if any(word in message for word in [
        "founder",
        "owner",
        "ceo"
    ]):

        return (
            f"The founder of {businessData.BUSINESS_NAME} "
            f"is {businessData.FOUNDER}."
        )

    if any(phrase in message for phrase in [
        "address",
        "location",
        "office location",
        "where are you located",
        "where is your office",
        "where are you based"
    ]):

        return (
            f"We are located at:\n"
            f"{businessData.ADDRESS}"
        )

    if any(phrase in message for phrase in [
        "phone",
        "phone number",
        "contact number",
        "contact details",
        "email",
        "email address",
        "website"
    ]):

        return (
            "You can contact us through:\n"
            f"Phone: {businessData.PHONE}\n"
            f"Email: {businessData.EMAIL}\n"
            f"Website: {businessData.WEBSITE}"
        )

    if any(phrase in message for phrase in [
        "business hours",
        "working hours",
        "opening hours",
        "opening time",
        "closing time",
        "working time"
    ]):

        return (
            f"Our business hours are:\n"
            f"{businessData.BUSINESS_HOURS}"
        )

    if any(word in message for word in [
        "price",
        "pricing",
        "cost",
        "costing",
        "charges",
        "fee",
        "fees",
        "amount"
    ]):

        for service in businessData.PRICING:

            service_words = service.lower().split()

            if all(word in message for word in service_words):
                return (
                    f"The price for {service} is "
                    f"{businessData.PRICING[service]}."
                )

        return (
            "Our starting prices are:\n"
            + "\n".join(
                f"- {service}: {price}"
                for service, price in businessData.PRICING.items()
            )
        )

    if any(phrase in message for phrase in [
        "about",
        "about business",
        "tell me about your business",
        "what does your business do",
        "what do you do"
    ]):

        return f"{businessData.ABOUT}"

    if any(word in message for word in [
        "social media",
        "instagram",
        "linkedin",
        "github"
    ]):

        return (
            "You can find us on:\n"
            f"Instagram: {businessData.SOCIAL_MEDIA['Instagram']}\n"
            f"LinkedIn: {businessData.SOCIAL_MEDIA['LinkedIn']}\n"
            f"GitHub: {businessData.SOCIAL_MEDIA['GitHub']}"
        )

    if any(word in message for word in [
        "faq",
        "frequently asked questions"
    ]):

        return (
            "Here are some frequently asked questions:\n"
            + "\n".join(
                f"- {question}"
                for question in businessData.FAQ
            )
        )

    if any(word in message for word in [
        "bye",
        "goodbye"
    ]):

        return "Thank you for visiting AI by Aryan! 👋"

    return (
        "Sorry, I don't have information about that yet. "
        "You can ask me about our services, pricing, "
        "contact details, location, business hours, or FAQs."
    )