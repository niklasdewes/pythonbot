from commands import MyClient, CMD
from roulette import ROU

def main():
    MyClient()
    CMD()
    ROU()

client = MyClient()
k = open('key.txt')
mykey = k.readline()
client.run(mykey)

if __name__ == "__main__":
    main()