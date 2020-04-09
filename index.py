# Python
import re
from urllib import parse,request 
"""
- "parse" nos ayudar a procesar una respuesta http
- "request" nos permite visitar una pagina de internet
"""
# Discord
import discord
from discord.ext import commands


# Utilities
import datetime
from decouple import config

bot = commands.Bot(command_prefix='-', description='Estes un Bot de ayuda') # Agregamos un simbolo para iniciar un comando para nuestro bot desde el chat

@bot.command()
async def ping(contexto):
    """Funcion de prueba
    
    Usamos asincronismo(corutina) por que la respuesta puede demorar.
    """
    await contexto.send('pong')

@bot.command()
async def sum(contexto, num1: int, num2:int):
    """ Suma de dos numeros.
    
    Utilizamos parametros para poder ejecutar la suma,
    El contexto tiene que estar primero en cada comando que creemos
    """
    await contexto.send(num1+num2)
# Event. Son piezas de codigo cuando pasa algo en un determinado tiempo inesperado

@bot.command()
async def info(contexto):
    """ Informacion del Servidor."""

    embed= discord.Embed(title='{}'.format(contexto.guild.name), description="Esto es una descripcion", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    """Agregando nuevos campos al mensaje"""
    embed.add_field(name="Fecha de creacion del servidor",value="{}".format(contexto.guild.created_at))
    embed.add_field(name="Propietario del servidor",value="{}".format(contexto.guild.owner))
    embed.add_field(name="Region del servidor",value="{}".format(contexto.guild.region))
    embed.add_field(name="ID del servidor",value="{}".format(contexto.guild.id))

    """Agregando una imagen al mensaje"""
    # embed.thumbnail(url='{}'.format(contexto.guild.icon))  # Podemos agregar la imagen que tiene nuestro servidor. Si no tiene imagen nuestro servidor dara error.
    embed.set_thumbnail(url="https://i0.pngocean.com/files/754/205/270/5bbc2d2d8be57.jpg")
    await contexto.send(embed=embed)  # Embed es un tipo de mensajes con un estilo diferente, se usa para mostrar mensajes que quieras que se resalten

@bot.command()
async def youtube(contexto, *, search):
    """ Comando para hacer busquedas en youtube
    Es importante dejar el * para que search pueda buscar por 2 palabras clave (Youtuber-tema)
    """
    query_string = parse.urlencode({'search_query': search})  # Convierte el texto del usuario a un busqueda de internet
    html_content = request.urlopen('http://www.youtube.com/results?'+query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})',html_content.read().decode())
    """ La expresion regular r'(href=\"\\/watch\\?v=(.{11})) buscara resultados parecidos a: href="/watch?v=71DZYl4Q4o8, pero solo nos devolvera la parte del id, esto lo hace con ayuda de los grupos usando paretensis '()'"""
    await contexto.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.event
async def on_ready():
    """Evento cuando se conecte.
    
    Este evento viene por defecto
    """
    # game= discord.Game('Developing the API') Agregamos un actividad que indica que esta jugando 
    # Esto lo colocamos agregando la variable a activity asi: await bot.change_presence(status=discord.Status.idle, activity=game)
    await bot.change_presence(status=discord.Status.idle)  # Agregamos un estado al momento de iniciar el bot.
    print('Mi bot esta ejecutandose')

bot.run(config('ACCESS_TOKEN'))  # Token creado desde discord developers
