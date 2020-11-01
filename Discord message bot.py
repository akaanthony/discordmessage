import discord

client = discord.Client()

a = "!example"
b = "!example2"



@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content == a:
        await message.channel.send("enter the message for example 1 here")
    
    elif message.content == b:
        await message.channel.send("enter the message for example 2 here")
   


    
    

client.run('')
