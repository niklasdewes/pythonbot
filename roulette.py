import discord
import random

class ROU(discord.Client):
    async def on_messages(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("!roulette"):
            bid = message.content.split(' ')[1]
            bid_param = -3
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                return await message.channel.send("Ungültige Eingabe")
            result = random.randint(0,36)
            print(result)
            if bid_param == -1:
                won = result%2 == 0 and not result == 0
            elif bid_param == -2:
                won = result%2 == 1
            else:
                won = result == bid_param
            if won:
                return await message.channel.send("~~~ Du hast gewonnen!!! ~~~")
            else:
                return await message.channel.send("Leider verloren...")

client = ROU()
k = open('key.txt')
mykey = k.readline()
client.run(mykey)