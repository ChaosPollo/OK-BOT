import nextcord, asyncio, datetime, re
from nextcord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["ban"])
    @commands.has_guild_permissions(ban_members=True)
    async def ban_function(self, ctx, user : nextcord.Member = None, *, reason = None):
        
        await ctx.message.delete()

        if user == None:
            
            e = nextcord.Embed(description="❌ **| Debes mencionar a un usuario.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        elif user == ctx.author:

            e = nextcord.Embed(description="❌ **| No te puedes banear a ti mismo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        else:
            
            if reason == None:
                text = "No se ha dado una razon..."
            else:
                text = reason
                
            e = nextcord.Embed(title=f"{user.name} ha sido baneado", description=f"**Razon:** __{text}__\n**Fecha de baneo:** __{datetime.datetime.utcnow()}__\n**Servidor:** __{ctx.author.guild}__", color = nextcord.Color.from_rgb(30, 255, 165))
            e.set_thumbnail(url=user.display_avatar)
            e.set_footer(text=f"Autor del ban: {ctx.author.name}")
            await ctx.send(embed = e)
            
            try:
                await user.send(embed=e)
            except Exception:
                pass
            await user.ban()
            
    @commands.command(aliases = ["kick"])
    @commands.has_guild_permissions(kick_members=True)
    async def kick_function(self, ctx, user : nextcord.Member = None, *, reason = None):

        await ctx.message.delete()

        if user == None:
            
            e = nextcord.Embed(description="❌ **| Debes mencionar a un usuario.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        elif user == ctx.author:

            e = nextcord.Embed(description="❌ **| No te puedes expulsar a ti mismo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        else:
            
            if reason == None:
                text = "No se ha dado una razon..."
            else:
                text = reason
                
            e = nextcord.Embed(title=f"{user.name} ha sido expulsado", description=f"**Razon:** __{text}__\n**Fecha de expulsación:** __{datetime.datetime.utcnow()}__\n**Servidor:** __{ctx.author.guild}__", color=nextcord.Color.from_rgb(30, 255, 165))
            e.set_thumbnail(url=user.display_avatar)
            e.set_footer(text=f"Autor del kick: {ctx.author.name}")
            await ctx.send(embed = e)
            
            try:
                await user.send(embed=e)
            except Exception:
                pass
            try:
                await user.kick()
            except Exception as e:
                await ctx.send(e)
        
    @commands.command(aliases = ["unban"])
    @commands.has_guild_permissions(ban_members=True)
    async def unban_function(self, ctx, user : nextcord.User = None): 
        
        await ctx.message.delete()
        
        if user == None:

            e = nextcord.Embed(description="❌ **| Debes mencionar la id de un usuario.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        else:
            
            try:
                await ctx.author.guild.unban(user)
            except Exception as e:
                
                if re.search("Unknown Ban", e):
                    
                    e = nextcord.Embed(description=f"❌ **| El usuario {user} no esta baneado.**", color=nextcord.Color.red())
                    error = await ctx.send(embed = e)
                    await asyncio.sleep(3)
                    await error.delete()
                    return
            
            await ctx.send(f"**¡Usuario {user} ha sido desbaneado!**")
            
def setup(client):
    client.add_cog(Mod(client))