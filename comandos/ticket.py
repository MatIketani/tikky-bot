import discord
from discord.ext import commands
from discord.utils import get, find
import sqlite3
import asyncio

class BugReport(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, *, bug):
        conn = sqlite3.connect('databases/tickets.db')
        cursor = conn.cursor()

        p_report = bug
        p_reporter = ctx.message.author

        # armazena os valores em variáveis únicas
        full_report = (f'{p_reporter}', f'{p_report}')
        sql_values = ''' INSERT INTO reports (reporter, bug) VALUES (?,?)'''
        
        # envia apenas 2 argumentos pra dentro da função cursor.execute
        message = await ctx.send('<:avatarlogo:738553001630761000> | Enviando report.')
        cursor.execute(sql_values, full_report)

        conn.commit()
        await asyncio.sleep(5)
        await message.edit(content='<:certo:739134394215825438> | Bug Report enviado com sucesso!')
        conn.close()
        return

def setup(client):
    client.add_cog(BugReport(client))