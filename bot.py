import discord
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

intents = discord.Intents.default()
intents.message_content = True

print(requests.get('https://scryfall.com/search?q=o%3Aflying&order=color&as=grid').text)

#client = MyClient(intents=intents)
#client.run('MTM5NjY1MjA0NTg1NTEwMTA1OQ.GvEQeE.xSDILSHJiOUd8wjGyLIJgY8NS49gPsqoqSp3y8')