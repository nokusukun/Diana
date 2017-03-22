import discord
import asyncio
from discord.ext import commands
from commands import urbandict, gelbooru


bot = commands.Bot(command_prefix='!')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.content.startswith('!ud'):
        msg = urbandict.urbandict(message.content.split(' ', 1)[1])
        await client.send_message(message.channel, embed=msg)

    if message.content.startswith("!cum"):
        msg = gelbooru.gelbooru_search(message.content.split(' ', 1)[1])
        await client.send_message(message.channel, embed=msg)

if __name__ == '__main__':
    token = open('token', 'r').readline().rstrip()
    client.run(token)
