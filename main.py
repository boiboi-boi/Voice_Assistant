import sys
from mywindow import *
from PyQt5 import QtCore, QtWidgets
import yadisk
from googletrans import Translator
import pyttsx3 as pyttsx3
import pyautogui as auto
import speech_recognition as sr
import re
import pyowm
import webbrowser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import datetime
import time
from translate import Translator
import os
import random

yandex_token = yadisk.YaDisk(token="AQAAAABUiD41AAcZLTVTB7vZ8EYdg2jgKYD5Aa8")
moood = ['дела','делишки', 'настроение']
excel = ['эксэль', 'эксель', 'excel', 'иксель', 'иксель']
cmd = ['cmd', 'командную', 'командная', 'строка']
msword = ['word', 'ворд']
paint = ['paint', 'пэйнт', 'пэинт', 'пайнт']
weather = ['погода','погоду', 'погоде','погодка','погодку','погодке', 'на улице', 'за окном']
help = ['ты можешь', 'ты умеешь', 'помощь', 'о себе', 'можешь сделать', 'команды']
times = ['текущее время', 'сейчас времени', 'который час', 'время']
stackoverflow = ['stackoverflow', 'стак оверфлоу', 'стакофверфлоу']
github = ['гит', 'гитхаб', 'github', 'git']
habr = ['хабр', 'habr']
java_test = ['джава', 'java', 'ява']
python_test = ['питон', 'пайтон', 'python']
cpp_test = ['си плюс плюс', 'плюс', 'си', 'c']
vk = ['вк', 'вконтакте', 'vk']
music = ['музыка', 'музыку', 'музыки', 'песню', 'песня', 'трек']
video = ['видео', 'видос', 'ролик', 'видеоролик']
pics = ['картинка', 'картинку', ' изображение', 'картинки', 'изображения']
python = ['пакет питон', 'питон пакет', 'пайтон пакет', 'пакет пайтон', 'python package', 'package python',
                  'пакет для пайтона', 'пакет для питона', 'пакет для python']
hello = ['привет', 'здравствуй', 'салют', 'добрый день', 'добрый вечер', 'доброе утро', 'здорово']
translate_alias = ['переведи', 'перевод']
exit = ['выход', 'выйти', 'закончи', 'закончить', 'заверши', 'завершить', 'прекратить']
test = ['тесты', 'тест', 'тестирование', 'тестики', 'тестик']
joke = ['шутка', 'шутку', 'шутки', 'анекдот', 'прикол', 'развесели', 'рассмеши', 'пошути']
things = ['Думаю, стоит сесть за незаконченный проект',
                  'Если вы уже долго время сидите за компьютером, сделайте гимнастику для глаз',
                  'Может прогуляться?', 'Почитайте новости, даже могу вам их рассказать',
                  'Не хотите встретиться с друзями? ']
jokes = [
            'Урок на дистанционке. Учитель: — Кто будет отвечать? Класс молчит. Учитель: — Лес рук, тогда пойдём по алфавиту, отвечать будет АngrуКittу2008',
            'На Василия, который двадцать лет живет в однокомнатной квартире с женой и тещей, комары уже не садятся.',
            '«Долбаный рис!» — обычно такой фразой заканчивается любая попытка приготовить суши дома.',
            'Мужики, меня в армию забирают. Как же так, у тебя же плоскостопие? Мне сказали: «За немцев будешь».',
            'Вечером жена говорит мужу: Милый, тебе рассказать как я покаталась на нашей новой машине или ты узнаешь завтра из газет?'
        ]

what_to_do = ['что делать', 'заняться', 'что можно поделать']
mood = ['Все отлично', 'У меня все супер!', 'Хорошо', 'Замечательно']
help_git = ['справочник', 'справка гит', 'справка по работе  git', 'справка по работе с гит', 'как работать',
            'как работает']
first = ['первый', 'первое', 'один']
second = ['второй', 'второе', 'два']
third = ['третий', 'третье', 'три']
fourth = ['четвертый', 'четвертое', 'четыре']
java_ask = ['Начнём с простого: что такое Java?',
                    'Что будет в результате выполнения операции 2 + 2 == 5 && 12 / 4 == 3 || 2 == 5 % 3?',
                    'Что такое класс в Java?',
                    'Какие варианты инициализации массива правильные?',
                    'Выберите верное утверждение',
                    'Как объявить класс в коде?',
                    'Для чего используется оператор NEW?',
                    'Что означает ключевое слово extends?',
                    'Что означает перегрузка метода в Java (overload)?',
                    'Чем отличаются static-метод класса от обычного метода класса?']
