import discord

class MyClient(discord.Client):
#If a message delivered
    async def on_message(self, message):
        if message.author == discord.client.User:
            return

        if message.content.startswith("!help"):
            await message.channel.send("Python Discord Bot von Niklas Dewes")
            await message.channel.send("Amy ist toll")
            await message.channel.send("Fabrizio mag Pizza")