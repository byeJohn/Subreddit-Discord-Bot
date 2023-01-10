import discord
import aiohttp
import asyncio
import praw
import time

client = discord.Client(intents=discord.Intents.default())
TOKEN = ''
reddit = praw.Reddit(client_id='', cilent_secret='', user_agent='')

# sets the amount of minutes per check
interval = 1

async def send_latest_post(subreddit, channel_id):
    # empty list that stores posts that have already been sent
    sent_posts = []
    
    while True:
        submission = reddit.subreddit(subreddit).new(limit=5) # gets the latest posts in the subreddit
        post = next(submission) # gets the next post
        title = post.title # gets the title of the post
        if title not in sent_posts: # checks if the post has already been sent
            sent_posts.append(title) # Adds the post to "sent_posts"
            url = post.url # gets the URL of the post
            reddit_link = post.permalink

            # Create an embed with the post title, URL, and content URL
            embed = discord.Embed(title=title)
            embed.add_field(name ='Reddit URL', value ="https://www.reddit.com" + reddit_link)
            embed.add_field(name = 'Content', value = url, inline=False)

            channel = client.get_channel(channel_id) # discord channel
            await channel.send(embed=embed)
        await asyncio.sleep(interval * 60) # pauses the program for the desired interval(minutes)


@client.event
async def on_ready():
    try:
        # runs this function once when the bot starts up
        await send_latest_post('buildapcsales', 1054872742089982004)

        # runs the function at the desired interval
        while True:
            time.sleep(interval * 60) # Pause the program for the desired interval in minutes
            await send_latest_post('buildapcsales', 1054872742089982004)
    except Exception as e:
        print(f'An exception occurred: {e}')
  

client.run(TOKEN)
