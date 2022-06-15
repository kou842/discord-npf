import discord

TOKEN = 'OTgzNjMyNjg2NjEyNjE1MTg4.G-BRBl.xpMtCDFzXja8n2-OkWDINuW2iRS2-ItTre8URc' # TOKENを貼り付け
CHANNELID = 983734676365668432 # チャンネルIDを貼り付け

client = discord.Client()

# 起動時処理
@client.event
async def on_ready():
    print(channel.name)
    print('ログインしました')
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")
    counter = 0
    
    

    
# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
    
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(983734676365668432)
    
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [964402355263123481, 964402355263123481]
    
        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** チャンネルから、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** チャンネルに、__" + member.name + "__  が参加しました！")
            
@client.event
async def on_ready():
    channel = 983734676365668432
    async for message in channel.history(limit=1):
        if message.author == client.user:
            counter += 1
            
async def on_reaction_add(reaction, user):

    # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
    botRoom = client.get_channel(983734676365668432)
    print("a"+reaction.message.id)
    if reaction.count <= 1 and reaction.message.id == 980453265563066398 :
        await botRoom.send("@"+reaction.message.user+"さん。3人以上の承認が行われたので、早退届・遅刻届を受理致します。お疲れ様でした。")
        
    

client.run(TOKEN)