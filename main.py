import discord
import commands
import roulette

class MyClient(discord.Client):
    #Login
    async def on_ready(self):
        print("I've been login.")

def main():
    MyClient()
    key = open("key.txt")
    read_file = key.read()
    exec(read_file)

client = MyClient()
k = open('key.txt')
mykey = k.readline()
client.run(mykey)

if __name__ == "__main__":
    main()