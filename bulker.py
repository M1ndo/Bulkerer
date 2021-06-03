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

@bot.command(name='del_msg', help='Message to delete (require arg)')
async def del_msg(ctx,*,times:str):
    msg = ctx.message.id
    channel_id = ctx.message.channel.id
    # print(f'DEBUG: message id is {msg}')
    # print(f'DEBUG: Channel id is {channel}')
    await ctx.message.delete()
    t = int(times) or 100
    channel = bot.get_channel(channel_id)
    count = 0
    async for message in channel.history(limit=t):
        if message.author == bot.user:
            try:
                await message.delete()
                count += 1
            except:
                continue
    print(f'DEBUG: Messages Deleted Successfully\n[+] Count {count}')

@bot.command(name='destiny',help="Playing Destiny 2")
async def destiny(ctx):
    await bot.change_presence(activity=discord.Game(name="Destiny 2"))
    await ctx.message.delete()

@bot.command(name='rocket',help="Playing Rocket League")
async def rocket(ctx):
    await bot.change_presence(activity=discord.Game(name="Rocket League"))
    await ctx.message.delete()

@bot.command(name='apex',help="Playing Apex Legends")
async def apex(ctx):
    await bot.change_presence(activity=discord.Game(name="Apex Legends"))
    await ctx.message.delete()

@bot.command(name='volorant',help="Playing VOLORANT")
async def volorant(ctx):
    await bot.change_presence(activity=discord.Game(name="VOLORANT"))
    await ctx.message.delete()

@bot.command(name='csgo',help="Playing Counter-Strike: Global Offensive")
async def csgo(ctx):
    await bot.change_presence(activity=discord.Game(name="Counter-Strike: Global Offensive"))
    await ctx.message.delete()

@bot.command(name='gtav',help="GTA V")
async def gtav(ctx):
    await bot.change_presence(activity=discord.Game(name="GTA V"))
    await ctx.message.delete()

@bot.command(name='cod',help="Playing Call of Duty®: Modern Warfare®")
async def cod(ctx):
    await bot.change_presence(activity=discord.Game(name="Call of Duty®: Modern Warfare®"))
    await ctx.message.delete()

@bot.command(name='ract',help="Remove activity")
async def ract(ctx):
    await bot.change_presence(activity=discord.Game(name=""))
    await ctx.message.delete()

@bot.command(name='track',help="Get Ip Location")
async def track(ctx,*,msg:str):
    ip = getip(msg.lower().strip())
    await ctx.send(f"\nIP {ip[0]}\nStatus: {ip[1]}\nRegion: {ip[2]}\nCountry: {ip[3]}\nCity: {ip[4]}\nISP: {ip[5]}\nLat,Lon: {ip[6]}\nZipcode: {ip[7]}\nTimezone: {ip[8]}\nAs: {ip[9]}")
    await ctx.message.delete()

@bot.command(pass_context=True)
async def rainbow(ctx, lawl:int, mamacita:str):
    channel_id = ctx.message.channel.id
    channel = bot.get_channel(channel_id)
    rainbow = await ctx.send(embed=discord.Embed(title=mamacita, color=discord.Color.red()))
    sex = 0
    await ctx.message.delete()
    async for message in channel.history(limit=1):
        while lawl > sex:
            sex = sex + 1
            color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            await message.edit(embed=discord.Embed(title=mamacita, color=discord.Color(value=color)))
            await asyncio.sleep(1)

bot.run(Token,bot=False)
