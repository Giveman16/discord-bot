import discord
from discord.ext import commands
from datetime import datetime
import random

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

@bot.command('info')
async def command_info(ctx: commands.Context):
    await ctx.send('Я демонстрационный бот!')

@bot.command('weather')
async def command_weather(ctx: commands.Context):
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

@bot.command('picture')
async def command_picture(ctx: commands.Context):
    images = ['picture1.jpg', 'picture2.jpg', 'picture3.jpg']
    weights = [0.6, 0.3, 0.1] 
    image_name = random.choices(images, weights=weights, k=1)[0]
    with open('images/' + image_name, 'rb') as file:
        image = discord.File(file)
    await ctx.send('Лови Картинку!', file=image)

bot.run('token')
