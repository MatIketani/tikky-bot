import discord
from discord.ext import commands
from random import randint
from time import sleep
import asyncio
import sqlite3
import wget

#<a:rolling:738527635600179302>

class Flip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        sorteio = randint(0,2)
        if sorteio == 1:
            cara = '<:cara:738517860069933108>'
            message = await ctx.send(f'Tikky est� girando a moeda! [{ctx.message.author.mention}]')
            await asyncio.sleep(2)
            await message.edit(content=f'**Cara!** | Ap�s girar a moeda, Tikky encontrou {cara}. [{ctx.message.author.mention}]')
            return
        if sorteio == 2:
            coroa = '<:coroa:738518087850131567>'
            message = await ctx.send(f'Tikky est� girando a moeda! [{ctx.message.author.mention}]')
            await asyncio.sleep(2)
            await message.edit(content=f'**Coroa!** | Ap�s girar a moeda, Tikky encontrou {coroa}. [{ctx.message.author.mention}]')
            return

class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, *, membro : discord.Member=None):
        if membro == 'mitty#5578' or membro == 'mitty' or membro == '<@547159814824787978>':
            avaURL = membro.avatar_url
            wget.download(avaURL)

        if membro == None:
            avatarURL = ctx.message.author.avatar_url
            embed=discord.Embed(title=f'Clique no t��tulo para baixar.', url=f'{avatarURL}', color=0x6cc5b5)
            embed.set_image(url=avatarURL)
            emojilogo = '<:avatarlogo:738553001630761000>'
            await ctx.send(f'{emojilogo} | Esse � o seu avatar! [{ctx.message.author.mention}]')
            await ctx.send(embed=embed)
            return
        else:
            avatarURL = membro.avatar_url
            member = f'{membro}'
            member = member[:-5:]
            embed=discord.Embed(title=f'Clique no t��tulo para baixar.', url=f'{avatarURL}', color=0x6cc5b5)
            embed.set_image(url=avatarURL)
            emojilogo = '<:avatarlogo:738553001630761000>'
            await ctx.send(f' {emojilogo} | Avatar de {member}. [{ctx.message.author.mention}]')
            await ctx.send(embed=embed)
            return

class Calc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calc(self, ctx, num1, operador, num2):
        #Multiplicação.
        if operador == 'x':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 * numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        if operador == '.':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 * numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        if operador == '*':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 * numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        #Soma
        if operador == '+':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 + numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        #Subtração
        if operador == '-':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 - numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        #Divisão
        if operador == '/':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 / numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        if operador == ':':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 / numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        if operador == '÷':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 / numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da sua express�o aritm�tica �: **{calculo}**.')
            return
        #Potenciação
        if operador == '^':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 ** numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da express�o aritm�tica � **{calculo}**.')
            return
        if operador == '**':
            numero1 = int(num1)
            numero2 = int(num2)
            calculo = numero1 ** numero2
            message = await ctx.send('<:calculadora:738709606242582569> | Tikky est� calculando...')
            await asyncio.sleep(2)
            await message.edit(content=f'<:calculadora:738709606242582569> | O resultado da express�o aritm�tica � **{calculo}**.')
            return

class Cancelado(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cancelado(self, ctx, member):
        sorteio = randint(0,10)
        if sorteio == 1:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por militar demais. [{ctx.message.author.mention}]')
            return
        if sorteio == 2:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por por ainda usar Facebook. [{ctx.message.author.mention}]')
            return
        if sorteio == 3:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por ser TikToker. [{ctx.message.author.mention}]')
            return
        if sorteio == 4:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por usar foto de anime no perfil. [{ctx.message.author.mention}]')
            return
        if sorteio == 5:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por ser corno. [{ctx.message.author.mention}]')
            return
        if sorteio == 6:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por cancelar muito as pessoas. [{ctx.message.author.mention}]')
            return
        if sorteio == 7:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por ser pregui�oso. [{ctx.message.author.mention}]')
            return
        if sorteio == 8:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por dormir demais. [{ctx.message.author.mention}]')
            return
        if sorteio == 9:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por n�o tomar banho. [{ctx.message.author.mention}]')
            return
        if sorteio == 10:
            await ctx.send(f'<:twitter:738721075524796497> | {member} foi cancelado por ouvir K-Pop. [{ctx.message.author.mention}]')
            return

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, tudo):
        await ctx.send(f'{tudo}')
        return

class Ship(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ship(self, ctx, memberone, membertwo):
        conn = sqlite3.connect('databases/ship.db')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT * FROM ships
        WHERE membro1 = '{memberone}' AND membro2 = '{membertwo}' ''')
        for linha in cursor.fetchall():
            print(linha)

        conn.close()

def setup(client):
    client.add_cog(Flip(client))
    client.add_cog(Avatar(client))
    client.add_cog(Calc(client))
    client.add_cog(Cancelado(client))
    client.add_cog(Say(client))
    client.add_cog(Ship(client))
