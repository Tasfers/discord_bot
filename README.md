<div align="center">
 <h1 align="center">  Discord bot </h1>
 <strong>Шаблон дискорд бота на языке Python и на библиотеке Disnake</strong><br />Для корректной работы бота советую установить Python 3.9 и выше<br /><br/>
 </div>
 
## Начало работы
### Установка Python
1. Тыкаем [сюда](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe) и у вас скачивается Python 3.9

2. **Обязательно** включаем галочку рядом с *Add Python 3.9 to PATH* и проходим дальнейшую установку

После установки Python вы так же можете установить **Visual Studio Code** для редактирования файлов бота по этой [ссылке](https://code.visualstudio.com/Download)

### Работа с ботом
#### Создание нового бота на сайте [Discord Developers Portal](https://discord.com/developers/applications)

1. Заходим на [сайт](https://discord.com/developers/applications) и нажимаем на кнопку **New Application**
2. Вводим название приложения и нажимаем **Create**
3. Выбираем вкладку **Bot**
4. Нажимаем **Add Bot**
5. И снова нажимаем **Yes, do it!**
6. Нажимаем **Reset Token** и сохраняем его где-нибудь

#### Корневой файл **bot.py**
##### 1. Персонализация бота
###### Существует 4 статуса бота
 Онлайн - online
 
 Оффлайн - offline
 
 Не беспокоить - dnd
 
 Не активен - idle

Что бы задать боту свой статус требуется вставить в строку
```py
status=disnake.Status.idle
```
Вместо **idle** любой статус из [списка](https://github.com/Towa1015/discord_bot#существует-4-статуса-бота) выше
