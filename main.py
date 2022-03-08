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

#change from here


vulgar=["noob","chutiya","bsdk","bkl",'lund','lavda','bc','mc']
replies=["look in the mirror","no need to call yourself","tera naam"]

solo=["cmng","aa raha hai"]
grp=["cmng","koi aa raha hai","aa rahe ho"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg='\0'
  #a command is passed
  if message.content.startswith("."):

    if  message.content=='.c':
      msg=random.choice(grp)+" "+xgamers+"?"
    #call command
    elif message.content[1]=='c':
      list=message.content[2:].split()
      msg=call_cmnd(list)
    #help command
    elif message.content=='.h' or message.content=='.help':
      msg="Help!!!\nThe command can be initiated with the '.' symbol.\nThe commands provided right now are :\n.cx to call the ex-gamers channel.\nc# in the place of # add first letter of name like:\n's' for starhelix \n'r' for ronin\n'na' for nameless\n'na007' for nameless007\n'e'/'et' for esakki\n'ax' for axo\n'am' for amjoker\nYou can write .cname in the place of name write the full name.\nAlso there are few more changes they will reveal themselves in course of time."
    #custom command
    
    #not proper syntax
    else:
      msg="Command not found :-("
      
    await message.channel.send(msg)
  else:
    list=message.content.split()
    i=scan(list)
    if i=='lund' or i=='lavda':
      msg="Chota ahe tujha!"
      await message.channel.send(msg)
    elif i!='null':
      msg=random.choice(replies)+" "+i
      await message.channel.send(msg)
      
def scan(list):
  for x in vulgar:
    for i in list:
      if x==i :
        return i
  return 'null'

def call_cmnd(list):
  usr=0
  msg=" "
  for x in list:
    if x=='r' or x=='ronin':
      msg=msg+" "+ronin
      usr=usr+1
    elif x=='am' or x=='amjoker':
      msg=msg+" "+amjoker
      usr=usr+1
    elif x=='ax' or x=='axo':
      msg=msg+" "+axo
      usr=usr+1
    elif x=='e' or x=='et' or x=='esakki':
      msg=msg+" "+et
      usr=usr+1
    elif x=='l' or x=='logan':
      msg=msg+" "+logan
      usr=usr+1
    elif x=='na' or x=='nameless':
      msg=msg+" "+nameless
      usr=usr+1
    elif x=='na007' or x=='nameless007':
      msg=msg+" "+nameless007
      usr=usr+1
    elif x=='no' or x=='nobody':
      msg=msg+" "+nobody
      usr=usr+1
    elif x=='s' or x=='star' or x=='starhelix':
      msg=msg+" "+star
      usr=usr+1
    elif x=='t' or x=='test':
      msg=msg+" "+test
      usr=usr+2
    elif x=='x' or x=='xgamers' or x=='xgamer' or x=='exgamer' or x=='exgamers':  
      msg=msg+" "+xgamers
      usr=usr+2
  if msg==" ":
    return "No user exists with initials given."
  else:
    return num(usr,msg)+"?"

def num(usr,msg):
  if usr>=2:
    msg=random.choice(grp)+msg
  elif usr>0:
    msg=random.choice(solo)+msg
  return msg

#till before this and then keep alive
  
keep_alive()
my_secret = os.environ.get('TOKEN')
client.run(my_secret)