java_ans = [['1) Марка машины', '2) Язык программирования', '3) Сигареты', '4) Футбольная команда'],
                    ['1) true', '2) false', '3) 0', '4) null'],
                    [
                        '1) Уровень сложности программы. Все операторы делятся на классы в зависимости от сложности их использования',
                        '2) Базовый элемент объектно-ориентированного программирования в языке Java',
                        '3) Такое понятие есть только в C++, в Java такого понятия нет',
                        '4) Просто одно из возможных названий переменной.'],
                    ['1) int[] array = 1,2,3,4,5;', '2) int[] array = int[]', '3) int[] arr = int[]',
                     '4) int[] array = new int[]{1,2,3,4,5}'],
                    ['1) Абстрактный класс должен содержать хотя бы один абстрактный метод',
                     '2) Абстрактный класс может не содержать ни одного абстрактного метода',
                     '3) Абстрактный метод может иметь тело, а может не иметь',
                     '4) Методы в интерфейсе обязательно должны иметь тело'],
                    ['1) class MyClass {}', '2) new class MyClass {}', '3) select * from class MyClass {}',
                     '4) MyClass extends class {}'],
                    ['1) Для объявления нового класса', '2) Это антагонист оператора OLD',
                     '3) Для создания экземпляра класса', '4) Для создания новой переменной'],
                    ['1) Что это дополнительный модуль класса, который расширяет его свойства',
                     '2) Что два класса делают одно и то же',
                     '3) Что данный класс наследуется от другого',
                     '4) Что это самый большой класс в программе'],
                    ['1) Изменение поведения метода класса относительно дочернего',
                     '2) Несколько методов с одинаковым названием, но разным набором параметров',
                     '3) Несколько разных классов с одинаковым методом',
                     '4) Изменение поведения метода класса относительно родительского'],
                    ['1) Обычный метод класса можно переопределить, а static-метод нельзя',
                     '2) Обычный метод класса можно перегрузить, а static-метод нельзя',
                     '3) Static-метод класса можно вызывать только внутри класса, а обычный - в любой части кода',
                     '4) Обычный метод класса работает от объекта класса, а static-метод от всего класса']]

python_ask = ['Начнём с простого: что такое Python?',
                      'Сколько библиотек можно импортировать в один проект?',
                      'Какая функция выводит что-либо в консоль?',
                      'Имеется кортеж вида T = (4, 2, 3). '
                      'Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?',
                      'Необходимо собрать и вывести все уникальные слова из строки рекламного текста. '
                      'Какой из перечисленных типов данных Python подходит лучше всего?',
                      'Как вывести список методов и атрибутов объекта x?',
                      'Для чего в пакетах модулей python в файле __init__.py служит список __all__?',
                      'При объявлении класса с помощью оператора class что пишется в круглых скобках после имени класса?',
                      'Какую роль в описании метода класса выполняет декоратор @property?',
                      'Что выведет следующий код?\n '
                      'try\n:'
                      '   raise IndexError\n'
                      'except IndexError:\n'
                      '   print(\'Получено исключение.\')\n'
                      'else:\n'
                      '   print(\'Но в этом нет ничего страшного.\')\n'
                      ]

python_ans = [['1) Змея', '2) Язык программирования', '3) Модель самолета', '4) Баскетбольная команда'],
                      ['1) Неограниченное количество', '2) до 4', '3) до 10', '4) 0'],
                      ['1) write()',
                       '2) print()',
                       '3) out()',
                       '4) outPrint()'],
                      ['1) T.startswith(1)', '2) T[0] = 1', '3) T = (1) + T[1:]', '4) T = (1,) + T[1:]'],
                      ['1) словарь (dict)',
                       '2) множество (set)',
                       '3) список (list)',
                       '4) кортеж (tuple)'],
                      ['1) dir(x)', '2) info(x)', '3) help(x)', '4) ?x'],
                      ['1) Для перечисления файлов, которые будут скрыты для импортирования.',
                       '2) Для конструкторов классов, как и всё, что связано с __init__',
                       '3) Список определяет, что экспортировать, когда происходит импорт с помощью from * ',
                       '4) Для перечисления переменных, которые будут скрыты для импортирования.'],
                      ['1) Имена классов, порождаемых данным классом.',
                       '2) Имена принимаемых классом аргументов.',
                       '3) Имена суперклассов, если класс наследуется от одного или нескольких классов.',
                       '4) Имена аргументов, принимаемых методом __init__.'],
                      ['1) Декорированный метод становится методом класса: метод получает класс, а не экземпляр.',
                       '2) Значение, возвращаемое декорированным методом, вычисляется при извлечении. Можно обратиться к методу экземпляра, как к атрибуту.',
                       '3) Декорированный метод становится статическим, экземпляр не передаётся.',
                       '4) Декорированный метод становится статическим, а экземпляр передаётся.'],
                      ['1) None',
                       '2) TypeError',
                       '3) IndexError',
                       '4) Получено исключение.']]

