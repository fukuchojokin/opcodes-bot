import discord
import tkn as t
import search as s
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('$opcodeof'):
        opcodes = s.search(t.file, message.content[9:].upper())
        await message.channel.send(opcodes)


client.run(t.TOKEN)
