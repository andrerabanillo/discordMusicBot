# Discord Music Bot

This following project allows Discord users in a voice chat to play audio from a Youtube video.

## Description
This Discord bot plays YouTube audio in voice channels using the discord.py library. 

With user commands such as "?play ", "?pause", "?resume", and "?stop", it can establish a connection to a voice channel and play, pause, resume, and stop tracks. 

The bot uses FFmpeg and youtube_dl to manage audio playback and extraction on Discord servers.

## Getting Started

### Dependencies

discord.py: For interacting with the Discord API and managing bot functionality within Discord servers.

youtube_dl: Used to extract audio information from YouTube URLs.

FFmpeg: Required for handling audio processing and playback within Discord voice channels.

asyncio: Utilized for handling asynchronous tasks within the bot.

### Executing program

Install Python: Make sure Python is installed on your computer.

Install Required Packages: Open your terminal or command prompt and type:

Copy the following code into your terminal: 

``pip install discord.py youtube_dl``


FFmpeg Installation: Download and install FFmpeg from FFmpeg. 
https://ffmpeg.org/download.html

Code Setup:

Replace token = "" with your Discord bot token.

Run the program, this is where the discord bot should join the discord channel you are currently in 

Invite the bot to your Discord server and grant it access to voice channels. Type?play [YouTube URL] in a text channel where the bot is present. To control the bot's music playback in voice channels, use the commands?pause,?resume, or?stop.

Before attempting to play music, make sure the bot is online and linked to a voice channel on your server.

### For example: 

?play https://www.youtube.com/watch?v=1uYWYWPc9HU and the bot will play audio from the youtube video

## Limitations

The bot can only be availble when ran locally.

## Author Information

Andre Rabanillo
1234572
arabanil@uoguelph.ca