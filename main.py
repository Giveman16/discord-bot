import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/') 

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send('Я демонстрационный бот!')

@bot.command('weather')
async def command_weather(ctx:commands.Context):
    await ctx.send('Погода сегодня класс.')


@bot.command('greet')
async def command_greet(ctx: commands.Context):
    user_name = ctx.message.author.name
    await ctx.send(f'Привет, {user_name}!')


@bot.command('time')
async def command_time(ctx: commands.Context):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'Текущее время: {current_time}')


@bot.command('calculate')
async def command_calculate(ctx: commands.Context, *, expression: str):
    try:
        result = eval(expression)  
        await ctx.send(f'Результат: {result}')
    except Exception as e:
        await ctx.send(f'Ошибка: {str(e)}')

bot.run('token')
