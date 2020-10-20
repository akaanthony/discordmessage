import discord

client = discord.Client()

a = "!key"
b = "!what is hybrid"
c = "!ticket"


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content == a:
        await message.channel.send("Your hybrid key is examplekey123")
    
    if message.content == b:
        await message.channel.send("Hybrid Scripts is a automation tool wich includes Hybrid Browser, to spoof your location. Hybrid Extension to help you checkout faster on websites and Hybrid clicker to claim you free nitro and auto click links sent in discord servers!")
    if message.content == c:
        await message.channel.send("To create a ticket about Hybrid Scripts please react to the mesage in #tickets")


    
    

client.run('enter key here')