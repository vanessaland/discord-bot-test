import os
import discord
from stay_awake import stay_awake

stay_awake()

# Example Discord Bot in Python

bot = discord.Client()

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  if message.author == bot:
    return

  if message.content.startswith('$bussin'):
    await message.channel.send('sheeeeeeesh')

  if message.content.startswith('$echo'):
    await message.channel.send(message.content[5:].strip())

  if message.content.startswith('$hbd'):
    if len(message.mentions) == 0:
      await message.channel.send('Happy birthday, <@' + str(message.author.id) + '>!')
    else:
      for mention in message.mentions:
        await message.channel.send('Happy birthday, <@' + str(mention.id)+'>!')

  if message.content.startswith('$channel'):
    channel_name = message.content[8:].strip()
    await message.channel.category.create_text_channel(channel_name)

bot.run(os.environ['TOKEN'])