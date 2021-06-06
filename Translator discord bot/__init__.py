import discord
from discord.ext.commands import Bot
from discord import abc
from discord import client
import google_trans_new
import requests
from google_trans_new import google_translator

translator = google_translator()
detector = google_translator()

def translate(text):
    return(translator.translate(text, lang_tgt="en"))

bot = Bot(command_prefix='$')
TOKEN = 'ODQ5ODM0MzQ0Nzg4OTE4MzAz.YLg76A.MnMXCDqYkRfUSeuBJQBEVekGb48'
client = discord.Client()

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

#does translation on discord side
@bot.event
async def on_message(message):
    text = message.content
    if message.author.bot:
        return
    else:
        if text != translate(message.content) or detector.detect(text) != "en":
            channel = bot.get_channel(850923972504846346)
            await channel.send(translate(message.content))


bot.run(TOKEN)
