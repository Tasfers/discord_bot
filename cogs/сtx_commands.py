import disnake
from disnake.ext import commands
import random

class Ctx_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#-------------------------Повторялка-------------------------

    @commands.command(name="say", aliases=["s"]) #aliases позволяет добавить команды на которые бот будет так же отзываться
    async def say_command(self, ctx, arg): #arg можно заменить на что угодно, это ваш собственный параметр
        await ctx.send(f"{arg}") #f перед кавычками позволяют добавлять аргументы в фигурных {} скобках

#-------------------------Рандомайзер-------------------------

    @commands.command(name="random", aliases=["rand", "r"])
    async def rand_command(self, ctx, min, max):
        randomaizer = random.randint(int(min),int(max))
        await ctx.send(f"Ваше число: {randomaizer}")

def setup(bot):
    bot.add_cog(Ctx_commands(bot))
