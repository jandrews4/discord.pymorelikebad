import discord
from discord.ext.commands import Bot
from google_trans_new import google_translator

translator = google_translator()
detector = google_translator()

def translate(text):
    return(translator.translate(text, lang_tgt="en"))

bot = Bot(command_prefix='$')
TOKEN = 'enter token'
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
            channel = bot.get_channel(enter channel id to put translations)
            #includes author in logging message
            await channel.send(str(message.author) + ' said ' + translate(message.content))


bot.run(TOKEN)

