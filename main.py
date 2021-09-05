import time
import datetime
from time import sleep
import json
import random
import string
from os import system, name
import os
from discord.ext import commands
import colorama
import asyncio
import re
import urllib.parse 
import io
import aiohttp
import discord
import requests
from colorama import Fore
import urllib.request
from urllib import parse, request
colorama.init()



def clear():
  system("cls")

TOKEN = os.environ['tokenn']

token = (TOKEN)

ping = False

bot = commands.Bot(command_prefix=("$"), self_bot=True)


@bot.event
async def on_message(message):
  await bot.process_commands(message)

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='SuupraaMK4', url='https://www.twitch.tv/zemmett'))
  print(f"{Fore.YELLOW}Logged as {Fore.RED}{bot.user}")

bot.remove_command("help")

@bot.command()
async def help(ctx):
  embed = discord.Embed(title='Ayuda', description='`test` - Comando de prueba\n`purge` - Borra todos tus mensajes en una chat\n`hypesquad` - Cambia tu casa de hypesquad', color=0x1C1C1C)
  embed.set_footer(text='Youtube')
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/883782125508259910/884046054612406282/575cac3769dd5f9002300eb4913a2830.gif')
  await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title='Prueba', description='Esto es una prueba para YouTube', color=0x1C1C1C)
  embed.set_image(url='https://cdn.discordapp.com/attachments/541858594098774018/883176453875834900/3176e8e54324fb86064f22b6db71ffdc_1.gif')
  embed.set_footer(text='Prueba Youtube')
  await ctx.send(embed=embed)

@bot.command()
async def purge(message):
  async for msg in message.channel.history(limit=10000):
    if msg.author == bot.user:
      try:
        await msg.delete()
      except:
        pass

@bot.command()
async def hypesquad(ctx, house):
  await ctx.message.delete()
  request = requests.session()
  headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
  }

  global payload

  if house == "bravery":
    payload = {'house_id': 1}
  elif house == "brilliance":
    payload = {'house_id': 2}
  elif house == "balance":
    payload = {'house_id': 3}

  try:
    requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
    print(f"{Fore.GREEN}Has cambiado a {house} correctamente!")
  except:
    print(f"{Fore.RED}Ha ocurrido un error al intentar cambiarte a {house}")


  



while True:
  try:
    bot.run(token, bot=False)
  except:
    clear()
    print("El token es inválido")
    quit()
