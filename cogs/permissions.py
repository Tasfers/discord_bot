import disnake
from disnake.ext import commands
from datetime import datetime

#Все права
add_reactions #Добавлять реакции
administrator #Администратор
attach_files #Прикреплять файлы
ban_members #Банить участников
change_nickname #Изменеить никнейм
connect #Подключаться к голосовым каналам
create_instant_invite #Создание мгновенного приглашения
create_private_threads #Создавать приватные ветки
create_public_threads #Создавать публичные ветки
deafen_members #Выключить звук у участников
embed_links #Встраивать ссылки в эмбед
external_emojis #Сторонние эмодзи
external_stickers #Сторонние стикеры
kick_members #Выгонять участников
manage_channels #Управлять каналами
manage_emojis #Управлять эмодзи
manage_emojis_and_stickers #Управлять эмодзи и стикерами
manage_events #Управлять ивентами (Событиями)
manage_guild #Управлять сервером
manage_messages #Удалять сообщения
manage_nicknames #Изменять никнеймы участникам
manage_permissions #Управлять правами
manage_roles #Управлять ролями
manage_threads #Управлять ветками
manage_webhooks #Управлять вебхуками
mention_everyone #Упоминать все роли (everyone, here и все другие)
moderate_members #Вроде как тайм-аут (Мут)
move_members #Перемещать участников в другие голосовые каналы
mute_members #Отключать микрофон у участников
priority_speaker #Приоритетный режим
read_message_history #Читать историю сообщений
request_to_speak #Поднять руку в требунах
send_messages #Отправлять сообщения
send_messages_in_threads #Отправлять сообщения в ветках
send_tts_messages #Отправлять tts сообщения
speak #Говорить в голосовом канале
start_embedded_activities #Вроде как запускать активности в войсе
stream #Включать стрим
use_external_emojis #Это вроде то же что и на строке 17
use_external_stickers #Это вроде то же что и на строке 18
use_slash_commands #Использовать слеш команды
use_voice_activation #Использовать активацию по голосу в голосовом канале
view_audit_log #Просматривать журнал аудита
view_channel #Просматривать канал
view_guild_insights #Просматривать информацию о сервере

class Permissions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Наличие_роли_у_участника")
    @commands.has_role("name") or @commands.has_role(id) #Позволяет выполнить команду если у человека есть заданная вами роль, название в кавычках либо айди без кавычек (Можно и то и то сразу)
    async def user_has_role(self, ctx):
        await ctx.send("Права есть!")
        
    @commands.command(name="Наличие_ролей_у_участника")
    @commands.has_any_role("one","two","three") or @commands.bot_has_role(id1, id2, id3) #Позволяет выполнить команду если у человека есть одна из есть заданныъ вами ролей, названия в кавычках либо айди без кавычек (Можно и то и то сразу)
    async def user_has_any_role(self, ctx):
        await ctx.send("Права есть!")
      
    @commands.command(name="Наличие_роли_у_бота")
    @commands.bot_has_role("name") or @commands.bot_has_role(id) #Позволяет выполнить команду если у бота есть заданная вами роль, название в кавычках либо айди без кавычек (Можно и то и то сразу)
    async def bot_has_role(self, ctx):
        await ctx.send("Права есть!")
        
    @commands.command(name="Наличие_ролей_у_бота")
    @commands.bot_has_any_role("one","two","three") or @commands.bot_has_any_role(id1, id2, id3) #Позволяет выполнить команду если у бота есть заданная вами роль, название в кавычках либо айди без кавычек (Можно и то и то сразу)
    async def bot_has_any_role(self, ctx):
        await ctx.send("Права есть!")
        
    @commands.command(name="Наличие_прав_у_участника")
    @commands.has_permissions(add_reactions=True, kick_members=True) #И так сколько угодно прав через запятую, я привёл пример, весь список прав в начале кога
    async def has_permissions(self, ctx):
        await ctx.send("Права есть!")
        
    @commands.command(name="Наличие_прав_у_бота")
    @commands.bot_has_permissions(add_reactions=True, kick_members=True) #А это уже права у бота
    async def bot_has_permissions(self, ctx):
        await ctx.send("Права есть!")
        
def setup(bot):
    bot.add_cog(Permissions(bot))
