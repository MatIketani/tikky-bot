import discord
from discord.ext import commands
from discord.utils import find, get
import asyncio

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.send(f'<:erro:738880635162198036> | Um erro inesperado aconteceu... tente novamente! [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return


        autor = ctx.message.author
        await member.send(f'<:avatarlogo:738553001630761000> | Você foi banido permanentemente do servidor ``{ctx.guild.name}``.')
        await member.ban(reason=reason)
        await autor.send(f'<:certo:739134394215825438> | ``{member}`` foi banido permanentemente!')
        await ctx.message.delete()
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'<:erro:738880635162198036> | Um erro inesperado aconteceu... tente novamente! [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Banir Usuários``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banidos = await ctx.guild.bans()
        nome, discriminator = member.split('#')

        for ban_entry in banidos:
            user = ban_entry.user

            if (user.name, user.discriminator) == (nome, discriminator):
                await ctx.guild.unban(user)
                await ctx.message.delete()
                autor = ctx.message.author
                await autor.send(f' <:certo:739134394215825438> | ``{user}`` desbanido.')
                return
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'<:erro:738880635162198036> | Um erro inesperado aconteceu... tente novamente! [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Banimentos``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class Clear(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, quant=100):
        mensagens = []
        async for message in ctx.message.channel.history(limit=quant):
            mensagens.append(message)
        if quant == None:
            await ctx.send(f'<:erro:738880635162198036> | Especifique uma quantidade de mensagens a serem apagadas (``2`` a ``100`` mensagens).')
            return
        if quant > 100:
            await ctx.send(f'<:erro:738880635162198036> | Você pode apagar no máximo ``100`` mensagens.')
            return
        if quant < 2:
            await ctx.send(f'<:erro:738880635162198036> | Você deve apagar no máximo ``2`` mensagens.')
            return
        await message.channel.purge(limit=quant)
        autor = ctx.message.author
        await autor.send(f'<:certo:739134394215825438> | Você apagou ``{quant}`` mensagens no chat ``#{ctx.message.channel.name}`` do grupo ``{ctx.guild.name}``.')
        await ctx.message.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Mensagens``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member : discord.Member, tempo=None, *, motivo=None):
        autor = ctx.message.author
        role = get(member.guild.roles, name = 'Muted') or get(member.guild.roles, name = 'Mutado') or get(member.guild.roles, name = 'Silenciado') or get(member.guild.roles, name = 'Silenced') or get(member.guild.roles, name = 'Silencied')
        if tempo == None:
            if motivo != None:
                await member.add_roles(role)
                await member.send(f'<:avatarlogo:738553001630761000> | Você foi mutado no servidor ``{ctx.guild.name}``.\nMotivo: ``{motivo}``.')
                await autor.send(f'<:certo:739134394215825438> | ``{member}`` mutado com sucesso.')
                return
            else:
                await member.add_roles(role)
                await member.send(f'<:avatarlogo:738553001630761000> | Você foi mutado no servidor ``{ctx.guild.name}``.')
                await autor.send(f'<:certo:739134394215825438> | ``{member}`` mutado com sucesso.')
                return
        if tempo != None:
            if motivo != None:
                await member.add_roles(role)
                await member.send(f'<:avatarlogo:738553001630761000> | Você foi mutado no servidor ``{ctx.guild.name}``.\nTempo: ``{tempo} minutos.``\nMotivo: ``{motivo}``.')
                await autor.send(f'<:certo:739134394215825438> | ``{member}`` mutado com sucesso.')

                await asyncio.sleep(tempo * 60)

                await member.remove_roles(role)
                await member.send(f'<:avatarlogo:738553001630761000> | Você foi desmutado do servidor ``{ctx.guild.name}``.')
        else:
            await member.add_roles(role)
            await member.send(f'<:avatarlogo:738553001630761000> | Você foi mutado no servidor ``{ctx.guild.name}``.\nTempo: ``{tempo} minutos.``')
            await autor.send(f'<:certo:739134394215825438> | ``{member}`` mutado com sucesso.')

            await asyncio.sleep(tempo * 60)

            await member.remove_roles(role)
            await autor.send(f'<:avatarlogo:738553001630761000> | O usuário ``{member}`` ficou mutado por **{tempo} minutos** e foi desmutado da guilda ``{ctx.guild.name}``.')
            await member.send(f'<:avatarlogo:738553001630761000> | Você foi desmutado do servidor ``{ctx.guild.name}``.')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Cargos``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class Unmute(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        autor = ctx.message.author
        role = get(member.guild.roles, name = 'Muted') or get(member.guild.roles, name = 'Mutado') or get(member.guild.roles, name = 'Silenciado') or get(member.guild.roles, name = 'Silenced') or get(member.guild.roles, name = 'Silencied')

        await autor.send(f'<:certo:739134394215825438> | ``{member}`` desmutado com sucesso.')
        await member.remove_roles(role)
        await member.send('<:avatarlogo:738553001630761000> | Você foi desmutado do servidor ``{ctx.guild.name}``.')
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Cargos``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class LockUnlock(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_permissions=True)
    @commands.command()
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f'🔐 | Canal trancado com sucesso! [{ctx.message.author.mention}]')
        return
    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Permissões``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

    @commands.has_permissions(manage_permissions=True)
    @commands.command()
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(f'🔐 | Canal destrancado com sucesso! [{ctx.message.author.mention}]')
        return
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Permissões``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return

class Slowmode(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_permissions=True)
    @commands.command()
    async def slowmode(self, ctx, tempo: int):
        if tempo == 0:
            await ctx.channel.edit(slowmode_delay=tempo)
            await ctx.send(f'<:tartaruga:743064078456455200> | Slowmode desligado com sucesso. [{ctx.message.author.mention}]')
            return
        else:
            await ctx.channel.edit(slowmode_delay=tempo)
            await ctx.send(f'<:tartaruga:743064078456455200> | Slowmode de {str(tempo)}s setado com sucesso. [{ctx.message.author.mention}]')
            return
    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f'<:erro:738880635162198036> | Você não tem permissões para ``Gerenciar Permissões``. [{ctx.message.author.mention}]')
            await ctx.message.delete()
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'<:erro:738880635162198036> | Você deve escolher o tempo (segundos) para adicionar o Slowmode. [{ctx.message.author.mention}]')
            return

def setup(client):
    client.add_cog(Ban(client))
    client.add_cog(Unban(client))
    client.add_cog(Clear(client))
    client.add_cog(Mute(client))
    client.add_cog(Unmute(client))
    client.add_cog(LockUnlock(client))
    client.add_cog(Slowmode(client))