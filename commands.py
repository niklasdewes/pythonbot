import discord

class CMD(discord.Client):
#If a message delivered
    async def on_message(self, message):
        if message.author == client.user:
            return  
        if message.content == "!help":
            return await message.channel.send("""Python Discord Bot von Niklas Dewes\n
                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
                                            !roulette <BID> - Spiele Roulette. Als BID kommt 'red', 'black' & 'number(0-30)' in Frage.""")

client = CMD()