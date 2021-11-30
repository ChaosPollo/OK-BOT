import nextcord, asyncio
from nextcord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ["ping"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def ping_function(self, ctx):
        
        e = nextcord.Embed(title="🤖 | Estado del bot", description=f"**Ping:** *{self.bot.latency:.2f}ms*", color=nextcord.Color.red())
        await ctx.send(embed = e)
        
    @ping_function.error
    async def ping_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
        
def setup(client):
    client.add_cog(Info(client))