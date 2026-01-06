import time
import sys
from typing import Union

def special_print(text: str) -> str:
    for i in text:
        print(i,end='',flush=True)
        time.sleep(0.005)

def introduction() -> str:
    intro = 'hello this program is served as a roadmap for your direction'.title()
    special_print(intro)

introduction()
def choice() -> Union[None, str]:
    directions = '''
            Frondend | Backend | QA | Devops
            '''
    special_print(directions)
    while True:
        choice = 'choose your direction or press gg to exit: '.title()
        special_print(choice)
        data = input('')
        data = data.lower()
        if data == 'gg':
            print('you went out from the roadmap')
            sys.exit()
        else:
            return data
    
def backend() -> str:
    text = '''
        Бэкенд-разработка — это создание серверной части веб-приложений, которая отвечает за обработку данных, 
        выполнение логики приложения и взаимодействие с базами данных. 

        1.Изучите основы Python или другого языка (например, JavaScript, Java)
       
        2.Основы веб-разработки
            HTML, CSS, JavaScript
            HTML & CSS
            JavaScript
        3.Основы бэкенда
            Введение в серверы, API, базы данных
            Flask (Python)
            Node.js
        4.Работа с базами данных
            SQL и NoSQL
            SQL Tutorial
            MongoDB
            '''
    return text

def frontend() -> str:
    text = '''
        Основы веба
            HTML — структура страниц
            Ресурс: HTML Tutorial — MDN
            CSS — стилизация
            Ресурс: CSS Tutorial — MDN
           JavaScript (JS) — программирование на стороне клиента
        Ресурс: JavaScript Guide — MDN
        2. Продвинутый JavaScript
            Работа с DOM (Document Object Model)
            DOM Tutorial — MDN
            Асинхронность: callbacks, promises, async/await
            Асинхронный JS — learn.javascript.ru
            Модули и сборка
            JavaScript Modules — MDN
        3. Инструменты разработчика
            Git и GitHub для контроля версий
            Pro Git Book
            NPM / Yarn — менеджеры пакетов
            '''
    return text

def QA_development() -> str:
    text = '''
        1. Основы тестирования
            Что такое тестирование ПО, зачем оно нужно
            Виды тестирования: функциональное, нефункциональное, регрессионное, приемочное и др.
            Жизненный цикл разработки ПО (SDLC) и роль QA
            Основные термины: баг, дефект, тест-кейс, тест-план, тест-сьют
        2. Типы тестирования
            Ручное тестирование (Manual Testing)
            Автоматизированное тестирование (Automation Testing) — введение
            Тестирование производительности (Performance Testing)
            Тестирование безопасности (Security Testing)
            Тестирование совместимости (Compatibility Testing)
            Тестирование юзабилити (Usability Testing)
        3. Тест-дизайн и документация
            Написание тест-кейсов и чек-листов
            Создание тест-планов
            Отчёты о дефектах (bug reports)
            Методы тест-дизайна: эквивалентное разбиение, граничные значения, таблицы принятия решений
        '''
    return text
def DevOps() -> str:
    text = '''
        Вот базовый роадмап по DevOps — ключевые темы и навыки, которые стоит изучить, чтобы стать специалистом в этой области:
        1. Основы
            Понимание что такое DevOps, цели и принципы (CI/CD, автоматизация, культура сотрудничества)
            Знакомство с жизненным циклом разработки ПО (SDLC) и ролью DevOps
        2. Операционные системы и сетевые основы
            Основы Linux (командная строка, файловая система, права доступа)
            Основы сетей: IP, DNS, HTTP/HTTPS, порты, VPN
        3. Контейнеризация
            Docker: создание, управление контейнерами и образами
            Docker Compose для оркестрации локальных контейнеров
        4. Оркестрация контейнеров
            Kubernetes: архитектура, деплой приложений, управление кластерами
            Helm — менеджер пакетов для Kubernetes
        5. Системы контроля версий
            Git: базовые и продвинутые команды, ветвление, слияния
            Работа с GitHub, GitLab, Bitbucket
        '''
    return text

def main():
    user_choice = choice()
    if user_choice == 'Backend':
        print(backend())
    
    elif user_choice == 'Frontend':
        print(frontend())
   
    elif user_choice.upper() == 'QA':
        print(QA_development())
    
    elif user_choice == 'Devops':
        print(DevOps())
    
    else:
        sys.exit()

if __name__ == '__main__':
    main()
