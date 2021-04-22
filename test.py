import discord

client = discord.Client

@client.event()
async def on_ready():
    print("hfbvfg")
    print('hhfgh')

@client.event()
async def on_message(message):
    if message.content.startwith('-'):
        await client.send_message(message.channel, 'hello')

bot.run('ODE4NTE2MzUwODU1MTUxNjYw.YEZMwQ.IAElxUv6loQOFimlNAAyq39mRHA')