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
    print(f'{client.user} está online !')

@client.event
async def on_message(message):
    conteudo = message.content
    l_conteudo = conteudo.lower()
    num_random = random.randint(1,20)

#Verificação se foi o usuario que mandou a mensagem
    if message.author == client.user:
        return
    
#Enviando uma mensagem privada com a lista de comandos
    if l_conteudo.startswith('!help'):
        try:
            await message.author.send(f':notebook_with_decorative_cover: ***Lista de Comandos*** :notebook_with_decorative_cover:\n'+
                                  '***!roll d20*** --> :game_die: Rola um dado de 20 lados :game_die:\n'+
                                  '**!ap1** Mostra uma Imagme do Primeiro Apostolo\n'+
                                  '**!ap2** Mostra uma Imagme do Segundo Apostolo\n'+
                                  '**!ap3** Mostra uma Imagme do Trceiro Apostolo\n'+
                                  '**!ap4** Mostra uma Imagme do Quarto Apostolo\n'+
                                  '**!ap5** Mostra uma Imagme do Quinto Apostolo\n'+
                                  '**!apc5** Mostra uma Imagme do companheiro do Quinto Apostolo')
        except discord.errors.Forbidden:
            await message.channel.send('Não foi possivel enviar a mensagem, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)')
    
#Rolando um dado randomico no canal onde o comando foi usado
    if l_conteudo.startswith('!roll d20'):
        embed_dado = discord.Embed(
            title=':game_die: Dados Rolados!',
            description= (f'[***d20*** : {num_random}]'),
            color= 0x030bfc
        )
        embed_dado.set_footer(text=f"Dado do **{message.author}**")
        await message.channel.send(embed=embed_dado)
#enviando imagens
    if l_conteudo.startswith('!ap1'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_1.png'))
        
    if l_conteudo.startswith('!ap2'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_2.jpg'))
        
    if l_conteudo.startswith('!ap3'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_3.jpg'))
        
    if l_conteudo.startswith('!ap4'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_4.jpg'))
        
    if l_conteudo.startswith('!ap5'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_5.jpg'))
        
    if l_conteudo.startswith('!apc5'):
        await message.channel.send(file=discord.File('.\img\mostros/apostolo_cao_5.jpg'))

#Iniciando o bot usando o Token
client.run('TOKEN')