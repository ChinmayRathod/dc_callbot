from webserver import keep_alive

import os
import discord
import random 
client = discord.Client()

ronin="<@461884415451201536>"
amjoker="<@434964559342862346>"
axo='<@650707507408273420>'
et="<@517990054812188674>"
logan="<@499147266939027467>"
nameless="<@693069897059794945>"
nameless007="<@760028292836360202>"
nobody="<@693156952175542282>"
star="<@650406306955526197>"
xgamers="<@&750273286998589500>"
test="<@&950428722018791464>"

@client.event
async def on_ready():
  print('We have logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  usr=0
  role=0
  if message.content.startswith('.c'):
    user="a"
    if message.content=='.cr' or message.content=='.cronin':
      user=ronin
      usr=1
    elif message.content=='.cam' or message.content=='.camjoker':
      user=amjoker
      usr=1
    elif message.content=='.cax' or message.content=='.caxo':
      user=axo
      usr=1
    elif message.content=='.ce' or message.content=='.cet' or message.content=='.cesakki':
      user=et
      usr=1
    elif message.content=='.cl' or message.content=='.clogan':
      user=logan
      usr=1
    elif message.content=='.cna' or message.content=='.cnameless':
      user=nameless
      usr=1
    elif message.content=='.cna007' or message.content=='.cnameless007':
      user=nameless007
      usr=1
    elif message.content=='.cno' or message.content=='.cnobody':
      user=nobody
      usr=1
    elif message.content=='.cs' or message.content=='.cstar' or message.content=='.cstarhelix':
      user=star
      usr=1
    elif message.content=='.ct' or message.content=='.ctest':
      user=test
      role=1
    elif message.content=='.cx' or message.content=='.c' or message.content=='.cxgamers' or message.content==".cxgamer" or message.content=='.cexgamer' or message.content=='.cexgamers':  
      user=xgamers
      role=1

    num=random.random()
    num=int(num*10)
    if usr==1:
      if num%2==1:
        user_id = "cmng "+user+"?"
      else:
        user_id = "aa raha hai "+user+"?"
      msg=user_id
    elif role==1:
      if num%2==1:
        user_id = "cmng "+user+"?"
      else:
        user_id = "koi aa raha hai "+user+"?"
      msg=user_id
    else:
      msg="Command does not exist :-("
    
    await message.channel.send(msg)
  elif message.content=='.help' or message.content=='.h':
    help_message="The command can be initiated with the '.' symbol.\nThe commands provided right now are :\n .cx to call the ex-gamers channel and .c# in the place of # add first letter of name like 's' for starhelix 'r' for ronin, 'na' for nameless, 'na007' for nameless007 etc.\nOr\n you can write .cname"
    await message.channel.send(help_message);

keep_alive()
my_secret = os.environ.get('TOKEN')
client.run(my_secret)