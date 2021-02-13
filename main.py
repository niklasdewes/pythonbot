import discord
from commands import MyClient, cmd
from roulette import rou

class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("I've been login.")

def main():
    MyClient()
    cmd()
    rou()

client = MyClient()
k = open('key.txt')
mykey = k.readline()
client.run(mykey)

if __name__ == "__main__":
    main()