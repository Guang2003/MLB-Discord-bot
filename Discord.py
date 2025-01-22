import discord
import datetime
import Crawling
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

reminder_list = set()  # 用於儲存用戶的名單

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game("MLB 9innings 2025")
    await client.change_presence(status=discord.Status.online, activity=game)
    if not reset_reminder_list.is_running():  # 確保不會重複啟動
        reset_reminder_list.start()
        print("提醒名單重置任務已啟動！")

@client.command()
async def remind(ctx):
    if reminder_list:
        members = ', '.join([f'<@{user_id}>' for user_id in reminder_list])
        await ctx.send(f"提醒: {members}記得預測、俱樂部戰、俱樂部挑戰")
    else:
        await ctx.send("目前沒有任何人需要提醒。")

@client.command()
async def join_reminder(ctx):
    user_id = ctx.author.id
    if user_id not in reminder_list:
        reminder_list.add(user_id)
        await ctx.send(f"<@{user_id}> 已成功加入提醒名單！")
    else:
        await ctx.send(f"<@{user_id}> 已經在提醒名單中！")

@client.command()
async def leave_reminder(ctx):
    user_id = ctx.author.id
    if user_id in reminder_list:
        reminder_list.remove(user_id)
        await ctx.send(f"<@{user_id}> 已成功從提醒名單中移除！")
    else:
        await ctx.send(f"<@{user_id}> 你不在提醒名單中！")

@tasks.loop(hours=24)
async def reset_reminder_list():
    reminder_list.clear()
    reminder_list.add(780404594991038494)
    reminder_list.add(844743434576330772)
    reminder_list.add(844740783466086471)
    reminder_list.add(747058166369353749)
    print("提醒名單已重置！")

@reset_reminder_list.before_loop
async def before_reset_reminder_list():
    now = datetime.datetime.now()
    next_reset = now.replace(hour=17, minute=42, second=0, microsecond=0)
    if now >= next_reset:
        next_reset += datetime.timedelta(days=1)
    await discord.utils.sleep_until(next_reset)

@client.command()
async def hstat(ctx, *player):
    """查詢指定打者今年數據"""
    try:
        # 將所有參數合併為一個完整的人名
        player_name = " ".join(player)
        hitter_info = Crawling.get_hitter_stat(player_name)
        await ctx.send(hitter_info)
    except Exception as e:
        await ctx.send(f"獲取指定打者時出錯：{str(e)}")

@client.command()
async def pstat(ctx, *player):
    """查詢指定投手今年數據"""
    try:
        # 將所有參數合併為一個完整的人名
        player_name = " ".join(player)
        pitcher_info = Crawling.get_pitcher_stat(player_name)
        await ctx.send(pitcher_info)
    except Exception as e:
        await ctx.send(f"獲取指定投手時出錯：{str(e)}")

file = open("token.txt", "r")
token = file.read()
client.run(token)
