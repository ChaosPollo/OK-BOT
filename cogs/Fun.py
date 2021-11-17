import nextcord, asyncio, datetime
from nextcord import embeds
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["say", "decir"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def say_function(self, ctx, *, args = None):

        if args == None:
            await ctx.message.delete()
            r = await ctx.send("❗ | ¡Debes mencionar algo!")
            await asyncio.sleep(3)
            await r.delete()
        else:
            await ctx.message.delete()
            await ctx.send(args)

    @say_function.error
    async def say_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            r = await ctx.send(f"❗ | El comando `say` esta en cooldown por *{error.retry_after:.2f}s*")
            await asyncio.sleep(3)
            await r.delete()

    @commands.command(aliases = ["avatar"])
    @commands.command(2, 3, commands.BucketType.user)
    async def avatar(self, ctx, user : nextcord.Member = None):

        def check_username(name):
            global new_name
            if len(name) > 7:
                new_name = f"{name[:-5]}..."
            else:
                new_name = name

        if user == None:
            avatar = ctx.author.display_avatar

            check_username(ctx.author.name)

            e = nextcord.Embed(title=f"Avatar de {new_name}", color = nextcord.Color.random(), timestamp=datetime.datetime.utcnow())
            e.set_footer(text=f"URL: [Avatar url]({ctx.author.avatar})")
            await ctx.send(embed = e)

def setup(client):
    client.add_cog(Fun(client))