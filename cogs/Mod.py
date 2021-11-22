import nextcord, asyncio, datetime
from nextcord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["ban"])
    @commands.has_guild_permissions(ban_members=True)
    async def ban_function(self, ctx, user : nextcord.Member = None, *, reason = None):

        if user == None:
            await ctx.message.delete()
            r = await ctx.send("❗ | ¡Debes mencionar a un usuario!")
            await asyncio.sleep(3)
            await r.delete()
        elif user == ctx.author:
            await ctx.message.delete()
            r = await ctx.send("❌ | No te puedes banear a ti mismo")
            await asyncio.sleep(3)
            await r.delete()
        else:
            if reason == None:
                text = "No se ha dado una razon..."
            else:
                text = reason
            e = nextcord.Embed(title=f"{user.name} ha sido baneado", description=f"Razon: {text}\nFecha de baneo: {datetime.datetime.utcnow()}\nServidor: {ctx.author.guild}", color=nextcord.Color.red())
            e.set_thumbnail(url=user.display_avatar)
            e.set_footer(text=f"Autor del ban: {ctx.author.name}")
            await ctx.send(embed = e)
            try:
                await user.send(embed=e)
            except Exception:
                pass
            await user.ban()

def setup(client):
    client.add_cog(Mod(client))