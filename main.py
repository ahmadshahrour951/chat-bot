# I'm importing choice from the random library, this package will be used to help us create the conditiional logic
from random import choice


def get_bot_response(user_response):
    # Define the get_bot_response function that takes one parameter called user_response, we'll be invoking this function later
    # there will be two variables holding elements, which are songs, relevant to different artists
    # once the user picks an option, a result will be printed using choice() and the user will be asked forever
    # until the user inputs "done"

