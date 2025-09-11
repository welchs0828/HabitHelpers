import os, datetime as dt
import discord
from discord.ext import commands, tasks
from packages.storage.repo import HabitRepo

bot = commands.Bot(command_prefix="!")
repo = HabitRepo.default()

@bot.command()
async def done(ctx, *, habit_name: str):
    h = repo.get_by_name(habit_name)
    repo.add_completion(h.id, dt.date.today(), "discord", note=f"user:{ctx.author.id}")
    await ctx.reply(f"✓ Logged {habit_name} for today.")

@tasks.loop(hours=24)
async def daily_reminders():
    # iterate user profiles, respect timezone and quiet hours
    pass

bot.run(os.environ["DISCORD_TOKEN"])