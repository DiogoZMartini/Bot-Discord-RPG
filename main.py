import discord
from discord.ext import commands
import random

#Declarando as intenções do bot
intents = discord.Intents.default()
intents. message_content = True

#Criação do bot, setando o prefixo e intenções
bot =  commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def d20(ctx):
 numero = random.randint(1,20)
 await ctx.send(numero)
#Iniciando o bot usando o Token
bot.run('token')
    