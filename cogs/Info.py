import nextcord, asyncio, datetime
from nextcord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
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
        
    @commands.command(aliases = ["ping"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def ping_function(self, ctx):
        
        e = nextcord.Embed(title="🤖 | Estado del bot", description=f"**Ping:** *{self.bot.latency:.2f}ms*", color=nextcord.Color.red())
        await ctx.send(embed = e)
    
    @commands.command(aliases = ["userinfo"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    @commands.has_guild_permissions(administrator = True)
    async def userinfo_function(self, ctx, user : nextcord.Member = None):
        
        name = user.name
        avatar = user.display_avatar
        avatar_url = user.avatar
        id = user.id
        
        roles = user.roles
        join_sv = user.joined_at
        join_ds = user.created_at
        
        rlist = []
        
        for i in roles:
            if i.name != "@everyone":
                rlist.append(i.mention)
                
        rol = " ".join(rlist)
        
        e = nextcord.Embed(title=f"Información sobre {name}", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(23, 249, 227))
        e.add_field(name = "Información principal", value= f"**Nombre:** {name}\n**Avatar:** [Link]({avatar_url})\n**Id:** {id}")
        e.add_field(name = "Información Tecnica", value = "**Cuenta creada:** {}\n**Se unio al server:** {}".format(join_ds.strftime("%d/%m/%Y, %r"), join_sv.strftime("%d/%m/%Y, %r")))
        e.add_field(name = "Roles del servidor", value="".join(rol), inline=False)
        e.set_thumbnail(url=avatar)
        self.check_username(ctx.author.name)
        e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
        await ctx.send(embed = e)
        
def setup(client):
    client.add_cog(Info(client))