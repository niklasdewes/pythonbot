import random
import discord
from discord import Member, Guild
import asyncio

client = discord.Client(intents=discord.Intents.all())

antworten = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Sieht so aus', 'Sehr wahrscheinlich',
            'Sehr unwahrscheinlich']

@client.event
async def on_ready():
    print(f"Eingeloggt als: {client.user.name}\r\n",
          "Version: 0.1")
    client.loop.create_task(status_task())

async def status_task():
    colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
    while True:
        await client.change_presence(activity=discord.Game("Bot ertellt von Niklas Dewes"), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game("Nur Augen für Amy!"), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game("!help für Hilfe"), status=discord.Status.online)
        await asyncio.sleep(5)
        guild: Guild = client.get_guild(782334678392111175)
        if guild:
            role = guild.get_role(810282842030342154)
            if role:
                if role.position < guild.get_member(client.user.id).top_role.position:
                    await role.edit(colour=random.choice(colors))


def is_not_pinned(mess):
    return not mess.pinned

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "!help" in message.content:
        await message.channel.send("**Python Discord Bot von Niklas Dewes**\r\n"
                                    "---------------------\n"
                                    "**!help** - Zum aufrufen aller Befehle.\n"
                                    "**!userinfo** - Zeigt dir die Userinfo von Personen an.\n"
                                    "**!clear** - Damit kannst du Nachrichten löschen, brauchst aber dafür die Berechtigungen.\n"
                                    "**!8b <Frage>** - Wahrheitskugel. Stell eine Frage und die Frage wird dir beantwortet.\n")
    if message.content.startswith('!userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Ich bin ein EmbedFooter.')
                mess = await message.channel.send(embed=embed)
    if message.content.startswith('!clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
    if message.content.startswith('!8b'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Ich versuche deine Frage `{0}` zu beantworten.'.format(frage))
            await asyncio.sleep(2)
            await mess.edit(content='Ich kontaktiere das Orakel...')
            await asyncio.sleep(2)
            await mess.edit(content='Deine Antwort zur Frage `{0}` lautet: `{1}`'
                            .format(frage, random.choice(antworten)))


k = open('key.txt')
mykey = k.readline()
client.run(mykey)