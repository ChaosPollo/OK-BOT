import nextcord, asyncio, datetime, requests, random, re, praw, typing
from nextcord.ext import commands
from PIL import Image
from io import BytesIO

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

    @commands.command(aliases = ["avatar"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def avatar_function(self, ctx, user : nextcord.Member = None):
        
        await ctx.message.delete()

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
            e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)

    @commands.command(aliases = ["binary", "binario"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def binary_function(self, ctx, op = None, *, args = None):

        await ctx.message.delete()
        self.check_username(ctx.author.name)
        url_decode = "https://some-random-api.ml/binary?decode={}"
        url_encode = "https://some-random-api.ml/binary?encode={}"
        
        if op == None:
            
            e = nextcord.Embed(description="❌ **| Debes elegir entre encode o decode.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return

        elif args == None:
            
            e = nextcord.Embed(description="❌ **| Debes escribir algo para traducirlo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        elif op == "encode":
            
            if len(args) <= 35:
                
                text = args.replace(" ", "%20")
                res = requests.get(url_encode.format(text))
                json = res.json()
                binary = json["binary"]
                
                e = nextcord.Embed(title="Texto a Binario", description=f"**Texto:**\n{args}\n\n**Binario:**\n{binary}", color=nextcord.Color.gold(), timestamp=datetime.datetime.utcnow())
                e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
                await ctx.send(embed = e)
                
            else:
                
                e = nextcord.Embed(description="❌ **| El texto debe tener menos de 35 caracteres.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()
                
        elif op == "decode":
            
            if len(args) <= 35 and args == int:
                
                text = args.replace(" ", "%20")
                res = requests.get(url_decode.format(text))
                json = res.json()
                textb = json["text"]
                
                e = nextcord.Embed(title="Binario a Texto", description=f"**Binario:**\n{args}\n\n**Texto:**\n{textb}", color=nextcord.Color.gold(), timestamp=datetime.datetime.utcnow())
                e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
                await ctx.send(embed = e)
            
            elif args != int:
                
                e = nextcord.Embed(description="❌ **| El texto debe tener binario no letras.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()

            else:

                e = nextcord.Embed(description="❌ **| El texto debe tener menos de 35 caracteres.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()
                
        else:
            
            e = nextcord.Embed(description="❌ **| Debes elegir entre encode o decode**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
    @commands.command(aliases = ["base64"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def base64_function(self, ctx, op = None, *, args = None):

        await ctx.message.delete()
        self.check_username(ctx.author.name)
        url_decode = "https://some-random-api.ml/base64?decode={}"
        url_encode = "https://some-random-api.ml/base64?encode={}"
        
        if op == None:
            
            e = nextcord.Embed(description="❌ **| Debes elegir entre encode o decode.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return

        elif args == None:
            
            e = nextcord.Embed(description="❌ **| Debes escribir algo para traducirlo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            
        elif op == "encode":
            
            if len(args) <= 100:
                
                text = args.replace(" ", "%20")
                res = requests.get(url_encode.format(text))
                json = res.json()
                base64 = json["base64"]
                
                e = nextcord.Embed(title="Codificación de Texto", description=f"**Texto:**\n{args}\n\n**Codigo:**\n{base64}", color=nextcord.Color.blurple(), timestamp=datetime.datetime.utcnow())
                e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
                await ctx.send(embed = e)
                
            else:
                
                e = nextcord.Embed(description="❌ **| El texto debe tener menos de 35 caracteres.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()
                
        elif op == "decode":
                
            text = args.replace(" ", "%20")
            res = requests.get(url_decode.format(text))
            json = res.json()
            textb = json["text"]
                
            e = nextcord.Embed(title="Decodificación de Base64", description=f"**Base64:**\n{args}\n\n**Texto:**\n{textb}", color=nextcord.Color.blurple(), timestamp=datetime.datetime.utcnow())
            e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
            await ctx.send(embed = e)
                
        else:
            
            e = nextcord.Embed(description="❌ **| Debes elegir entre encode o decode**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()

    @commands.command(aliases = ["tweet"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def tweet_function(self, ctx, member : typing.Optional[nextcord.Member] = None, *, args = None):
        
        await ctx.message.delete()
        
        if args == None:
            e = nextcord.Embed(description="❌ **| Debes escribir algo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()
            return
        
        replies = random.randint(100, 500)
        retweets = random.randint(100, 350)
        likes = random.randint(1, 100)
        
        url = "https://some-random-api.ml/canvas/tweet?avatar={}&username={}&displayname={}&comment={}&replies={}&retweets={}&likes={}k"

        if member == None:
            
            self.check_username(ctx.author.name)
            avatar = ctx.author.avatar
            name = new_name.replace(" ", "%20")
            text = args.replace(" ", "%20")
            
            new_url = url.format(avatar, name, name, text, replies, retweets, likes)
            
            e = nextcord.Embed(title = f"{new_name} ha posteado algo 🤔", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(0, 237, 224))
            e.set_image(url = new_url)
            await ctx.send(embed = e)
                
        else:
            
            self.check_username(member.name)
            avatar = member.avatar
            name = new_name.replace(" ", "%20")
            text = args.replace(" ", "%20")
            
            new_url = url.format(avatar, name, name, text, replies, retweets, likes)
            
            e = nextcord.Embed(title = f"{new_name} ha posteado algo 🤔", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(0, 237, 224))
            e.set_image(url = new_url)
            await ctx.send(embed = e)

    @commands.command(aliases = ["meme"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def meme_function(self, ctx):
        
        await ctx.message.delete()
        
        self.check_username(ctx.author.name)
        
        top = subredditMeme.top(limit = 25)
        mims = []
        for memes in top:
            mims.append(memes)
        
        meme = random.choice(mims)
        
        e = nextcord.Embed(timestamp=datetime.datetime.utcnow())
        e.add_field(name=meme.title, value=f"[Link del meme]({meme.url})", inline=False)
        e.set_image(url = meme.url)
        e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
        await ctx.send(embed = e)
        
    @commands.command(aliases = ["rip"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def rip_function(self, ctx, user : typing.Optional[nextcord.Member] = None, *, reason = "Desconocida..."):
        
        if user == None:
            user = ctx.author
            
        self.check_username(user.name)
            
        rip = Image.open("./img/rip.png")
        
        avatar = user.avatar.with_size(128)
        data = BytesIO(await avatar.read())         
        pfp  = Image.open(data)  
        
        pfp = pfp.resize((198,180))
        
        rip.paste(pfp, (140,200))
        
        rip.save("./img/command_rip.png")
        
        file = nextcord.File("./img/command_rip.png")
        
        e = nextcord.Embed(title=f"NOOO SE NOS MURIO {new_name.upper()} 😔", description=f"Razon de muerte: {reason}",timestamp=datetime.datetime.utcnow(), color=nextcord.Color.light_grey())
        e.set_image(url="attachment://command_rip.png")
        self.check_username(ctx.author.name)
        e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
        
        await ctx.send(embed=e, file=file)
        
    @commands.command(aliases = ["emojify"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def emoji_function(self, ctx, *, args = None):
        
        emojis = []
        
        if args == None:
            
            e = nextcord.Embed(description="❌ **| Debes escribir algo.**", color=nextcord.Color.red())
            error = await ctx.send(embed = e)
            await asyncio.sleep(3)
            await error.delete()

        else:
            
            if len(args) < 26:
                for i in args.lower():
                
                    if i.isalpha():
                        emoji = f":regional_indicator_{i}:"
                        emojis.append(emoji)
                        
                    elif i.isdecimal():
                        number = {"1" : "one" , "2" : "two" , "3" : "three" , "4" : "four" , "5" : "five" , "6" : "six" , "7" : "seven" , "8" : "eight" , "9" : "nine" , "0" : "zero"}
                        emoji = f":{number.get(i)}:" 
                        emojis.append(emoji)
                    else:
                        emojis.append(i)
                        emojis.append(i)
                        
                    emojis.append(" ")
                    
                await ctx.send("".join(emojis))
            
            else:
                
                e = nextcord.Embed(description="❌ **| El texto debe tener menos de 25 caracteres.**", color=nextcord.Color.red())
                error = await ctx.send(embed = e)
                await asyncio.sleep(3)
                await error.delete()
                
    @commands.command(aliases = ["wanted"])
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def wanted_function(self, ctx, user : nextcord.Member = None):
        
        if user == None:
            user = ctx.author
            
        self.check_username(user.name)
            
        rip = Image.open("./img/wanted.jpg")
        
        avatar = user.avatar.with_size(128)
        data = BytesIO(await avatar.read())         
        pfp  = Image.open(data)  
        
        pfp = pfp.resize((543,538))
        
        rip.paste(pfp, (166,423))
        
        rip.save("./img/command_wanted.jpg")
        
        file = nextcord.File("./img/command_wanted.jpg")
        
        e = nextcord.Embed(title=f"BUSCADO {new_name.upper()}",timestamp=datetime.datetime.utcnow(), color=nextcord.Color.yellow())
        e.set_image(url="attachment://command_wanted.jpg")
        self.check_username(ctx.author.name)
        e.set_footer(icon_url=ctx.author.display_avatar, text=f"Pedido por: {new_name}")
        
        await ctx.send(embed=e, file=file)
            
def setup(client):
    client.add_cog(Fun(client))