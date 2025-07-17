import random
import time
import sys
import csv



print('Hello, in this app you can learn your unknown words')
name, surname = input('Enter your name and surname: ').split()
mainbody = input('if you want to know the main functional of this app - enter "bam": to exit - enter "gg": else to learn "l": ')


if mainbody == 'bam':
    print('it"s the main body')
    print(f"Your name is {name.title()}, surname is {surname.title()}")
    print('this app was creatured by andrew')
    print('Owner tg"s - "https://t.me/nalegke30"')

elif mainbody == 'gg':
    print('Вы покинули приложение')
    sys.exit()

elif mainbody == 'l':
    print('Enter words like(apple, яблоко), when you finish you have to press "Enter" -> "Ctrl Z" -> "Enter": ')
    data = [i.strip().split(', ') for i in sys.stdin]
    columns = ['word','translation']
    with open('information.csv','w',encoding='utf-8',newline='') as file:
        file = csv.writer(file)
        file.writerow(columns)
        for i in data:
            file.writerow(i)
    elseOrNot = input('will you be learning with attempts? yes = y, no = n: ').lower()
    if elseOrNot == 'y':
        with open('information.csv','r',encoding='utf-8') as info:
            info = csv.DictReader(info)
            for i in info:
                print(f"{i}") 
            Continue = input('Are all words correct? and let"s start the circle of learning yes = y,no = n: ').lower()
            if Continue == 'y' or Continue == 'yes':
                with open('information.csv','r',encoding='utf-8') as info:
                    info = csv.DictReader(info)
                    lstMeanings = []
                    lstWords = []
                    for i in info:
                        lstMeanings.append(i['translation'])
                        lstWords.append(i['word'])
                attempt = input('how many attempts do you want to apply? ')
                count = 0
                for word, meaning in zip(lstWords,lstMeanings):
                    attempts = int(attempt)
                    while attempts > 0:
                        mean = input(f'Enter translate of this word {word}').strip()
                        if mean == meaning:
                            print('Correct')
                            count += 1
                            break
                        else:
                            attempts -= 1
                            print(f'you answered uncorrectly, you have {attempts}')
                print(f'Oh, you know {count} words')
    elif elseOrNot == 'n':
        with open('information.csv','r',encoding='utf-8') as info:
                    info = csv.DictReader(info)
                    lstMeanings = []
                    lstWords = []
                    for i in info:
                        lstMeanings.append(i['translation'])
                        lstWords.append(i['word'])
        indexes = list(range(len(lstWords)))
        random.shuffle(indexes)
        lstWords = [lstWords[i] for i in indexes]
        lstMeanings = [lstMeanings[j] for j in indexes]
        
        ln_lstWords = len(lstWords)
        cor = 0
        timer = 0
        while ln_lstWords > 0:
            print(f"Write meanings or translations of these words -> {lstWords}") 
            start = time.monotonic()
            answers = input('write your answers by comma: ').strip()
            changed_answers = [row.strip() for row in answers.split(',')]
            if changed_answers == lstMeanings:
                cor += 1
                end = time.monotonic()
                plenty_of_time = end - start
                timer += plenty_of_time
                print(f"Corrrect! You solved it for {round(plenty_of_time,2)} seconds")
                ln_lstWords -= 1 
                break
            else:
                print('Try again')
        
        if round(plenty_of_time) > 60:
            minutes = plenty_of_time // 60
            seconds = plenty_of_time % 60
            print(f'From {len(lstWords)} words you have correctly answered for {minutes} minutes and {seconds} seconds')
        else:
            print(f'From {len(lstWords)} words you have correctly answered for {round(plenty_of_time,2)} seconds')
    
    else:
        print('PLEASE ENTER Y OR N (sorry for high voice)')

else:
    print('Bro, enter correct commands!')

    
