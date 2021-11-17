import nextcord, asyncio
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["say", "decir"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def say_function(self, ctx, *, args = None):

        if args == None:
            await ctx.message.delete()
            r = await ctx.send("❗ ¡Debes mencionar algo!")
            await asyncio.sleep(3)
            await r.delete()
        else:
            await ctx.message.delete()
            await ctx.send(args)

    @say_function.error
    async def say_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            r = await ctx.send(f"❗ El comando esta en cooldown por {error.retry_after:.2f}s")
            await asyncio.sleep(3)
            await r.delete()

def setup(client):
    client.add_cog(Fun(client))