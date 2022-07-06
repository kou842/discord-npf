from email import message_from_binary_file
from operator import truediv
import discord

TOKEN = 'OTgzNjMyNjg2NjEyNjE1MTg4.GUmqQp.TDAzSFqR8sB3ZaJD_I365_4Kv0AuUyky3eBrsw' # TOKENを貼り付け
CHANNELID = 983734676365668432 # チャンネルIDを貼り付け

client = discord.Client()

# 起動時処理
@client.event
async def on_ready():
    print('ログインしました')
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")
    for guild in client.guild():
@client.event
async def on_message(message):
    messager = message.author.roles
    print (messager)
    for number  in range(len(messager)):
        role = messager[number]
        if role.name == "容疑者（逮捕済み）":
            await message.delete()
                

        
        
client.run(TOKEN)