import discord
import aiohttp
import asyncio
import praw
import time

client = discord.Client(intents=discord.Intents.default())

reddit = praw.Reddit(client_id='', cilent_secret='', user_agent='')

# set the amount of minutes you want the bot to check. (default every 1 minute)
interval = 1

async def send_latest_post(subreddit, channel_id):
  

client.run('BOT_TOKEN_HERE')
