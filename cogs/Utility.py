import discord
import os
import threading
import string
import random
import time
import json
import asyncio
import aiohttp
from threading import Thread
from discord.utils import find, get
from discord.ext import commands
from time import strftime, gmtime
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, Style
import datetime


class Utility(commands.Cog):
      def __init__(self, client):
            self.client = client
            self.colors = [0xffb2a3,0xff00ee]



      @commands.command(aliases=["Av","av"])
      async def Avatar(self, ctx, *, member: discord.Member = None):
       await ctx.message.delete()
       member = ctx.author if not member else member
       embed = discord.Embed(timestamp=ctx.message.created_at, color=random.choice(self.colors))
       embed.set_author(name=f"{member.name}'s avatar", icon_url=ctx.author.avatar_url)
       embed.set_image(url=member.avatar_url)
       embed.set_footer(text=f"{ctx.author}")
       await ctx.send(embed=embed)

      snipe_message_content = None
      snipe_message_author = None
      snipe_message_id = None

      @commands.Cog.listener()
      async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author
        snipe_message_id = message.id
        await asyncio.sleep(60)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

      @commands.command()
      async def snipe(self, message):
          if snipe_message_content==None:
                await message.channel.send("`Theres nothing to snipe.`")
          else:
                embed = discord.Embed(description=f"{snipe_message_content}", color=random.choice(self.colors))
                embed.set_author(name=f"{snipe_message_author}", icon_url=snipe_message_author.avatar_url)
                await message.channel.send(embed=embed)
                return

      @commands.command(aliases=["ping"])
      async def Ping(self, ctx):
        embed=discord.Embed(title="Pong!", color=random.choice(self.colors))

        embed2=discord.Embed(title=f"`{round(self.client.latency *100)}ms`", color=random.randint(0, 0xFFFFFF))
        Ping = await ctx.send(embed=embed)

        await asyncio.sleep(1.2)
        await Ping.edit(embed=embed2)

      @commands.command(aliases=["serverinfo","si","Si"])
      async def Serverinfo(self, ctx):
        await ctx.message.delete()
        a = ctx.guild.member_count
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(
            title=f"{ctx.guild.name}",
            description=
            f"{a} **Members**\n {len(ctx.guild.roles)} **Roles**\n {len(ctx.guild.text_channels)} **Text-Channels**\n {len(ctx.guild.voice_channels)} **Voice-Channels**\n {len(ctx.guild.categories)} **Categories**",
            timestamp=datetime.datetime.utcnow(),
            color=random.choice(self.colors))
        embed.add_field(
            name="Server created at",
            value=f"{ctx.guild.created_at.strftime(date_format)}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

      @commands.command(aliases=["whois"])
      async def Whois(self,ctx, member: discord.Member):
         await ctx.message.delete()
         member = ctx.author if not member else member
         roles = [role for role in member.roles]

         embed = discord.Embed(color=random.choice(self.colors), timestamp=ctx.message.created_at)
  
         embed.set_author(name=f"User Info - {member}")
         embed.set_thumbnail(url=member.avatar_url)
         embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

         embed.add_field(name="User ID", value=member.id)
         embed.add_field(name="Nickname", value=member.display_name)

         embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))
         embed.add_field(name="Guild Join Date", value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))

         embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
         embed.add_field(name="Highest Role", value=member.top_role.mention)

         embed.add_field(name="Bot?", value=member.bot)

         await ctx.send(embed=embed)
   

def setup(client):
    client.add_cog(Utility(client))
