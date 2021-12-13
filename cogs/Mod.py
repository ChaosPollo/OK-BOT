import nextcord, asyncio, datetime, re
from nextcord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.msg_content = None
        self.msg_user = None
        self.msg_id = None
        self.msg_guild = None
        
    def check_username(self, name):
        global new_name
        if len(name) > 7 and len(name) <= 10:
            new_name = f"{name[:-2]}..."
        elif len(name) > 10 and len(name) <= 15:
            new_name = f"{name[:-4]}..."
        elif len(name) > 15 and len(name) <= 20:
            new_name = f"{name[:-8]}..."
        elif len(name) > 20 and len(name) <= 25:
            new_name = f"{name[:-13]}..."
        elif len(name) > 25 and len(name) <= 30:
            new_name = f"{name[:-18]}..."
        elif len(name) > 30 and len(name) <= 35:
            new_name = f"{name[:-23]}..."
        else:
            new_name = name

    @commands.command(aliases = ["ban"])
    @commands.has_guild_permissions(ban_members=True)
    async def ban_function(self, ctx, user : nextcord.Member = None, *, reason = None):
        
        await ctx.message.delete()

        if user == None:
            
            e = nextcord.Embed(description="❌ **| Debes mencionar a un usuario.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        elif ctx.author.top_role.position < user.top_role.position:
            
            e = nextcord.Embed(description="❌ **| El usuario tiene un rango más alto.**", color=nextcord.Color.red())
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
            
        elif ctx.author.top_role.position < user.top_role.position:
            
            e = nextcord.Embed(description="❌ **| El usuario tiene un rango más alto.**", color=nextcord.Color.red())
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
  
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        
        self.msg_content = msg.content
        self.msg_user = msg.author.name
        self.msg_id = msg.id
        self.msg_guild = msg.guild.id
        await asyncio.sleep(60)
        self.msg_content = None
        self.msg_user = None
        self.msg_id = None
        self.sg_guild = None
            
    @commands.command(aliases = ["snipe"])
    async def snipe_function(self, ctx):
        
        if self.msg_content == None:
            
            e = nextcord.Embed(description=f"❌ **| No hay ningun mensaje borrado.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return
        
        elif self.msg_guild != ctx.guild.id:
            
            e = nextcord.Embed(description=f"❌ **| No hay ningun mensaje borrado.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return
        
        else:
            
            e = nextcord.Embed(title="Comando snipe 🔎", description=f"**Contenido:** {self.msg_content}\n**Usuario:** {self.msg_user}\n**Id del mensaje:** {self.msg_id}", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.dark_blue())
            self.check_username(ctx.author.name)
            e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
            e.set_thumbnail(url=ctx.author.display_avatar)
            await ctx.send(embed = e)
            
def setup(client):
    client.add_cog(Mod(client))