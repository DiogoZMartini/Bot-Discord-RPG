import discord
import random

#Declarando as intenções do bot
intents = discord.Intents.default()
intents. message_content = True

#Criação do bot, setando o prefixo e intenções
client = discord.Client(intents=intents)

#Quando o bot iniciar mostrara uma mensagem no terminal
@client.event
async def on_ready():
    print(f"{client.user} está online !")

@client.event
async def on_message(message):
    conteudo = message.content
    l_conteudo = conteudo.lower()
    numero = random.randint(1,20)
    
    if message.author == client.user:
        return
    
    if l_conteudo.startswith('t!roll d20'):
        await message.channel.send(f':game_die: Dados Rolados! \n [***d20*** : {numero}]')
        

#Iniciando o bot usando o Token
client.run('TOKEN')