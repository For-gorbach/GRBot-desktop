# -------=импорт нужных библиотек и файлов=-------
from pyrogram import Client, filters  # библиотека для работы с юзерботом
from time import sleep  # библиотека для создания задержки
import eel  # библиотека для создания веб интерфейса

@eel.expose  # подключаем функцию к модулю eel
def text(text, chats, time, api_id, api_hash):  # функция
    groups_id = chats.split(' ')  # удаляем из строки chats пробелы, после чего превращаем её в список
    groups_id = "\n".join(groups_id)
    groups_id = groups_id.split('\n')  #

    def removeel(lst, el):  # функция по удалению лишних элементов из списка
        els=0  # создаем переменную которая равна 0
        for i in range(len(lst)):  # цикл по количеству элементов в списке lst (если в lst 5 элементов цикл выполнится 5 раз)
            ele = lst[i]  # ele ровно элементу из списка lst по индексу i (например если список ["1", "2", "3"] а i = 1 то ele равно "2" {в списках счет начинается с 0 а не 1})
            if ele == el:  # если ele = el то...
                els+=1  # прибавляем 1 к els
        for i in range(els):  # повторяем цикл столько раз сколько означает els (например если els = 1 то цикл работает 1 раз)
            lst.remove(el)  # удаляем элемент
        return lst  # возвращаем новый список

    groups_id = removeel(groups_id, "")  # вызываем функцию по удалению лишних элементов

    app = Client("my_account", api_id=api_id, api_hash=api_hash)  # записываем в переменную app то что юзербот будет выполнять все действия от имени юзера, а так же передаем api_id и api_hash которые мы объявили в файле settings.py


    # -------=работа с юзерботом=-------
    with app:  # выполнение действий с помощью юзербота
        while True:  # вечный цикл

            for id in groups_id:  # берет id групп из их списка, который прописан в файле settings.py
                print(groups_id)

                try:  # код внутри try будет проверяться на ошибки
                    app.send_message(id, text)  # отправляет сообщение (msg) в нужный чат по id
                    sleep(1)  # задержка
                except Exception as ex:  # если будет ошибка обрабатываем её и вписываем в переменную ex
                    print(ex)  # выводим ошибку

            sleep(float(time))  # задержка отправки сообщения в час (в переменной zdr 3600 сек - 1 час)

# инфу ниже лень комментить 🤡, и она не так важна
eel.init("web")
eel.start("index.html", size=(1000, 800))
