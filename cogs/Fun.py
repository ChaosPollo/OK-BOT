import nextcord, asyncio, datetime, requests, random, re, praw, typing
from nextcord.ext import commands

reddit = praw.Reddit(client_id = "z9x0j67BXBb2m0aDz1jnzA", 
                     client_secret = "JafIAV9_1PONVDtUImI0tembAkJaVA", 
                     username = "Mr-Pollo21", 
                     password = "tom45_43", 
                     user_agent = "Ok bot meme gen")

subredditMeme = reddit.subreddit("SpanishMeme")

class Fun(commands.Cog):
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

    #################
    ## Comando say ##
    #################

    @commands.command(aliases = ["say", "decir"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def say_function(self, ctx, *, args = None):

        if args == None:
            await ctx.message.delete()
            e = nextcord.Embed(description="❌ **| Debes escribir algo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
        else:
            await ctx.message.delete()
            await ctx.send(args)

    @say_function.error
    async def say_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
    ####################
    ## Comando avatar ##
    ####################


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
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
    ####################
    ## Comando binary ##
    ####################


    @commands.command(aliases = ["binary", "binario"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def binary_function(self, ctx, *, args = None):

        self.check_username(ctx.author.name)

        if args == None:
            await ctx.message.delete()
            e = nextcord.Embed(description="❌ **| Debes escribir algo para traducirlo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
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
                e = nextcord.Embed(description="❌ **| El texto debe tener menos de 35 caracteres.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()

    @binary_function.error
    async def binary_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
    ###################
    ## Comando tweet ##
    ###################

    @commands.command(aliases = ["tweet"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def tweet_function(self, ctx, member : typing.Optional[nextcord.Member] = None, *, args = None):
        
        if args == None:
            await ctx.message.delete()
            e = nextcord.Embed(description="❌ **| Debes escribir algo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return
        
        replies = random.randint(100, 500)
        retweets = random.randint(100, 350)
        likes = random.randint(1, 100)

        if member == None:

            self.check_username(ctx.author.name)
            avatar = ctx.author.avatar
            name = new_name.replace(" ", "%20")

            text = args.replace(" ", "%20")
            e = nextcord.Embed(title = f"{new_name} ha posteado algo 🤔", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(0, 237, 224))
            e.set_image(url = f"https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={name}&displayname={name}&comment={text}&replies={replies}&retweets={retweets}&likes={likes}k")
            e.set_footer(text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)
            await ctx.message.delete()
                
        else:
            self.check_username(member.name)
            avatar = member.avatar
            name = new_name.replace(" ", "%20")
            
            text = args.replace(" ", "%20")
            e = nextcord.Embed(title = f"{new_name} ha posteado algo 🤔", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(0, 237, 224))
            e.set_image(url = f"https://some-random-api.ml/canvas/tweet?avatar={avatar}&username={name}&displayname={name}&comment={text}&replies={replies}&retweets={retweets}&likes={likes}k")
            self.check_username(ctx.author.name)
            e.set_footer(text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)
            await ctx.message.delete()

    @tweet_function.error
    async def tweet_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
    ##################
    ## Comando meme ##
    ##################

    @commands.command(aliases = ["meme"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def meme_function(self, ctx):
        
        top = subredditMeme.top(limit = 25)
        mims = []
        for memes in top:
            mims.append(memes)
        
        meme = random.choice(mims)
        
        e = nextcord.Embed(timestamp=datetime.datetime.utcnow())
        e.add_field(name=meme.title, value=f"[Link del meme]({meme.url})", inline=False)
        e.set_image(url = meme.url)
        e.set_footer(text=f"Pedido por: {ctx.author.name}")
        await ctx.send(embed = e)
        
    @meme_function.error
    async def meme_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
def setup(client):
    client.add_cog(Fun(client))