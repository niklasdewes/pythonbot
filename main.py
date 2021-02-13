import discord
from commands import cmd
from roulette import rou

class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("I've been login.")

    cmd()
    rou()

def main():
    MyClient()

client = MyClient()
k = open('key.txt')
mykey = k.readline()
client.run(mykey)

if __name__ == "__main__":
    main()