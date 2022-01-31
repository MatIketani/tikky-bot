import discord
import os
from discord.ext import commands
from discord.utils import get
import asyncio
from asyncio import sleep
from datetime import date
from datetime import datetime
import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout

client = commands.Bot(command_prefix='t.')

@commands.is_owner()
@client.command()
async def reloadcmds(ctx):
    os.startfile('main.py')
    await ctx.message.add_reaction('<:certo:739134394215825438>')
    await ctx.send(f'<:avatarlogo:738553001630761000> | Comandos recarregados com sucesso! [{ctx.message.author.mention}]')
    exit()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} servidores e {str(len(client.users))} membros!"))
    now = datetime.now()
    versao = 'v0.6'
    print(now.strftime(f'\n\n\nTikky carregado com sucesso!\nDia: %d/%m/%Y\nHora: %H:%M:%S\n\nVersão: {versao}'))

for filename in os.listdir('./comandos'):
    if filename.endswith('.py'):
        client.load_extension(f'comandos.{filename[:6]}')

client.create_guild

@commands.is_owner()
@client.command(name='eval')
async def _eval(ctx, *, body):
    """Evaluates python code"""
    env = {
        'ctx': ctx,
        'client': client,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        'source': inspect.getsource
    }

    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text)-1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))
    
    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:
                    
                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')

TOKEN = 'YOUR_TOKEN'
client.run(token)
