# I'm importing choice from the random library, this package will be used to help us create the conditiional logic
from random import choice


def get_bot_response(user_response):
    # Define the get_bot_response function that takes one parameter called user_response, we'll be invoking this function later
    # there will be two variables holding elements, which are songs, relevant to different artists
    # once the user picks an option, a result will be printed using choice() and the user will be asked forever
    # until the user inputs "done"

    bot_response_pink_floyd = ["Wish You Were Here",
                               "Comfortably Numb", "Shine On You Crazy Diamond"]
    bot_response_the_beetles = [
        "Here Comes The Sun", "Hey Jude", "Come Together"]

  # Here is where the conditional logic falls, I compare the user's input to each condition, regardless of what the user inputs, the user will get an output
    if user_response == 'Pink Floyd':
        return choice(bot_response_pink_floyd)
    elif user_response == 'The Beetles':
        return choice(bot_response_the_beetles)
    elif user_response == 'Neither':
        return "ummm...... unfortunately, I'm frankly disappointed.... go and never come back you tastless banana!!!!! you probably like Rick Astley'.."
    else:
        return "For pete's sake! I gave you simple instructions to input one of the three choices I gave you earlier... scroll up buddy..."


