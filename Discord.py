import discord
import Crawling
import time
import datetime
from discord.ext import tasks, commands
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game("笑死")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "MLB":
        probable = Crawling.show_probable() 
        for i in range(len(probable)):
            await message.channel.send(probable[i])
            time.sleep(0.01)
            
class TaskTime(commands.Cog):
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 21, minute = 35, tzinfo = tz)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()

    @tasks.loop(seconds=60)
    async def everyday(self):
        now = datetime.datetime.now(self.tz)
        if now.hour == self.everyday_time.hour and now.minute == self.everyday_time.minute:
            print("hihihihi")
            channel_id = 1232217167311798296
            channel = self.bot.get_channel(channel_id)
            probable = Crawling.show_probable() 
            for i in range(len(probable)):
                await channel.send(probable[i])
        

async def setup(bot: commands.Bot):
    await bot.add_cog(TaskTime(bot))

file = open("token.txt","r")
token = file.read()
client.run(token)