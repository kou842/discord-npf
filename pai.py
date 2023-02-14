import discord

TOKEN = 'OTgzNjMyNjg2NjEyNjE1MTg4.G_Rwx0.CZCN8OgXBda5xuiTormmilrpwbyFvHnoLo_GCM' # TOKENを貼り付け
GUILD = 964402354805940225
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    channel = message.channel
    content = message.content
    
    if channel.id == 983318451084984430:
        if content == "金谷":
            await channel.send("消えろ")
            
client.run(TOKEN)
