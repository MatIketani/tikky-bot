import discord
from discord.ext import commands
from discord.utils import find, get
import asyncio
from time import sleep
import time
import requests
from random import randint
from pyfiglet import Figlet
from mcstatus import MinecraftServer

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        inicio = time.perf_counter()
        message = await ctx.send('<:ping:738813929630859285> | Tikky está calculando sua latência...')
        fim = time.perf_counter()
        duracao = (inicio - fim) * 100
        await message.edit(content=f'**Pong!** <:ping:740633403061174272> | Sua latência é de {abs(round(duracao))}ms')
        return
            
class Dicio(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def dicionario(self, ctx, argumento, palavra):
        if argumento == 'near':
            r = requests.get(f'https://api.dicionario-aberto.net/near/{palavra}')
            texto = r.text
            texto = texto.replace('","', '\n')
            texto = texto[2:]
            texto = texto[:-2]
            if texto == '':
                await ctx.send(f'<:erro:738880635162198036> | Nenhum resultado encontrado! [{ctx.message.author.mention}]')
                return
            embed=discord.Embed(title=f"<:dicionario:738871552292028448> | Palavras semelhantes a {palavra}.", color=0x1bdaa1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/738515674242220035/738767497926541352/tiky_logo.png")
            embed.add_field(name='<:avatarlogo:738553001630761000> | Lista de Palavras', value=f"``{texto}``", inline=False)
            message = await ctx.send(f'Buscando... [{ctx.message.author.mention}]')
            await asyncio.sleep(3)
            await message.edit(content=f'<:certo:739134394215825438> | Busca realizada com sucesso! [{ctx.message.author.mention}]')
            await ctx.send(embed=embed)
        if argumento == 'semelhante':
            r = requests.get(f'https://api.dicionario-aberto.net/near/{palavra}')
            texto = r.text
            texto = texto.replace('","', '\n')
            texto = texto[2:]
            texto = texto[:-2]
            if texto == '':
                await ctx.send(f'<:erro:738880635162198036> | Nenhum resultado encontrado! [{ctx.message.author.mention}]')
                return
            message = await ctx.send(f'Buscando... [{ctx.message.author.mention}]')
            await asyncio.sleep(3)
            await message.edit(content=f'<:certo:739134394215825438> | Busca realizada com sucesso! [{ctx.message.author.mention}]')
            embed=discord.Embed(title=f"<:dicionario:738871552292028448> | Palavras semelhantes a {palavra}.", color=0x1bdaa1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/738515674242220035/738767497926541352/tiky_logo.png")
            embed.add_field(name='<:avatarlogo:738553001630761000> | Lista de Palavras', value=f"``{texto}``", inline=False)
            await ctx.send(embed=embed)

class Hex(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hex(self, ctx, cor=None):
        if cor == None:
            message = await ctx.send(f'<a:rolling:738527635600179302> | Gerando cor aleatória... [{ctx.message.author.mention}]')
            sorteio = randint(0,11)
            sleep(5)
            if sorteio == 1:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Preto``\n**HEX Color:** ``#000000``')
                return
            if sorteio == 2:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Azul``\n**HEX Color:** ``#0000FF``')
                return
            if sorteio == 3:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Cinza``\n**HEX Color:** ``#808080``')
                return
            if sorteio == 4:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Amarelo``\n**HEX Color:** ``#FFFF00``')
                return
            if sorteio == 5:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Rosa``\n**HEX Color:** ``#FF1493``')
                return
            if sorteio == 5:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Laranja``\n**HEX Color:** ``#FF8C00``')
                return
            if sorteio == 6:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Verde``\n**HEX Color:** ``#008000``')
                return
            if sorteio == 7:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Marrom``\n**HEX Color:** ``#964B00``')
                return
            if sorteio == 8:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Vermelho``\n**HEX Color:** ``#FF0000``')
                return
            if sorteio == 9:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Branco``\n**HEX Color:** ``#FFFFFF``')
                return
            if sorteio == 10:
                await message.edit(content='<:avatarlogo:738553001630761000> | **Cor gerada:** ``Lilás``\n**HEX Color:** ``#C8A2C8``')
                return

        if cor == 'preto' or cor == 'Preto' or cor == 'black' or cor == 'Black':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Preto``\n**HEX Color:** ``#000000``')
            return
        if cor == 'azul' or cor == 'Azul' or cor == 'blue' or cor == 'Blue':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Azul``\n**HEX Color:** ``#0000FF``')
            return
        if cor == 'cinza' or cor == 'Cinza' or cor == 'grey' or cor == 'Grey':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Cinza``\n**HEX Color:** ``#808080``')
            return
        if cor == 'amarelo' or cor == 'Amarelo' or cor == 'yellow' or cor == 'Yellow':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Amarelo``\n**HEX Color:** ``#FFFF00``')
            return
        if cor == 'rosa' or cor == 'Rosa' or cor == 'pink' or cor == 'Pink':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Rosa``\n**HEX Color:** ``#FF1493``')
            return
        if cor == 'laranja' or cor == 'Laranja' or cor == 'orange' or cor == 'Orange':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Laranja``\n**HEX Color:** ``#FF8C00``')
            return
        if cor == 'verde' or cor == 'Verde' or cor == 'green' or cor == 'Green':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Verde``\n**HEX Color:** ``#008000``')
            return
        if cor == 'marrom' or cor == 'Marrom' or cor == 'brown' or cor == 'Brown':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Marrom``\n**HEX Color:** ``#964B00``')
            return
        if cor == 'vermelho' or cor == 'Vermelho' or cor == 'red' or cor == 'Red':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Vermelho``\n**HEX Color:** ``#FF0000``')
            return
        if cor == 'branco' or cor == 'Branco' or cor == 'white' or cor == 'White':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Branco``\n**HEX Color:** ``#FFFFFF``')
            return
        if cor == 'Lilás' or cor == 'Lilás' or cor == 'purple' or cor == 'Purple':
            await ctx.send('<:avatarlogo:738553001630761000> | **Cor:** ``Lilás``\n**HEX Color:** ``#C8A2C8``')
            return

'''class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        for i in ctx.guild.invites():

        if ctx.guild.invites() != None:
            invite = await ctx.channel.create_invite(max_age=86400)
            await ctx.send(f'Invite **{ctx.guild.name}**: {invite}\nEsse invite durará **24 horas**. [{ctx.message.author.mention}]')
            return
        else:
            return'''

class BotInvite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def botinvite(self, ctx):
        url = 'https://discord.com/api/oauth2/authorize?client_id=738514164770668584&permissions=8&scope=bot'
        embed=discord.Embed(description=f'Você pode me adicionar em seu servidor clicando [aqui]({url}).', color=0x6cc5b5)
        await ctx.send(f'[{ctx.message.author.mention}]')
        await ctx.send(embed=embed)
        return

class Ascii(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def figlet(self, ctx, *, arg):
        f = Figlet(font='slant')
        lenght = len(arg)
        if lenght > 20:
            await ctx.send(f'Você excedeu o limite de **20** caracteres! [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return
        else:
            asciizado = f'```{f.renderText(arg)}```'
            await ctx.send(f'[{ctx.message.author.mention}] {asciizado}')
            await ctx.message.delete()
            return

class Minecraft(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def minecraft(self, ctx, ip, port=None):
        if port == None:
            server = MinecraftServer(f"{ip}", 25565)
            status = server.status()
            playercount = status.players.online
            ping = status.latency
            avatar = ctx.message.author.avatar_url
            nome = f'{ctx.message.author}'
            nome = nome[:-5]

            embed = discord.Embed(title=f'<:minecraft:742867662941716669> **Informações do servidor:** __{ip}__', description='Por conta de limitações da API, as informações serão mínimas.', color=0x6cc5b5)
            embed.add_field(name='**Número de Jogadores:**', value=f'{playercount} jogadores.', inline=False)
            embed.add_field(name='**Latência:**', value=f'{round(ping)}ms.', inline=False)
            embed.set_footer(text=f"Mensagem enviada por: {nome}", icon_url=f"{avatar}")
            await ctx.send(f'[{ctx.message.author.mention}]')
            await ctx.send(embed=embed)
            return
        
        else:
            server = MinecraftServer(f"{ip}", int(port))
            status = server.status()
            playercount = status.players.online
            ping = status.latency
            avatar = ctx.message.author.avatar_url
            nome = f'{ctx.message.author}'
            nome = nome[:-5]
            
            embed = discord.Embed(title=f'<:minecraft:742867662941716669> **Informações do servidor:** __{ip}__', description='Por conta de limitações da API, as informações serão mínimas.', color=0x6cc5b5)
            embed.add_field(name='**Número de Jogadores:**', value=f'{playercount} jogadores.', inline=True)
            embed.add_field(name='**Latência:**', value=f'{ping}ms.', inline=True)
            embed.set_footer(text=f"{nome}", icon_url=f"{avatar}")
            await ctx.send(f'[{ctx.message.author.mention}]')
            await ctx.send(embed=embed)
            return
            
    @minecraft.error
    async def minecraft_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'<:minecraft:742867662941716669> | Você deve especificar o **IP** e a **porta** do servidor. [{ctx.message.author.mention}]')
            return

def setup(client):
    client.add_cog(Ping(client))
    client.add_cog(Dicio(client))
    client.add_cog(Hex(client))
    client.add_cog(BotInvite(client))
    client.add_cog(Ascii(client))
    client.add_cog(Minecraft(client))
    '''client.add_cog(Invite(client))'''