import discord
from config import settings
from config import Reaction
call = Reaction()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Loged on as {self.user}!")

    async def on_message(self, message):
        if str(message.author) == "SeyDin#4840":
            await message.channel.send(call.make_fraze_hello_alex())
        elif str(message.author) == "BlackSmith#7978":
            await message.channel.send(call.make_fraze_hello_rus())


client = MyClient()
client.run(settings['token'])