cpp_ask = ['Начнём с простого: что такое C++?',
                   'Можно ли перегружать операции для встроенных типов данных?',
                   'Что такое полиморфизм?',
                   'Как указать комментарий?',
                   'Сколько параметров можно передать в деструктор?',
                   'Что выдаст код ниже?\n'
                   'char s[] = \"hello\", t[] = \"hello\";\n'
                   'if(s == t)\n'
                   '   cout << "True";',
                   'Дружественная функция - это',
                   'Можно ли перегружать операции для встроенных типов данных?',
                   'Что такое инкапсуляция?',
                   'Выберите правильное объявление производного класса:'
                   ]

cpp_ans = [['1) Вирус', '2) Язык программирования', '3) Модель ракеты', '4) Математическая операция'],
                   ['1) Нет', '2) Да', '3) Не знаю', '4) Не всегда'],
                   [
                       '1) Свойство языка программирования, позволяющее объединить и защитить данные и код в объектe и скрыть реализацию объекта от пользователя.',
                       '2) Возможность объектов с одинаковой спецификацией иметь различную реализацию',
                       '3) Такое понятие есть только в Java, в C++ такого понятия нет',
                       '4) Полиморфизм? Не знаю такого.'],
                   ['1) # комметарий', '2) / комментарий', '3) /* комметарий /*', '4) // комментарий'],
                   ['1) Не более 3',
                    '2) В него нельзя передавать параметры',
                    '3) 2',
                    '4) Не более 10'],
                   ['1) Ничего не выведет, так как идет сравнение указателей', '2) True', '3) False', '4) Ошибка'],
                   ['1) Функция, являющаяся членом класса и объявленная с атрибутом friend.',
                    '2) Функция другого класса, среди аргументов которой есть элементы данного класса.',
                    '3) Функция, объявленная в классе с атрибутом friend, но не являющаяся членом класса.',
                    '4) Функция, которая в другом классе объявлена как дружественная данному.'],
                   ['1) Да',
                    '2) Не знаю',
                    '3) Нет',
                    '4) Не всегда'],
                   ['1) Возможность объектов с одинаковой спецификацией иметь различную реализацию',
                    '2) Свойство языка программирования, позволяющее объединить и защитить данные и код в объектe и скрыть реализацию объекта от пользователя',
                    '3) Не знаю',
                    '4) То же самое, что и наследование'],
                   ['1) class MoreDetails:: Details;',
                    '2) class MoreDetails: public class Details;',
                    '3) class MoreDetails: class(Details);',
                    '4) class MoreDetails: public Details;']]

speak_engine = pyttsx3.init()

