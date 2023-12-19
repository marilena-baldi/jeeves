info_menu = """
Introducing Jeeves, your trusty assistant bot!
Jeeves is here to help and assist you.

Here is the list of commands you can use:
- /new: Start a new conversation.
- /info: Display this info menu.

Note: Jeeves is an AI-powered bot and may not always provide accurate or up-to-date information. The answers provided by Jeeves are for informational purposes only and should not be relied upon as professional advice. It is important to verify any information obtained from Jeeves through other sources before making any decisions or taking any action. Additionally, Jeeves may not always be able to understand or respond to every request or question, so please be patient and try again if you do not receive a response. By using Jeeves, you acknowledge that you understand these limitations and will hold harmless the developers and owners of Jeeves in any case of inaccurate or incomplete information.
"""

def parse_message(message):
    if not message:
        return ["Sorry, I didn't understand that."]

    messages = []
    if len(message) < 4096:
        messages.append(message)
    else:
        for i in range(len(message) % 4096):
            messages.append(message[i*4096:(i+1)*4096])

    return messages
