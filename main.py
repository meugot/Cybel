import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if(message.content == "Hello"):
            await message.channel.send("What you doin?")
        if(message.content == "Whatup Bot?"):
            await message.channel.send("Nothin, what bout you?")

client = MyClient()
client.run(os.getenv('TOKEN'))
