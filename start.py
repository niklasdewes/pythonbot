import discord
import commands
import roulette

class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("I've been login.")

client = MyClient()
client.run(open("key.txt)"))