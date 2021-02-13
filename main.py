import discord
import random

class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("""Der Bot wurde erfolgreich gestartet.
---------------------
Version: 0.1
Auhtor: Niklas Dewes""")

    async def on_message(self, message):
        if message.author == MyClient.user:
            return  
        if message.content == "!help":
            await message.channel.send("""Python Discord Bot von Niklas Dewes
---------------------
!roulette <BID> - Spiele Roulette. Als BID kommt 'red', 'black' & 'number(0-36)' in Frage.""")

        if message.author == MyClient.user:
            return

        if message.content.startswith("!rl"):
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
                await message.channel.send('Ungültige Eingabe')
                return
            result = random.randint(0,36)
            print(result)
            if bid_param == -1:
                won = result%2 == 0 and not result == 0
            elif bid_param == -2:
                won = result%2 == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send('$$$ Du hast gewonnen $$$')
            else:
                await message.channel.send('Leider verloren...')
def main():
    MyClient()

    client = MyClient()
    k = open('key.txt')
    mykey = k.readline()
    client.run(mykey)

if __name__ == "__main__":
    main()