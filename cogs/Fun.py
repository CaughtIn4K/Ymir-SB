import discord, random, aiohttp
from discord import Permissions
from discord.ext import commands

class Fun(commands.Cog):
      def __init__(self, client):
            self.client = client
            self.colors = [0xffb2a3,0xff00ee]

      @commands.command(aliases=['8ball'])
      async def _8ball(self, ctx, *, question):
            porn = ["https://i.imgur.com/n5bJtbe.png","https://i.imgur.com/C526ITb.png","https://i.imgur.com/MRgokDa.png","https://i.imgur.com/YCLcKkh.png","https://i.imgur.com/ecICnkK.png","https://i.imgur.com/XQmeInr.png","https://i.imgur.com/UputnOP.png","https://i.imgur.com/Jc4UAqN.png","https://i.imgur.com/dyW5NU0.png","https://i.imgur.com/Hddr37O.png","https://i.imgur.com/OZe1KTS.png","https://i.imgur.com/6P9OHCA.png","https://i.imgur.com/WqULYv2.png"]
            Rporn = random.choice(porn)
            embed = discord.Embed(title=f"{ctx.author}", color=random.choice(self.colors))
            embed.set_image(url=Rporn)
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            
      @commands.command(aliases=["cock", "penis"], pass_context=True)
      async def pp(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            ppsize = random.randint(0, 21)
            pp = ""

            if member == None:
                  for i in range(0, ppsize):
                      pp += "="
                  embed = discord.Embed(
                        description=f"8{pp}D", color=random.choice(self.colors))
                  embed.set_author(name=f"{ctx.author}'s pp", icon_url=ctx.author.avatar_url)
                  embed.set_footer(text=f"Requested By {ctx.author}")
                  await ctx.send(embed=embed)

            for i in range(0, ppsize):
                pp += "="
                embed = discord.Embed(
                  description=f"8{pp}D", color=random.choice(self.colors))
                embed.set_author(name=f"{member.name}'s pp", icon_url=member.avatar_url)
                embed.set_footer(text=f"Requested By {ctx.author}")
                await ctx.send(embed=embed)
    
      @commands.command(aliases=["gr", "homo"])
      async def gayrate(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            gay = random.randint(0, 100)
            if member == None:
                  embed = discord.Embed(
                  description=f"{gay}% gay", color=random.choice(self.colors))
                  embed.set_author(name=f"{ctx.author} is", icon_url=ctx.author.avatar_url)
                  embed.set_footer(text=f"requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(
                   description=f"{gay}% gay", color=random.choice(self.colors))
            embed.set_author(name=f"{member.name} is", icon_url=member.avatar_url)
            embed.set_footer(text=f"requested by {ctx.author}")
            await ctx.send(embed=embed)
                  
      @commands.command(pass_contex=True, aliases=['flip'])
      async def coinflip(self, ctx):
            await ctx.message.delete()
            sides = "Heads", "Tails"
            coin = ["https://www.lazygoblin.com/image/gold_coin_heads.png","https://www.lazygoblin.com/image/gold_coin_tails.png"]
            side = random.choice(sides)
            embed=discord.Embed(description=f"**It Landed On {side}!**", color=random.choice(self.colors))
            rsides = random.choice(coin)
            embed.set_image(url=rsides)
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

      @commands.command(pass_contex=True, aliases=['Hug'])
      async def hug(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            if member == None:
                  embed = discord.Embed(description = f"**{ctx.author.mention} Hugged {ctx.author.mention}**", color=random.choice(self.colors))
                  HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806539106707439656/hug.gif","https://cdn.discordapp.com/attachments/790405104280666122/806540353150124062/anime_hug_2.gif"]
                  rhug = random.choice(HUG)
                  embed.set_image(url=rhug)
                  embed.set_footer(text=f"Requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(description = f"**{ctx.author.mention} Hugged {member.mention}**", color=random.choice(self.colors))
            HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806539106707439656/hug.gif","https://cdn.discordapp.com/attachments/790405104280666122/806540353150124062/anime_hug_2.gif"]
            rhug = random.choice(HUG)
            embed.set_image(url=rhug)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)

      @commands.command(pass_contex=True, aliases=['Kiss'])
      async def kiss(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            if member == None:
                  embed = discord.Embed(description = f"**{ctx.author.mention} Kissed {ctx.author.mention}**", color=random.choice(self.colors))
                  HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806543272168128572/TBKlQSx.gif","https://cdn.discordapp.com/attachments/790405104280666122/806543009612955708/anime_kiss.gif"]
                  rhug = random.choice(HUG)
                  embed.set_image(url=rhug)
                  embed.set_footer(text=f"Requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(description = f"**{ctx.author.mention} Kissed {member.mention}**", color=random.choice(self.colors))
            HUG = ["https://cdn.discordapp.com/attachments/790405104280666122/806543272168128572/TBKlQSx.gif","https://cdn.discordapp.com/attachments/790405104280666122/806543009612955708/anime_kiss.gif"]
            rhug = random.choice(HUG)
            embed.set_image(url=rhug)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)

      
def setup(client):
    client.add_cog(Fun(client))
