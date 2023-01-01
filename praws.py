import discord
import aiohttp
import asyncio
import praw
import time

client = discord.Client(intents=discord.Intents.default())

reddit = praw.Reddit(client_id='', cilent_secret='', user_agent='')

# set the amount of minutes you want the bot to check. (default every 1 minute)
interval = 1

    sent_posts = []
    
    while True:
        submission = reddit.subreddit(subreddit).new(limit=5) 
        post = next(submission) 
        title = post.title 
        if title not in sent_posts: 
            sent_posts.append(title) 
            url = post.url 
            content_url = post.url 
            reddit_link = post.permalink

            #embed the post title, URL, and content URL
            embed = discord.Embed(title=title)
            embed.add_field(name ='Reddit URL', value ="https://www.reddit.com" + reddit_link)
            embed.add_field(name = 'Content', value = url, inline=False)

            channel = client.get_channel(channel_id)
        await channel.send(embed=embed)
        time.sleep(interval * 60)
        
@client.event
async def on_ready():
    try:
        
        await send_latest_post('subreddit', channel_id)

         
        while True:
            time.sleep(interval * 60)  
            await send_latest_post('subreddit', channel_id)
    except Exception as e:
        print(f'An exception occurred: {e}')
  

client.run('BOT_TOKEN_HERE')
