# Для работы бота необходимо: 1. Установить все используемые библиотеки 2. Добавить ID группы(17стр)
#                             3. Добавить токен группы (18стр) 4. Добавить токин приложения (278)

# - Библиотеки для Вк БОтаа -
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

#  Библиотеки для Яндекс Диска
import requests
import yadisk
import datetime



# Переменные

group_id = ''       # ID группы
secret = ''  # Мой токен группы



# Для удобства

bot_token = secret
bot_group_id = group_id
vk = Bot(bot_token, bot_group_id)


tokenYa = ["У тебя не добавлен токен☹️"]  #  Здесь хранится токен яндекс диска
saveTok = [1]


@vk.on.private_message(text=['Начать', 'Ку', 'Привет'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Приветик!\nСкорее пиши Меню, что бы открыть клавиатуру')




# Меню
@vk.on.private_message(text=['Меню', 'menu', 'меню', "🔙Меню🔙", "🔚Меню🔚"])

async def menu(message: Message):
    await message.answer(
        # Сообщение при отправлении клавиатуры
        message='Весь функционал: ',
        # Клавиатура
        keyboard=(
            # one_time - True - одноразовая клавиатура, False - постоянная клавиатура
            # inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
            # .add - добавить кнопку
            # .row - отступ
            # Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
            # PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time=False, inline=False)
                .add(Text('📩Сохранить фото📩'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('✅Добавить ТОКЕН✅'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('🧐Какой токен используется🧐'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('❔Как получить ТОКЕН❔'))
                .row()
                .add(Text('📚Что я умею📚'), color=KeyboardButtonColor.PRIMARY)
        )
    )

    if message.text == "🔙Меню🔙":
        saveTok.pop(-1)
        print(saveTok)

    elif message.text == "🔚Меню🔚":
        for_id.pop(-1)
        print(for_id)


        # КНОПКА:   📩Сохранить фото📩
@vk.on.private_message(text="📩Сохранить фото📩")
async def menu(message: Message):
    await message.answer(
        message='Если страница пользователя закрыта, то это будет не возможно☹️\nОткуда схронять фото?',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Профиль'), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text('Со стены'), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text('Сохранёнки'), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Меню"), color=KeyboardButtonColor.NEGATIVE)
        )
    )





                    #   Функция сохраниения фото с профиля

id_pro = []
for_id = [1]
photos = []


@vk.on.private_message(text="Профиль")
async def menu(message: Message):
    await message.answer(
        message='Введи ID: ',
        keyboard=(Keyboard(one_time=False, inline=False)
                  .add(Text("🔚Меню🔚"), color=KeyboardButtonColor.NEGATIVE)))

    for_id.append("ID")
    photos.append("Профиль")




                    #   Функция сохраниения фото из Альбома
@vk.on.private_message(text="Со стены")
async def menu(message: Message):
    await message.answer(
        message='Введи ID: ',
        keyboard=(Keyboard(one_time=False, inline=False)
                  .add(Text("🔚Меню🔚"), color=KeyboardButtonColor.NEGATIVE)))

    for_id.append("ID")
    photos.append("Со стены")


                    #   Функция сохраниения фото из Сохранёнок
@vk.on.private_message(text="Сохранёнки")
async def menu(message: Message):
    await message.answer(
        message='Эта функция возможна если только у пользователя открыты сохранёнки\nВведи ID: ',
        keyboard=(Keyboard(one_time=False, inline=False)
                  .add(Text("🔚Меню🔚"), color=KeyboardButtonColor.NEGATIVE)))

    for_id.append("ID")
    photos.append("Сохранёнки")



                            # КНОПКА:   🧐Какой токен используется🧐

@vk.on.private_message(text='🧐Какой токен используется🧐')
async def tok(message: Message):
    await message.answer(
        message=f'Твой токен:\n {tokenYa[-1]}')




                             # КНОПКА:   ✅Добавить ТОКЕН✅

@vk.on.private_message(text='✅Добавить ТОКЕН✅')
async def tok(message: Message):
    await message.answer(
        message='Напиши мне свой токен📝',
        keyboard=(Keyboard(one_time=False, inline=False)
                  .add(Text("🔙Меню🔙"), color=KeyboardButtonColor.NEGATIVE)))


    saveTok.append("сохр")
    print(saveTok)



                      # КНОПКА:   ❔Как получить ТОКЕН❔

photo_token = "photo-212331614_457239018"      # Фото сайта
photo_token1 = "photo-212331614_457239019"

@vk.on.private_message(text='❔Как получить ТОКЕН❔')
async def blasthk(message: Message):
    await message.answer(
        message='Нужно перейти по ссылке и войти в аккаунт: https://yandex.ru/dev/disk/poligon/\n\n Далее нажать: \nПолучить OAuth-токен', attachment= photo_token)

    await message.answer(
        message='Копируем его и добавляем в Бота', attachment= photo_token1 )




                         # КНОПКА:   📚Что я умею📚

@vk.on.private_message(text='📚Что я умею📚')
async def help(message: Message):
    await message.answer(
        message='Я сохраняю фото с профиля пользователя по его ID тебе на Яндекс.Диск\nНо если страница пользователя закрыта, то это будет не возможно☹️')




                            # Если неизвестная команда

@vk.on.private_message()
async def main(message):
                                #  Функция добавление токена
    if saveTok[-1] == "сохр":
        await message.answer(
            'Токен добавлен ✅', keyboard=(Keyboard(one_time=False, inline=False)
            .add(Text('📩Сохранить фото📩'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('✅Добавить ТОКЕН✅'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('🧐Какой токен используется🧐'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('❔Как получить ТОКЕН❔'))
            .row()
            .add(Text('📚Что я умею📚'), color=KeyboardButtonColor.PRIMARY)
    ) )

        tok = message.text
        tokenYa.append(tok)  # Добавление токена

        saveTok.pop(-1)

                                #   Добавление ID пользователя
    elif for_id[-1] == "ID":
        if len(tokenYa) < 1:  # Если нет токена
            await message.answer(
                'У вас не добавлен токен Яндекс.Диска☹️', keyboard=(Keyboard(one_time=False, inline=False)
                .add(Text('📩Сохранить фото📩'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('✅Добавить ТОКЕН✅'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('🧐Какой токен используется🧐'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('❔Как получить ТОКЕН❔'))
                .row()
                .add(Text('📚Что я умею📚'), color=KeyboardButtonColor.PRIMARY)
    ))
            for_id.pop(-1)

        else:
            await message.answer(
                "Проверьте свой Яндекс.Диск\nЕсли ничего не загрузилось проверьте данные", keyboard=(Keyboard(one_time=False, inline=False)
                .add(Text('📩Сохранить фото📩'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('✅Добавить ТОКЕН✅'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('🧐Какой токен используется🧐'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('❔Как получить ТОКЕН❔'))
                .row()
                .add(Text('📚Что я умею📚'), color=KeyboardButtonColor.PRIMARY)
                ))

            for_id.pop(-1)

            id_man = message.text
            id_pro.append(id_man)   # Сохранение ID

            photo_profil()


                            # Если нет команды
    else:
        await message.answer(
            'К сожалению я не знаю такой команды☹️', keyboard=(Keyboard(one_time=False, inline=False)
          .add(Text('📩Сохранить фото📩'), color=KeyboardButtonColor.POSITIVE)
          .add(Text('✅Добавить ТОКЕН✅'), color=KeyboardButtonColor.POSITIVE)
          .row()
          .add(Text('🧐Какой токен используется🧐'), color=KeyboardButtonColor.POSITIVE)
          .row()
          .add(Text('❔Как получить ТОКЕН❔'))
          .row()
          .add(Text('📚Что я умею📚'), color=KeyboardButtonColor.PRIMARY)
          ))




                            # Функция сохранения фото профиля

def photo_profil():

    global params
    pril_tok = ""        # Токен приложения Вк

    URL = "https://api.vk.com/method/photos.get"

    if photos[-1] == "Профиль":
        params = {
            "user_ids": "1",
            "access_token": pril_tok,
            "v": "5.131",
            "owner_id": id_pro[-1],
            "album_id": "profile",
            "count": "100",
            "extended": "1"
        }
    elif photos[-1] == "Со стены":
        params = {
            "user_ids": "1",
            "access_token": pril_tok,
            "v": "5.131",
            "owner_id": id_pro[-1],
            "album_id": "wall",
            "count": "100",
            "extended": "1"
        }

    elif photos[-1] == "Сохранёнки":
        params = {
            "user_ids": "1",
            "access_token": pril_tok,
            "v": "5.131",
            "owner_id": id_pro[-1],
            "album_id": "saved",
            "count": "100",
            "extended": "1"
        }

    res = requests.get(URL, params=params).json()

    res1 = res['response']['items']

    name = []
    name.append([str(photo["likes"]['count']) for photo in res1]) # из всего списка берём количество лайков с фото


    size = []
    size.append([str(url["sizes"][-1]["type"]) for url in res1]) # из всего списка берём максимальный размер

    url_photo = []
    url_photo.append([str(url["sizes"][-1]["url"]) for url in res1]) # из всего списка берём URL фото


    y = yadisk.YaDisk(token=tokenYa[-1])
    name_folder = datetime.datetime.now().strftime("%d-%m-%Y \n%H.%M.%S")  # Имя для папки сегодняшняя дата
    y.mkdir(name_folder)  # Создание папки


    i = 0
    while i < len(name[0]):
        print(f"\n\nЗАГРУЖЕНО ФОТО {i+1}/{len(name[-1])}\nИмя фотографии: {name[-1][i]} \nРазмер фотографии: {size[-1][i]} \nСсылка на фото: {url_photo[-1][i]}")
        y.upload_url({url_photo[0][i]}, f"{name_folder}/{name[-1][i]}.jpg")  # Загрузка фото

        i += 1




vk.run_forever()
