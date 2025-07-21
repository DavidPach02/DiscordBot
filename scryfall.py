import requests
import json

def get_first_card(message):
    """ This searches a card in scryfall based on the card name provided.
    
    Arguments:
        message {string} -- Message input by the user
    Returns:
        string -- First card image found in the list.
    """
    # Split the string to the search keyword and the card name
    message_split = message.content.split(' ', 1)

    # If the list is less than one, then the user forgot to enter a card name
    if len(message_split) <= 1:
        return 'Please enter a card name.'
    
    card_Name = message_split[1]
    # If the search keyword is valid, then search for the card
    response = requests.get(f'https://api.scryfall.com/cards//search?q={card_Name}&unique=cards&order=name')
    json_data = json.loads(response.text)

    # If the object is not a list, then a card was not found
    if json_data['object'] != 'list':
        return f'**{card_Name}** not found.'

    # Else return the first card found
    return json_data['data'][0]['image_uris']['normal']

def get_random_commander():
    """ This returns a random commander card from Scryfall.
    
    Returns:
        string -- Card image from Scryfall.
    """
    # Get a random commander card
    response = requests.get('https://api.scryfall.com/cards/random?q=is%3Acommander')
    json_data = json.loads(response.text)

    # If the object is not a list, then a card was not found
    if json_data['object'] != 'card':
        return f'Card not found.'
    
    # Else return the commander card
    return json_data['image_uris']['normal']

def get_random_card_normal():
    """ This returns a random card from Scryfall.
    
    Returns:
        string -- Card image from Scryfall
    """
     # Get a random commander card
    response = requests.get('https://api.scryfall.com/cards/random')
    json_data = json.loads(response.text)
    return json_data['image_uris']['normal']


def get_random_card(message):
    """ This generally returns a random card based on the keyword given by the user

    Arguments:
        message {string} -- Message input by the user
    Returns:
        string -- Card image from Scryfall
    """
     # Split the string to the random keyword
    message_split = message.content.split(' ', 1)

    # If the list is less than one, just return random card
    if len(message_split) <= 1:
        return get_random_card_normal()
    
    # If it has the commander keyword, then it will return a random commander
    if message_split[1].startswith('commander'):
        return get_random_commander()