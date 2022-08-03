import disnake
from disnake.ext import commands
from datetime import datetime

#Все права
add_reactions #Ставить реакции
administrator #Администратор
attach_files #Прикреплять файлы
ban_members #Банить участников
change_nickname #Изменение никнейма
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
manage_events #Управлять ивент               
manage_guild
manage_messages
manage_nicknames
manage_permissions
manage_roles
manage_threads
manage_webhooks
mention_everyone
moderate_members
move_members
mute_members
priority_speaker
read_message_history
read_messages
request_to_speak
send_messages
send_messages_in_threads
send_tts_messages
speak
start_embedded_activities
stream
use_external_emojis
use_external_stickers
use_slash_commands
use_voice_activation
view_audit_log
view_channel
view_guild_insights

class Permissions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Наличие роли у участника")
    @commands.has_role("name") or @commands.has_role(id) #Позволяет выполнить команду если у человека есть заданная вами роль, название в кавычках либо айди без кавычек
    async def user_has_role(self, ctx):
        
    @commands.command(name="Наличие ролей у участника")
    @commands.has_any_role("one","two","three") or @commands.bot_has_role(id1, id2, id3) #Позволяет выполнить команду если у человека есть одна из есть заданныъ вами ролей, названия в кавычках либо айди без кавычек
    async def user_has_any_role(self, ctx):
      
    @commands.command(name="Наличие роли у бота")
    @commands.bot_has_role("name") or @commands.bot_has_role(id) #Позволяет выполнить команду если у бота есть заданная вами роль, название в кавычках либо айди без кавычек
    async def bot_has_role(self, ctx):
        
    @commands.command(name="Наличие ролей у бота")
    @commands.bot_has_any_role("one","two","three") or @commands.bot_has_any_role(id1, id2, id3) #Позволяет выполнить команду если у бота есть заданная вами роль, название в кавычках либо айди без кавычек
    async def bot_has_any_role(self, ctx):
        
    @commands.command(name="Наличие права у участника")
    @commands.has_permissions(add_reactions=True, kick_members=True) #И так сколько угодно прав через запятую, я привёл пример, весь список прав в начале кога
    async def bot_has_any_role(self, ctx):
        
def setup(bot):
    bot.add_cog(Permissions(bot))
