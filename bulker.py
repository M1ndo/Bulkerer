# created by ybenel on 31/05/2021
# Discord Bot To Delete Message (Bullk)
import os,sys
import discord,logging
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO) # INFO || DEBUG
handler = logging.FileHandler(filename='logger.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Authorization: ODQyODU5MXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXz
Token = "ODQyODU5XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXz"
channelid = "" #Place Channel Id HereÎ

client = discord.Client()
bot = commands.Bot(command_prefix="$",self_bot=True)
@bot.event
async def on_ready():
    print("Discord Bot Ready")
    print("User %s Is Rocking It"%(bot.user))

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True

@bot.command(name='del_msg', help='testing command for dev use')
async def del_msg(ctx):
    msg = ctx.message.id
    print(f'DEBUG: message id is {msg}')
    await ctx.message.delete()
    channel = bot.get_channel(int(channelid))
    count = 0
    async for message in channel.history(limit=500):
        try:
            if message.author == bot.user:
                if count == 50:
                    break
                await message.delete()
                count += 1
        except:
            continue
    await ctx.send("Messages Deleted Successfully\n[+] Count: %s"%(count))

bot.run(Token,bot=False)
