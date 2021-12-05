from logging import exception
import nextcord, dotenv, os, asyncio, datetime
from nextcord.ext import commands

dotenv.load_dotenv()
client = commands.Bot(command_prefix="o!")
client.remove_command('help')

@client.event
async def on_ready():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
                print(f"[+] Se ha cargado {file[:-3]}")
            except Exception as error:
                print(f"[-] No se ha cargado el modulo {file[:-3]} por: {error}")
    print("¡SE HA INICIADO EL BOT!")
    
@client.event
async def on_command_error(ctx, error):
    
    if isinstance(error, commands.CommandNotFound):
        
        await ctx.message.delete()
        
        cmdbeta = str(error.args).replace("('Command ", "")
        cmdbeta2 = str(cmdbeta).replace(" is not found',)", "")
        
        e = nextcord.Embed(description=f"❌ **| El comando `{cmdbeta2}` no ha sido encontrado, use `o!help` para ver todos los comandos.**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(5)
        await error.delete()    
        
    if isinstance(error, commands.CommandOnCooldown):
        
        await ctx.message.delete()
        e = nextcord.Embed(description=f"❌ **| Este comando esta en cooldown por {error.retry_after:.2f}s**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(3)
        await error.delete()
    
    if isinstance(error, commands.BotMissingPermissions):
        
        await ctx.message.delete()
        e = nextcord.Embed(description=f"❌ **| El bot no tiene permisos necesarios.**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(5)
        await error.delete()  
        
    if isinstance(error, commands.MissingPermissions):

        await ctx.message.delete()
        e = nextcord.Embed(description=f"❌ **| Usted no tiene permisos suficientes para ejecutar este comando.**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(3)
        await error.delete()  
        
    if isinstance(error, commands.MemberNotFound):
        
        await ctx.message.delete()
        e = nextcord.Embed(description=f"❌ **| El miembro no se ha encontrado.**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(3)
        await error.delete()
        
    if isinstance(error, commands.UserNotFound):

        await ctx.message.delete()
        e = nextcord.Embed(description=f"❌ **| El usuario no se ha encontrado.**", color=nextcord.Color.red())
        error = await ctx.send(embed = e)
        await asyncio.sleep(3)
        await error.delete() 
    
@client.command(aliases = ["help", "ayuda"])
async def help_function(ctx):
    
    e = nextcord.Embed(title = "📔 Ayuda | Ok bot", description="**❓ | Prefix:** `o!`\n**🦺 | Desarrollador:** `Mr. Pollo`\n**📖 | Libreria:** `nextcord`", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.from_rgb(252, 255, 30))
    e.add_field(name="🎃 | Diversión", value="`say` `avatar` `tweet` `binary` `meme` `rip` `emojify` `wanted`", inline=False)
    e.add_field(name="🎩 | Moderación", value="`ban` `kick` `unban`", inline=False)
    e.add_field(name="🦺 | Información", value="`ping`", inline=False)
    e.add_field(name="🎫 | Invitación", value="**[Invite](https://discord.com/api/oauth2/authorize?client_id=898721894889582652&permissions=17649690726&scope=bot)**", inline=False)
    e.set_footer(text=f"Pedido por: {ctx.author.name}")
    await ctx.send(embed = e)

client.run(os.getenv("TOKEN"))