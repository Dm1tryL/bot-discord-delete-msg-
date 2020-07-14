import discord
import time
from discord.ext import commands

TOKEN = 'NzMyNjEyMDAxNzE2NzY0NzEz.Xw3Nvg.MOed3-RyijwExCJ1MTx_XMhycyU'
bot = commands.Bot(command_prefix='!')
bad_words = [ 'хуй' , '_play']


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

@bot.event
async def on_message( message ):
    await bot.process_commands( message )	

    if message.content in bad_words:
    	time.sleep(600)
    	await message.delete()

bot.run(TOKEN)