text = """
Вы можете попросить у меня:
• открыть популярные сайты: github, stackoverflow, habr или открыть любую другую страницу в интернете
• пройти тестирование и узнать свой уровень знаний по трем популярным языкам программирования
• открыть соц. сеть ВКонтакте
• включить музыку
• включить видео
• рассказать актуальные новости на день
• узнать о погоде
• показать справочник по работе с GitHub
• найти пакет для python
• узнать текущее время
• найти картинку в интернете 
• перевести текст с английского на русский
• открыть некоторые приложения: excel, cmd, word, paint 
• рассмешить Вас
• если нечего делать могу подкинуть пару мыслей или можем просто поболтать
"""


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def setMoveWindow(widget):
    """
    Позволяет перемещать окно ухватившись не только за заголовок, а за произвольный виджит (widget).
    """
    win = widget.window()
    cursorShape = widget.cursor().shape()
    moveSource = getattr(widget, "mouseMoveEvent")
    pressSource = getattr(widget, "mousePressEvent")
    releaseSource = getattr(widget, "mouseReleaseEvent")

    def move(event):
        if move.b_move:
            x = event.globalX() + move.x_korr - move.lastPoint.x()
            y = event.globalY() + move.y_korr - move.lastPoint.y()
            win.move(x, y)
            widget.setCursor(QtCore.Qt.SizeAllCursor)
        return moveSource(event)

    def press(event):
        if event.button() == QtCore.Qt.LeftButton:
            x_korr = win.frameGeometry().x() - win.geometry().x()
            y_korr = win.frameGeometry().y() - win.geometry().y()
            parent = widget
            while not parent == win:
                x_korr -= parent.x()
                y_korr -= parent.y()
                parent = parent.parent()
            move.__dict__.update({"lastPoint": event.pos(), "b_move": True, "x_korr": x_korr, "y_korr": y_korr})
        else:
            move.__dict__.update({"b_move": False})
            widget.setCursor(cursorShape)
        return pressSource(event)

    def release(event):
        move.__dict__.update({"b_move": False})
        widget.setCursor(cursorShape)
        return releaseSource(event)

    setattr(widget, "mouseMoveEvent", move)
    setattr(widget, "mousePressEvent", press)
    setattr(widget, "mouseReleaseEvent", release)
    move.__dict__.update({"b_move": False})
    return widget


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        qss_file = open('style_window.qss').read()
        self.setStyleSheet(qss_file)
        self.ui.pushButton.clicked.connect(self.run)
        self.ui.toolButton_2.clicked.connect(self.closeWin)
        self.ui.toolButton.clicked.connect(self.rollUp)
        self.ui.textBrowser.setText(text)

    def upload_log(self):
        date = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S") + str(random.randint(1, 60))
        yandex_token.upload("log.log", f"/log{date} .log")

    def closeWin(self):
        self.upload_log()
        sys.exit()

    def rollUp(self):
        self.showMinimized()

    def run(self):
        def userCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                bot = 'Скажите что-нибудь...'
                print(bot)
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language="ru-RU").lower()
                print('Пользователь: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = userCommand()
            logger(command)
            return command

        def userAnswer():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                bot = 'Назовите номер ответа...'
                print(bot)
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language="ru-RU").lower()
                print('Ваш ответ: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = userAnswer()
            logger(command)
            return command

        def isPartInList(cmd, list):
            for word in list:
                if word.lower() in cmd.lower():
                    return True
            return False

        def readAnswer(ans_list):
            for ans in ans_list:
                speak(ans)

        def speak_n_logger(bot):
            f = open('log.log', 'a')
            now = datetime.datetime.now()
            if bot is not None:
                speak(bot)

            if bot is not None:
                f.write('BOT\t' + bot + '\t' + str(datetime.date.today()) + '\t' + str(now.hour) + ':' + str(
                    now.minute) + ':'
                        + str(now.second) + '\n')
            f.close()

        def logger(user):
            f = open('log.log', 'a')
            now = datetime.datetime.now()
            if user is not None:
                f.write('USER\t' + user + '\t' + str(datetime.date.today()) + '\t' + str(now.hour) + ':' + str(
                    now.minute) + ':'
                        + str(now.second) + '\n')

            f.close()

        def logger_ans(ans_list):
            f = open('log.log', 'a')
            now = datetime.datetime.now()
            if ans_list is not None:
                f.write('BOT\t' + str(ans_list) + '\t' + str(datetime.date.today()) + '\t' + str(now.hour) + ':' + str(
                    now.minute) + ':'
                        + str(now.second) + '\n')
            f.close()

        def scoringPoints(prog_lang_ask, prog_lang_ans):

            def speakAskAndAns(count):
                speak_n_logger(prog_lang_ask[count])
                readAnswer(prog_lang_ans[count])
                logger_ans(prog_lang_ans[count])

            count = 0
            total = 0

            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, second):
                total = total + 1
            # 2 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return -1
            if isPartInList(ans, first):
                total = total + 1
            # 3 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, second):
                total = total + 1
            # 4 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, fourth):
                total = total + 1
            # 5 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, second):
                total = total + 1
            # 6 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, first):
                total = total + 1
            # 7 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, third):
                total = total + 1
            # 8 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, third):
                total = total + 1
            # 9 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, second):
                total = total + 1
            # 10 ask
            count = count + 1
            speakAskAndAns(count)
            ans = userAnswer()
            if isPartInList(ans, exit):
                speak_n_logger('Тест завершен!')
                return 0
            if isPartInList(ans, fourth):
                total = total + 1

            if total >= 9:
                speak_n_logger('Вы прекрасно знаете данным языком программирования! Отличный результат!')
            elif total >= 7:
                speak_n_logger('Вы неплохо владеете данным яыком программирования! Хороший результат!')
            elif total >= 5:
                speak_n_logger('Я думаю Вам нужно больше практики и все получится! Удовлетворительный результат')
            elif total <= 4:
                speak_n_logger('Тест провален! :(')

        def assistant(command):
            try:
                if isPartInList(command, test):
                    tmp = None
                    speak_n_logger('Тест по какому языку программирования вы хотите пройти?')
                    speak_n_logger('Python, Java, C плюс плюс')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)
                    tmp = r.recognize_google(audio, language="ru-RU").lower()
                    logger(tmp)
                    speak_n_logger('Ну что же... Начнем!')
                    speak_n_logger('Чтобы дать ответ: произнесите номер правильного варианта')
                    if (isPartInList(tmp, java_test)):
                        total = scoringPoints(java_ask, java_ans)
                        speak_n_logger('Результат: ' + str(total) + ' баллов')
                    elif (isPartInList(tmp, cpp_test)):
                        total = scoringPoints(cpp_ask, cpp_ans)
                        speak_n_logger('Результат: ' + str(total) + ' баллов')
                    elif (isPartInList(tmp, python_test)):
                        total = scoringPoints(python_ask, python_ans)
                        speak_n_logger('Результат: ' + str(total) + ' баллов')

                elif (isPartInList(command, pics)):
                    speak_n_logger('Картинки по какому запросу вы бы хотели увидеть?')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)
                    query = r.recognize_google(audio, language="ru-RU")
                    pic = query.lower()
                    logger(pic)
                    print('Пользователь: ' + pic + '\n')
                    webbrowser.open('https://yandex.ru/images/search?text=' + pic)

                elif 'найди' in command:
                    reg_ex = re.search('найди (.*)', command)
                    if reg_ex:
                        url = reg_ex.group(1)
                        webbrowser.open('https://yandex.ru/search/search?text=' + url)
                        speak_n_logger('Вот что нашлось в интернете по вашему запросу')
                    else:
                        speak_n_logger('Что конкретно нужно найти?')
                        url = userCommand()
                        webbrowser.open('https://yandex.ru/search/search?text=' + url)
                        speak_n_logger('Вот что нашлось в интернете по вашему запросу')

                elif 'новости' in command:
                    news_url = "https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru"
                    Client = urlopen(news_url)
                    xml_page = Client.read()
                    Client.close()
                    soup_page = soup(xml_page, "xml")
                    news_list = soup_page.findAll("item")
                    speak_n_logger('Итак, новости на сегодня:')
                    for news in news_list[:5]:
                        speak(news.title.text)


                elif (isPartInList (command,excel)):
                    path = "excel.exe"
                    os.startfile(path)

                elif isPartInList(command, cmd ):
                    path = "cmd.exe"
                    os.startfile(path)

                elif isPartInList(command, msword):
                    path = "winword.exe"
                    os.startfile(path)

                elif isPartInList(command, paint):
                    path = "mspaint.exe"
                    os.startfile(path)

                elif (isPartInList(command, music)):
                    speak_n_logger('Какую песню мне включить?')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)
                    query = r.recognize_google(audio, language="ru-RU")
                    mus = query.lower()
                    logger(mus)
                    print('Пользователь: ' + mus + '\n')
                    webbrowser.open('https://music.youtube.com/search?q=' + mus)
                    auto.sleep(3)
                    auto.click(460, 368)

                elif (isPartInList(command, video)):
                    speak_n_logger('Какое видео мне включить?')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)

                    query = r.recognize_google(audio, language="ru-RU")
                    vid = query.lower()
                    logger(vid)
                    print('Пользователь: ' + vid + '\n')
                    webbrowser.open('https://youtube.com/search?q=' + vid)
                    auto.sleep(3)
                    auto.click(460, 368)

                elif (isPartInList(command, translate_alias)):
                    speak_n_logger('Говорите фразу на русском языке')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)

                    query = r.recognize_google(audio, language="ru-RU")
                    trans = query.lower()
                    logger(trans)
                    print('Пользователь: ' + trans + '\n')
                    translator = Translator(from_lang="ru", to_lang="en")

                    result = translator.translate(str(trans))
                    speak_n_logger(result)

                elif (isPartInList(command, weather)):
                    speak_n_logger('Уточните название города')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)

                    city = r.recognize_google(audio, language="ru-RU").lower()
                    logger(city)
                    print('Пользователь: ' + city + '\n')
                    owm = pyowm.OWM('9b242ce98c6d9eba3bf99f872f636b74')
                    obs = owm.weather_manager().weather_at_place(city)
                    w = obs.weather
                    k = w.status
                    if k == 'Clouds':
                        k = 'Облачно'
                    elif k == 'Clear':
                        k = 'Ясно'
                    elif k == 'Rain':
                        k = 'Дождь'
                    elif k == 'Snow':
                        k = 'Снег'
                    temp = w.temperature("celsius")
                    speak_n_logger(str('Погода в городе ' + city + ' - ' + k + '. Температура воздуха ' + str(
                        int(temp['temp'])) + ' градусов по Цельсию'))

                elif (isPartInList(command, times)):

                    now = datetime.datetime.now()
                    speak_n_logger("Сейчас " + str(now.hour) + ":" + str(now.minute))

                elif (isPartInList(command, github)):
                    url = 'https://github.com/'
                    webbrowser.open(url)
                    speak_n_logger('Открываю гитхаб')

                elif (isPartInList(command, habr)):
                    url = 'https://habr.com/'
                    webbrowser.open(url)
                    speak_n_logger('Открываю Хабр')

                elif (isPartInList(command, vk)):
                    url = 'https://vk.com/'
                    webbrowser.open(url)
                    speak_n_logger('Открываю ВКонтакте')

                elif (isPartInList(command, stackoverflow)):
                    url = 'https://stackoverflow.com/'
                    webbrowser.open(url)
                    speak_n_logger('Открываю Stack Overflow')

                elif (isPartInList(command, python)):
                    speak_n_logger('Какой пакет найти?')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)

                    query = r.recognize_google(audio, language="ru-RU")
                    pckg = query.lower()
                    logger(pckg)
                    print('Пользователь: ' + pckg + '\n')
                    url = "https://pypi.org/search/?q=" + pckg
                    webbrowser.open(url)
                    speak_n_logger('Открываю ')


                elif 'открой' in command:
                    speak_n_logger('Пожалуйста, назовите сайт с доменом')
                    r = sr.Recognizer()
                    with sr.Microphone(device_index=1) as source:
                        audio = r.listen(source)
                    site = r.recognize_google(audio, language="ru-RU").lower()
                    logger(site)
                    print('Пользователь: ' + site + '\n')
                    url = 'https://www.' + site
                    webbrowser.open(url)
                    speak_n_logger('Открываю ' + site)

                elif (isPartInList(command, help_git)):
                    speak_n_logger('Открываю небольшой справочник по GitHub')
                    webbrowser.open("https://github.com/ashtanyuk/Git-intro")

                elif (isPartInList(command, hello)):
                    day_time = int(time.strftime('%H'))
                    if day_time < 12:
                        speak_n_logger('Доброе утро')
                    elif 12 <= day_time < 18:
                        speak_n_logger('Добрый день')
                    else:
                        speak_n_logger('Доброй ночи')

                elif (isPartInList(command, help)):
                    speak_n_logger("""
                        Вы можете попросить у меня:
                        - открыть популярные сайты: github, stackoverflow, habr или отркыть любую другую страницу в интернете
                        - пройти тестирование и узнать свой уровень знаний по трем популярным языкам программирования
                        - открыть соц. сеть ВКонтакте
                        - включить музыку
                        - включить видео
                        - рассказать актуальные новости на день
                        - узнать о погоде
                        - показать справочник по работе с GitHub
                        - найти пакет для python
                        - узнать текущее время
                        - открыть некоторые приложения (excel, командную строку, word, paint, wordpad)
                        - найти картинку в интернете 
                        - перевести текст с английского на русский 
                        - рассмешить Вас
                        - если нечего делать могу подкинуть пару мыслей или можем просто поболтать
                        """)

                elif (isPartInList(command, joke)):
                    speak_n_logger(random.choice(jokes))

                elif (isPartInList(command, moood)):
                    speak_n_logger(random.choice(mood))

                elif (isPartInList(command, what_to_do)):
                    speak_n_logger(random.choice(things))

                elif 'как' in command:
                    reg_ex = re.search('как (.*)', command)
                    if reg_ex:
                        url = reg_ex.group(1)
                        webbrowser.open('https://yandex.ru/search/search?text=' + url)
                        speak_n_logger('Вот, что нашлось в интернете по вашему запросу')
                    else:
                        speak_n_logger('Что конкретно нужно найти?')
                        userCommand()
            except sr.UnknownValueError:
                print("Кажется, я тебя не поняла, повтори еще раз")


        assistant(userCommand())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MyWin()
    setMoveWindow(mainWin)
    mainWin.show()
    speak('Привет')
    sys.exit(app.exec_())

