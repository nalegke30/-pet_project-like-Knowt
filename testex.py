import time 
import random
from typing import Any, Union

def складывание(x: int , y: int) -> int:
    return x + y

def вычитание(x: int, y: int) -> int:
    return x - y

def умножение(x: int, y: int) -> int:
    return x * y

def деление(x: int, y: int) -> int:
    return x / y

def oformation(sentense: Any) -> Any:
    for text in sentense:
        print(text, end='', flush=True)
        time.sleep(0.02)

def main() -> Union[str, int, None]:
    print("Смотри, вы вводите два числа и происходит рандомная операция.")
    while True:
        try:
            num1, num2  = map(int, input('Введите только два числа через пробел: ').split())
            operation = {складывание: 1, вычитание: 2, умножение: 3, деление: 4}
            
            
            number = random.randint(1,5)
            for function, digit in operation.items():
                if digit == number:
                    result = function(num1, num2)
                    function_name = function.__name__
                    
                    print(f"Результат: {result}, операция {function_name}")
              
        except ZeroDivisionError:
            oformation('Вы не можеть поделить на ноль!\n')
        except ValueError:
            oformation('Вводить можно только числа!\n')


if __name__ == '__main__':
    main()