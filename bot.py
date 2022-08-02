import disnake
from disnake.ext import commands
import os
from config import settings

class PersistentViewBot(commands.Bot):
    def __init__(self): 
        super().__init__(command_prefix=settings['prefix'], intents=disnake.Intents().all(), activity=disnake.Streaming(name="Название стрима", url="https://www.twitch.tv/username"), test_guilds=[123]) #вместо 123 вставить айди сервера на котором будут слеш команды, а еще вот сайт где показаны все активности --> https://stackoverflow.com/questions/59126137/how-to-change-activity-of-a-discord-py-bot
        self.persistent_views_added = False
    async def on_ready(self): 
        if not self.persistent_views_added:
     
            self.persistent_views_added = True
        print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nБот запущен\nName: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") #тут бот принтует в консоль при запуске, можно написать что угодно

bot = PersistentViewBot()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs." + filename[:-3])

@bot.remove_command("help") #это удаляет стандартную и не красивую команду help
        
@bot.slash_command(description='Загрузить модуль бота') #эта команда отвечает за загрузку когов
@commands.is_owner()
async def load(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.load_extension(f"cogs.{module}")
    await inter.response.send_message(f"Загружен модуль `{module}`",ephemeral=True)

@bot.slash_command(description='Выгрузить модуль бота') #эта команда отвечает за выгрузку когов (отключение)
@commands.is_owner()
async def unload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.unload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Выгружен модуль `{module}`",ephemeral=True)
    
@bot.slash_command(description="Перезагрузить модуль бота") #эта команда отвечает за перезагрузку когов (т.е не обязательно перезагружать бота, можно перезагрузить сам ког)
@commands.is_owner()
async def reload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.reload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Перезагружен модуль `{module}`",ephemeral=True)

bot.run(settings['token'])
