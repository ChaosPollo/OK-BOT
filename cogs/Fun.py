import nextcord, asyncio, datetime, requests, random, re
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def check_username(self, name):
        global new_name
        if len(name) > 7 and len(name) <= 10:
            new_name = f"{name[:-3]}..."
        elif len(name) > 10 and len(name) <= 15:
            new_name = f"{name[:-5]}..."
        elif len(name) > 15 and len(name) <= 20:
            new_name = f"{name[:-10]}..."
        elif len(name) > 20 and len(name) <= 25:
            new_name = f"{name[:-15]}..."
        elif len(name) > 25 and len(name) <= 30:
            new_name = f"{name[:-20]}..."
        elif len(name) > 30 and len(name) <= 35:
            new_name = f"{name[:-25]}..."
        else:
            new_name = name

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
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def avatar_function(self, ctx, user : nextcord.Member = None):

        if user == None or user == ctx.author:
            avatar = ctx.author.display_avatar

            self.check_username(ctx.author.name)

            e = nextcord.Embed(color = nextcord.Color.random(), timestamp=datetime.datetime.utcnow())
            e.add_field(name=f"TU AVATAR", value=f"URL: [Avatar URL]({ctx.author.avatar})")
            e.set_image(url=avatar)
            e.set_footer(text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)
        else:
            avatar = user.display_avatar

            self.check_username(user.name)

            e = nextcord.Embed(color = nextcord.Color.random(), timestamp=datetime.datetime.utcnow())
            e.add_field(name=f"Avatar de {new_name}", value=f"URL: [Avatar URL]({user.avatar})")
            e.set_image(url=avatar)
            self.check_username(ctx.author.name)
            e.set_footer(text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)

    @avatar_function.error
    async def avatar_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            r = await ctx.send(f"❗ | El comando `avatar` esta en cooldown por *{error.retry_after:.2f}s*")
            await asyncio.sleep(3)
            await r.delete()

    @commands.command(aliases = ["binary", "binario"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def binary_function(self, ctx, *, args = None):

        self.check_username(ctx.author.name)

        if args == None:
            await ctx.message.delete()
            r = await ctx.send("❗ | ¡Debes mencionar algo!")
            await asyncio.sleep(3)
            await r.delete()
        else:
            if len(args) <= 35:
                text = args.replace(" ", "%20")
                res = requests.get(f"https://some-random-api.ml/binary?encode={text}")
                json = res.json()
                binary = json["binary"]
                e = nextcord.Embed(title="Traductor Binario", description=f"**Texto original:**\n{args}\n\n**Binario:**\n{binary}", color=nextcord.Color.gold(), timestamp=datetime.datetime.utcnow())
                e.set_footer(text=f"Pedido por: {new_name}")
                await ctx.send(embed = e)
                await ctx.message.delete()
            else:
                await ctx.message.delete()
                r = await ctx.send("❌ | El texto no puede tener más de 35 caracteres")
                await asyncio.sleep(3)
                await r.delete()

    @binary_function.error
    async def binary_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            r = await ctx.send(f"❗ | El comando `binary` esta en cooldown por *{error.retry_after:.2f}s*")
            await asyncio.sleep(3)
            await r.delete()

    @commands.command(aliases = ["tweet"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def tweet_function(self, ctx, *, args = None):

        self.check_username(ctx.author.name)

        avatar = ctx.author.avatar
        name = new_name.replace(" ", "%20")
        replies = random.randint(100, 500)
        retweets = random.randint(100, 350)
        likes = random.randint(1, 100)

        if args == None:
            text = ["Se%20murio%20mientras%20escribia...", "Se%20aburrio%20de%20escribir...", "Simplemente%20no%20escribio%20nada...", "AMOGUS!"]
            textR = random.choice(text)
            url = f"https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={name}&displayname={name}&comment={textR}&replies={replies}&retweets={retweets}&likes={likes}k"
            await ctx.send(url)
            await ctx.message.delete()
        else:
            text = args.replace(" ", "%20")
            url = f"https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={name}&displayname={name}&comment={text}&replies={replies}&retweets={retweets}&likes={likes}k"
            await ctx.send(url)
            await ctx.message.delete()

    @tweet_function.error
    async def tweet_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            r = await ctx.send(f"❗ | El comando `tweet` esta en cooldown por *{error.retry_after:.2f}s*")
            await asyncio.sleep(3)
            await r.delete()

def setup(client):
    client.add_cog(Fun(client))