from typing import Dict, Generator, List


Task = Dict[str, str | bool] # ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ TASK
tasks: List[Task] = [] # ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ tasks

def build_task(name: str, describe: str) -> Task: # создаем словарь с основными характеристиками
    return {
        "name": name,
        "description": describe,
        "completed": False
        }



def add_task(name: str, describe: str) -> None: # добавляем задачу
    res = build_task(name, describe)
    tasks.append(res) # добалвяем в список

def list_tasks(check: bool | None = None) -> Generator[Task, None, None]:
    '''
    Возвращает задачи из глобального списка tasks по заданному фильтру.
    
    :param check: 
        - True — вернуть только выполненные задачи
        - False — вернуть только активные задачи
        - None — вернуть все задачи
    :return: Генератор, который по одному выдаёт словари задач (Task)
    '''
    for task in tasks:
        if check is None or check == task['completed']:
            yield task



def show_all_tasks(create_task: Generator[Task, None, None]) -> None:
    '''
    Docstring для show_all_tasks
    :param create_task: Описание
    :type create_task: Generator[Task, None, None]
    '''
    for number, task in enumerate(create_task):
        status = "✔️" if task['completed'] else "❌️"
        print(f"Статус {status} № {number}\nназвание - {task['name']}\nописание - {task['description']}")

def task_counter():
    def completed() -> int:
        return sum(task['completed'] for task in tasks) # все активные задачи
    def finished() -> int:
        return sum(not task['completed'] for task in tasks) # все завершенные задачи
    return completed, finished

def mark_completed(index: int) -> bool: # завершаем задачу
    try:
        tasks[index]['completed'] = True
        return True
    except IndexError:
        return False


def remove_task(idx: int) -> bool: # удаляем задачу
    try:
        del tasks[idx]
        return True
    except IndexError:
        return False

def main(): # основной блок, где выполняются все функции
    print('Добро пожаловать в менеджер продуктивности')
    while True:
        print(
        "\n1. Добавить задачу"
        "\n2. Показать все задачи"
        "\n3. Показать активные"
        "\n4. Показать выполненные"
        "\n5. Завершить задачу"
        "\n6. Удалить задачу"
        "\n7. Статистика"
        "\n0. Выход"
        )
        choice = input('Выберите дейтсвие: ')
        match choice:
            case '1':
                nam = input('Как будет называться задача: ')
                describ = input('Дайте описание к своей задаче: ')
                add_task(nam, describ)
            
            case '2':
                show_all_tasks(list_tasks())
                
            case "3":
                show_all_tasks(list_tasks(False)) # False - вернуть только активные задачи
                
            case "4":
                show_all_tasks(list_tasks(True)) # True - вернуть только выполненные задачи
            
            case "5":
                try:
                    num = int(input("Введите номер задачи, нумерация начинается с 0: ")) 
                    mark_completed(num)
                except ValueError:
                    print("Требуется ввести только число")
            
            case "6":
                try:
                    info = int(input('Напишите номер задачи: '))    
                    remove_task(info)
                except ValueError:
                    print("Требуется ввести только число")
                 
            case "7":
                current, finished = task_counter()
                print(f'Активные: {current()}')
                print(f'Завершенные: {finished()}')
            
            case "0":
                print('Выходим...')
                break
            
            case _:
                print("Неверный ввод")
    

if __name__ == '__main__':
    main()