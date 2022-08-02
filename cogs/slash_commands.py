import disnake
from disnake.ext import commands
import random

class Slash_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#-------------------------Простой ответ-------------------------

    @commands.slash_command(name="hi", description="test")
    async def test_command(self, inter: disnake.CommandInteraction): 
        await inter.response.send_message("Привет", Ephemeral=True) #Это inter ответ на вызов слеш команды, если его не будет то действие (например бан) выполнится, но команда просто напишет "Ошибка взаимодействия", Ephemeral это скрыть ли сообщение (Видно только вам)

def setup(bot):
    bot.add_cog(Slash_commands(bot))
