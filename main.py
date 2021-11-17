import nextcord, dotenv, os, asyncio
from nextcord.ext import commands

dotenv.load_dotenv()
client = commands.Bot(command_prefix="&")

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

client.run(os.getenv("TOKEN"))