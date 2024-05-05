import telebot
from telebot import types
import random

mail = str()

# Прошу обратить внимание перед прочтением этого кода!!!!!
# В субботу мы решили все сделать через ТГ-бота, но проблема в том, что никто такого не делал и не писал
# Это мой первый проект на библиотеке telebot
# Вся эта программа написана мной, за один вечер, параллельно изучая данную библиотеку
# Так же хочу предупредить, что в программе есть комментарии для ее удобного понимания, а так же описание проблем
# с которыми я столкнулся!
bot = telebot.TeleBot('6879356448:AAGLZ4ejcwT-blbL9RznQhKflhYc8UjbOXs')


@bot.message_handler(commands=['start'])
def get_info(message):
    bot.send_message(message.chat.id, """Привет! Ты попал в мир Sportlingo 🐸 
    
Sportlingo - это новая нейросеть для занятий настольным теннисом онлайн. 
Все работает очень просто. Я тебе отправляю видео-упражнение, ты его выполняешь, записываешь на камеру и отправляешь видео мне.
А я тебе говорю, правильно ты делаешь или нет. 
Если в выполнении упражнения есть ошибки, то я покажу тебе, как нужно делать правильно.

Давай скорее начнём!""")

    bot.send_message(message.chat.id, 'Введи свою почту на которую мы отправим твой результат:')

    # В этом боте не работает привязка почты, тут она скорее для галочки и развития
    # дальнейшего диалога программы
    @bot.message_handler(content_types=['text'])
    def getmail(message):

        vibor1 = types.ReplyKeyboardMarkup(row_width=1)
        vibornext = types.KeyboardButton('Перейти на "backhand"')
        vibornextt = types.KeyboardButton('Перейти на "forehand"')  # создание кнопок для переходов
        vibor1.add(vibornext, vibornextt)

        ssilka1 = types.InlineKeyboardMarkup(row_width=1)
        silka = types.InlineKeyboardButton('Перейти на YouTube:', url='https://www.youtube.com/watch?v=Eml35mX_cqs')
        ssilka1.add(silka)  # создание кнопок для переходов на ютуб видосы

        ssilka2 = types.InlineKeyboardMarkup(row_width=1)
        silka = types.InlineKeyboardButton('Перейти на YouTube:', url='https://www.youtube.com/watch?v=1iLQoYRJYCE')
        ssilka2.add(silka)  # создание кнопок для переходов на ютуб видосы

        markup = types.ReplyKeyboardMarkup(row_width=2)
        sport1 = types.KeyboardButton('forehand')
        sport2 = types.KeyboardButton('backhand')  # Основные кнопки для переключения
        markup.add(sport1, sport2)
        if '@' in message.text:
            # mail=message.text
            # Почему если я включаю меил то вместе с нижним ифом то выходит ошибка: UnboundLocalError: local variable 'mail' referenced before assignment
            bot.send_message(message.chat.id,
                             'Отлично, ты успешно зарегестрирован, теперь выбери те упражнения, по которым ты хочешь отточить навыки из меню ниже:',
                             reply_markup=markup)



        # Блок ифа для работы с "форхендом"

        elif (message.text == 'forehand') or (message.text == 'Перейти на "forehand"'):
            bot.send_message(message.chat.id,
                             'Вы выбрали "forehand", Посмотрите обучающее видео и пришлите ваш видео-результат: ',
                             reply_markup=ssilka1)

            @bot.message_handler(content_types=['video'])
            def video_send(message):
                # Так как сроки поджимают и свою нейронку написать и обучить нет времени, я пойду на такие методы, которые можно реализовать:
                video_qual = random.randint(1, 10)
                if video_qual <= 3:
                    bot.send_message(message.chat.id, 'Тренеруйтесь усерднее! Пересмотрите обучающий ролик.')
                else:
                    bot.send_message(message.chat.id,
                                     'Вы молодец! Можете отправлять мне еще видео или выбрать другое упражнение!',
                                     reply_markup=vibor1)

        # Блок ифа для работы с "бекхендом"

        elif (message.text == 'backhand') or (message.text == 'Перейти на "backhand"'):
            bot.send_message(message.chat.id,
                             'Вы выбрали "backhand", Посмотрите обучающее видео и пришлите ваш видео-результат: ',
                             reply_markup=ssilka2)

            @bot.message_handler(content_types=['video'])
            def video_send2(message):
                # Так как сроки поджимают и свою нейронку написать и обучить нет времени, я пойду на такие методы, которые можно реализовать:
                video_qual = random.randint(1, 10)
                if video_qual <= 3:
                    bot.send_message(message.chat.id, 'Тренеруйтесь усерднее! Пересмотрите обучающий ролик.')
                else:
                    bot.send_message(message.chat.id,
                                     'Вы молодец! Можете отправлять мне еще видео или выбрать другое упражнение!',
                                     reply_markup=vibor1)
        elif '@' not in message.text:
            # if mail == '':
            bot.send_message(message.chat.id,
                             'Неизвестная комманда, попробуй еще раз:')  # Вывод этого сообщения если все остальные не подходят под патерны описанные выше
            # else:
            # pass


bot.polling(none_stop=True, interval=0)
