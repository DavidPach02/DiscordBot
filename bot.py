import discord
import myclient

intents = discord.Intents.default()
intents.message_content = True

client = myclient.MyClient(intents=intents)
client.run('MTM5NjY1MjA0NTg1NTEwMTA1OQ.GvEQeE.xSDILSHJiOUd8wjGyLIJgY8NS49gPsqoqSp3y8')