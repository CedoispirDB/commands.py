def countMessages(user):
    user = user + ":"
    file = open("/Users/marcobarreirinhas1/downloads/WhatsApp Chat with Família bonita ❤️🦈(1).txt", "r")
    total_messages = 0
    user_messages = 0
    user_text_messages = 0
    user_omitted = 0

    for line in file:
        if line.__contains__("PM - ") or line.__contains__("AM - "):
            if line.__contains__("PM - " + user) or line.__contains__("AM - " + user):
                if line.__contains__("<Media omitted>"):
                    user_omitted += 1
                else:
                    user_text_messages += 1
                user_messages += 1
            total_messages += 1

    print(user + " sent: " + str(user_text_messages) + " text messages")
    print(user + " sent: " + str(user_omitted) + " not text messages ")
    print(user + " sent a total of : " + str(user_messages))
    print(user + " sent " + str(int(user_messages * 100 / total_messages)) + "% of the group's messages")
    print("Total messages sent: " + str(total_messages))



if __name__ == '__main__':
    countMessages("Marco")


    # 437
    # 337
    # 924
    # 231