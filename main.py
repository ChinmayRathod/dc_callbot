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


pause=0

vulgar=["noob",'lavde',"fuck",'fck','bitch',"chutiya","bsdk","bkl",'lund','lavda','bc','mc','gaandu','gandu','gaand','gand','f','chu']
ur_mom=["sexy"]
ur_mom_replies=["Your mom"]
replies=["look in the mirror","pakka","no need to call yourself","tera naam",'tu','sabse bada']

solo=["cmng","aa raha hai"]
grp=["cmng","koi aa raha hai","aa rahe ho"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg="\0"
  message.content=message.content.lower()
  global pause
  if pause==0:
    msg=check(message.content,vulgar)
    if message.content.startswith('.p'):
      pause=1
      await message.channel.send("Bot paused")
    elif msg!='\0':
      msg=output(vulgar,replies,msg,message)#vulgarity output
    else:
    
      msg=check(message.content,ur_mom)
      if msg!='\0':
        msg=output(ur_mom,ur_mom_replies,msg,message)#ur mom output
      else:
      
        if message.content[0]=='.':
        
          if  message.content=='.c':
            msg=random.choice(grp)+" "+xgamers+"?"
          elif message.content[1]=='c':
            list=message.content[2:].split()
            msg=time(list)
            msg=call_cmnd(list) + msg
          elif message.content=='.h' or message.content=='.help':
            msg="Help!!!\nThe command can be initiated with the '.' symbol.\nThe commands provided right now are :\n.cx to call the ex-gamers channel.\nc# in the place of # add first letter of name like:\n's' for starhelix \n'r' for ronin\n'na' for nameless\n'na007' for nameless007\n'e'/'et' for esakki\n'ax' for axo\n'am' for amjoker\nYou can write .cname in the place of name write the full name.\nAlso there are few more changes they will reveal themselves in course of time."
          else:
            msg="Command not found :-("
    if msg!='\0':
      await message.channel.send(msg)
  elif pause==1:
    if message.content.startswith('.up'):
      pause=0
      await message.channel.send("Bot unpaused")
    elif message.content.startswith('.'):
      await message.channel.send("I am paused , unpause me!Let's have some fun!!!")

def output(list,list_r,msg,message):
  msg=random.choice(list_r)+" "+msg+" "+message.author.name
  return msg
  
def time(list):
  msg="?"
  for x in list:
    if x[0]<='9' and x[0]>='0':
      msg= " at " + x +" ?"
  return msg

def check(msg,list):
  for x in list:
    i=msg.find(x)
    if i>=0:
      return x
  return '\0'

def call_cmnd(list):
  usr=0
  msg=" "
  for x in list:
    if x=='r' or x=='ronin' or x=='rr':
      msg=msg+" "+ronin
      usr=usr+1
    elif x=='k':
      msg=msg+" "+amjoker+" "+et+" "+nameless
      usr=usr+3
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
    return "No user exists with initials given"
  else:
    return num(usr,msg)

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