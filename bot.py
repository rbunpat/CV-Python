# bot.py
import http
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
import nmap
import pyshorteners

import discord
from discord.ext import commands

import cvpython

#get discord token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bltoken = os.getenv('BITLY_TOKEN')
#logging shit
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#specify bot command prefix
bot = commands.Bot(command_prefix='!')
#finallu, the bot comamnds
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Type !help for bot help'))
    print(f'{bot.user.name} has connected to Discord!')
    return

@bot.command()
async def ping(ctx):
    await ctx.send(f'{ctx.author.name}')
    return

@bot.command(name='covid', help='Check Surat Thani covid situation')
async def covid(ctx):
        print('!covid command detected')
        cvpython.run()
        response = cvpython.output
        await ctx.send(response)
        print('!covid response sent')
        return

@bot.command(name='api', help='Show API URL')
async def api(ctx):
        print('!api command detected')
        response = cvpython.response_API.url
        await ctx.send(response)
        print('!api response sent')
        return

@bot.command(name='shutdown', help='Shutdown Bot')
async def shutdown(ctx):
        if ctx.author.id == int(os.getenv('OWNER_ID')):
                await ctx.send('Shutting down...')
                await bot.logout()
        else:
                await ctx.send('You are not authorized to shutdown the bot')
        return

@bot.command(name='time', help='tells you the time')
async def test(ctx):
        await ctx.send(datetime.now().strftime('%H:%M:%S'))
        return

@bot.command(name='statchk', help='check if ip address is up')
async def portscan(ctx, addr):
        await ctx.send(f'Pinging {addr}...')
        nm = nmap.PortScanner()
        nm.scan(hosts=addr, arguments='-O')
        for host in nm.all_hosts():
                await ctx.send(f'{host} {nm[host].state()}')
        return

@bot.command(name='bitly', help='Shorten URL with bitly')
async def bitly(ctx, url):
        await ctx.send(f'Shortening {url}...')
        type_bitly = pyshorteners.Shortener(api_key=bltoken)
        if ('http://') in url:
                short_url = type_bitly.bitly.short(url)
        elif ('https://') in url:
                short_url = type_bitly.bitly.short(url)
        else: 
                short_url = type_bitly.bitly.short(f'http://{url}')
        await ctx.send(f'{short_url}')
        return



bot.run(TOKEN)