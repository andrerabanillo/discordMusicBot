import discord
import os 
import asyncio
import youtube_dl


token = "" #insert token here 

#Interact with discord API
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

voice_clients = {}

yt_dl_opts = {'format' : 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}

#Waits for bot to come online
@client.event 
async def on_ready():
    print(f"Bot is now logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try: 
            url = msg.content.split()[1]
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_clients[msg.guild.id].play(player)


        except Exception as err:
            print(err)
    
    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print (err)

    if msg.content.startswith("?resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print (err)


    if msg.content.startswith("?stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print (err)

    
client.run(token)