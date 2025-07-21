import discord
import scryfall
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('$search'):
            await message.channel.send(scryfall.get_first_card(message))
        if message.content.startswith('$random'):
            await message.channel.send(scryfall.get_random_card(message))