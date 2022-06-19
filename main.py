# -------=импорт нужных библиотек и файлов=-------
from pyrogram import Client, filters  # библиотека для работы с юзерботом
from time import sleep  # библиотека для создания задержки
import eel  # библиотека для создания веб интерфейса
import asyncio  # библиотека для асинхронности

@eel.expose  # подключаем функцию к модулю eel
def text(text, chats, api_id, api_hash):  # функция
    groups_id = eval("{"+chats+"}")  # превращаем переданную информацию в словарь (например если передан текст "100: 30" то мы добавляем скобки и получаем "{100: 30}" а при помощи eval ``убираем`` ковычки превращая текст в словарь

    app = Client("my_account", api_id=api_id, api_hash=api_hash)  # записываем в переменную app то что юзербот будет выполнять все действия от имени юзера, а так же передаем api_id и api_hash которые мы объявили в файле settings.py

    async def send(app, id, time):  # функция отправки в которую передаем app (юзера), айди и время
        while True:  # вечный цикл
            await app.send_message(id, text)  # отправляем сообщение
            await asyncio.sleep(time)  # "усыпляем" данный цикл

    async def main():  # асинхронная функция
        async with app:  # начинаем работу с юзером
            await asyncio.gather(*[send(app, id, time) for id, time in groups_id.items()])  # через цикл берем айди и время и передаем их в send вместе с юзером, asyncio.gather что бы это были независимые циклы

    asyncio.run(main())  # запускаем асинхронную функцию

eel.init("web")  # инициализируем проект в папке web
eel.start("index.html", size=(1000, 800))  # запускаем index.html в окне с размером 1000 на 800
