<div align="center">
 <h1 align="center">  Discord bot </h1>
 <strong>Гайд по написанию дискорд бота на языке Python и на библиотеке Disnake</strong><br />Для корректной работы бота советую установить Python 3.9 и выше<br /><br/>
 </div>
 
## Начало работы
### Установка Python
1. Тыкаем [сюда](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe) и у вас скачивается Python 3.9

2. **Обязательно** включаем галочку рядом с *Add Python 3.9 to PATH* и проходим дальнейшую установку

После установки **Python** вы так же можете установить **Visual Studio Code** для редактирования файлов бота по этой [ссылке](https://code.visualstudio.com/Download)

### Работа с ботом
#### Создание нового бота на сайте [Discord Developers Portal](https://discord.com/developers/applications)

1. Заходим на [сайт](https://discord.com/developers/applications) и нажимаем на кнопку `New Application`
2. Вводим название приложения и нажимаем `Create`
3. Выбираем вкладку `Bot`
4. Нажимаем `Add Bot`
5. И снова нажимаем `Yes, do it!`
6. Нажимаем `Reset Token` и сохраняем его где-нибудь

#### Настройка интентов (для слеш команд)

Во вкладке `Bot` включаем следующие галочки
1. `Public Bot` (не обязательно)
2. `Presence Intent`
3. `Server Members Intent`
4. `Message Content Intent`

#### Установка зависимости
`pip install disnake` - а вот и сам disnake

#### Корневой файл `bot.py`
##### Настройка бота под себя
###### Статусы
 ```py
 Онлайн
 status=disnake.Status.online

 Оффлайн
 status=disnake.Status.offline

 Не беспокоить
 status=disnake.Status.dnd

 Не активен
 status=disnake.Status.idle
 ```

###### Активности
 ```py
 Играет
 activity=disnake.Game(name="игру")
 
 Смотрит
 activity=disnake.Activity(type=disnake.ActivityType.watching, name="ютуб")
 
 Слушает
 activity=disnake.Activity(type=disnake.ActivityType.listening, name="музыку")
 
 Стримит
 activity=disnake.Streaming(name="стрим", url="https://www.twitch.tv/никнейм") #если убрать аргумент url то кнопки просто не будет, но все будет работать
 
 Соревнуется в
 activity=disnake.Activity(type=disnake.ActivityType.competing, name="игре")
 ```

###### Test Guilds
 Этот термин обозначает принудительное включение слеш команд на определённых серверах
 
 Что бы добавить туда свой сервер напишите так
 ```py
 test_guilds=[960169222808432660]
 ```
 
 Что бы добавить несколько серверов напишите так
 ```py
 test_guilds=[960169222808432660, 941767647790514216]
 ```
 **Важно** - Если айди вашего сервера не будет там то слеш команда появится/обновится только через час после её добавления/изменения
 
 ### Создание кога
 Создаем файл `<название на английском>.py` в папке `cogs`, пример - `moderation.py`
 #### Начинка кога (Вместо Fun ставим название своего кога)
 ```py
 import disnake
 from disnake.ext import commands

 class Fun(commands.Cog):

     def __init__(self, bot):
         self.bot = bot

     @commands.Cog.listener()
     async def on_ready(self): #ивент который будет активироваться когда вы включите бота
         print('Любой текст, к примеру: Cog Fun - Ready')

     Тут будут команды и ивенты

 def setup(bot):
     bot.add_cog(Fun(bot))
 ```
 
 ### Термины
 Ког - модуль бота где хранятся команды, можно создать несколько когов (Модерация, Развлечение и.т.п)
 
 Токен - код с помощью которого код с ботом подключается к дискорду
 
 Импорт - обязательная вещь которая добавляет в код много полезного, пример ниже
 
 ```py
 import disnake
 from disnake.ext import commands
 ```
 Ивент - триггер который активируется при каком либо действии, к примеру on_ready - бот включен(готов)
 
 *На этом все, дальше смотрите файлы, там я буду выкладывать примеры*
