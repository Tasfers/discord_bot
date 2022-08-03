import disnake
from disnake.ext import commands
from datetime import datetime

class Embed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed") #Пример эмбеда, переменную эмбеда можно заменить на любую другую
    async def embed_command(self, ctx):
        embed = disnake.Embed(title="Title", description="Description", color=0x2F3136, timestamp=datetime.now()) #Название, описание, HEX код цвета, время отправки
        embed.set_author(name="Author", icon_url="image url here") #Жирное поле сверху с маленькой круглой картинкой
        embed.add_field(name="Field 1", value="Not inline", inline=False)
        embed.add_field(name="Field 2", value="Inline 1", inline=True)
        embed.add_field(name="Field 3", value="Inline 2", inline=True)
        embed.set_footer(text="Footer", icon_url="image url here") #Маленькое поле снизу с маленькой круглой картинкой
        embed.set_image(url="image url here") #Большая картинка снизу
        embed.set_thumbnail(url="image url here") #Средняя картинка справа сверху
        await ctx.send(embed=embed) #Отправка эмбеда

def setup(bot):
    bot.add_cog(Embed(bot))
