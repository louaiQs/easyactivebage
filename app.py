import discord
from discord.ext import commands
from discord import app_commands
import datetime

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

last_check_time = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="check", description="Shows days since last execution and Active Developer link")
async def check(interaction: discord.Interaction):
    global last_check_time
    current_time = datetime.datetime.now()
    
    response_message = ""
    
    if last_check_time is None:
        response_message = "This is the first time the command has been executed.\n"
    else:
        days_since = (current_time - last_check_time).days
        response_message = f"Days since last execution: {days_since}\n"
    
    response_message += "Active Developer Portal: https://discord.com/developers/active-developer"
    
    await interaction.response.send_message(response_message)
    last_check_time = current_time
bot.run('yourbottoken')
