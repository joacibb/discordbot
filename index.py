
from urllib import response
import discord
from discord.ext import commands
from sqlalchemy import false
import requests
import lxml.html

TOKEN = 'OTA4ODQxOTY0ODE5MDU4NzE4.YY7nCQ.seDaqUq2qN3h_q75EKwIrfvHJt0'

client = discord.Client()

bot = commands.Bot(command_prefix = '+') #prefijo del bot

@bot.command(name='miragett')
async def miragett(ctx,lugar):
    if lugar == 'a' or lugar =='A':
        await ctx.send("https://gfycat.com/amusedshinyhummingbird")
        await ctx.send("https://gfycat.com/creamyorangefishingcat")
        await ctx.send("https://gfycat.com/recklesslinedfalcon")
    if lugar == 'medio' or lugar =='MEDIO' or lugar =='Medio':
        await ctx.send("https://gfycat.com/actualuncomfortableilladopsis")
    if lugar == 'b' or lugar =='B':
        await ctx.send("https://gfycat.com/coldembellishedherring")

@bot.command(name='miragect')
async def miragect(ctx,lugar):
    if lugar == 'a' or lugar =='A':
        await ctx.send("https://gfycat.com/fatherlyeachgonolek")
        await ctx.send("https://gfycat.com/angelicanothergerenuk")
        await ctx.send("https://gfycat.com/blondshabbyarcticduck")
    if lugar == 'medio' or lugar =='MEDIO' or lugar =='Medio':
        await ctx.send("https://gfycat.com/amusingmatureankolewatusi")
        await ctx.send("https://gfycat.com/competentbruiseddartfrog")
    if lugar == 'b' or lugar =='B':
        await ctx.send("https://gfycat.com/selfreliantacademicfieldmouse")

@bot.command(name='commands')
async def commands(ctx):
        await ctx.send("**+'mapa'ct 'zona'** Por ejemplo '+miragect A' para ver latas CT en A de Mirage . \n\n**+'mapa'tt 'zona'.** Por ejemplo '+miragett medio' para ver latas TT en medio de Mirage.\n\n**Los mapas que tengo disponibles son:** Mirage - Inferno\n\n**Las zonas son:** A, B y medio. \n\n**+cfg 'nombre del player':** para descargar el .cfg de forma directa. Por ejemplo '+cfg luken' \n\n**+profile 'nombre del player':** para ver resolucion, dpi, setup, etc. Por ejemplo: '+profile luken'" )
   
@bot.command(name='infernott')
async def infernott(ctx,lugar):
    if lugar == 'a' or lugar =='A':
        await ctx.send("https://gfycat.com/alarmingpleasantcapybara")
        await ctx.send("https://gfycat.com/warpedcheerygermanpinscher")
        await ctx.send("https://gfycat.com/imperfectdensebasenji")
    if lugar == 'medio' or lugar =='MEDIO' or lugar =='Medio':
        await ctx.send("https://gfycat.com/electricmelodicadeliepenguin")
    if lugar == 'b' or lugar =='B':
        await ctx.send("https://gfycat.com/achingflakyfattaileddunnart")
        await ctx.send("https://gfycat.com/admirableblissfulgermanpinscher")
        await ctx.send("https://gfycat.com/animatedflimsyconch")
        await ctx.send("https://gfycat.com/frayedhoarsebillygoat")

@bot.command(name='infernoct')
async def infernoct(ctx,lugar):
    if lugar == 'a' or lugar =='A':
        await ctx.send("https://gfycat.com/alarmingpleasantcapybara")
        await ctx.send("https://gfycat.com/barefavoritebarracuda")
    if lugar == 'medio' or lugar =='MEDIO' or lugar =='Medio':
        await ctx.send("https://gfycat.com/actualuncomfortableilladopsis")
    if lugar == 'b' or lugar =='B':
        await ctx.send("https://gfycat.com/amplealllark")
        await ctx.send("https://gfycat.com/sinfulclosedcaribou")

@bot.command(name='cfg')
async def cfg(ctx,nombre):
    html = 'https://prosettings.net/configs/'+nombre+'.zip'
    html2= 'https://liquipedia.net/counterstrike/'+nombre+'/'
    #doc = lxml.html.fromstring(html.content)
    await ctx.send('**Descarga directa segura: ** '+html+'\n\n**Si no lo encontraste podes buscar algo de info en : **'+html2)

@bot.command(name='profile')
async def profile(ctx,nombre):
    html = 'https://prosettings.net/counterstrike/'+nombre+'/'
    html2= 'https://liquipedia.net/counterstrike/'+nombre
    #doc = lxml.html.fromstring(html.content)
    await ctx.send('**Perfil de '+nombre+' : ** '+html+'\n\n**Tambien te puede servir: **'+html2)

bot.run('OTA4ODQxOTY0ODE5MDU4NzE4.YY7nCQ.seDaqUq2qN3h_q75EKwIrfvHJt0')  