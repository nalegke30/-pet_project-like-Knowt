preparation = False
try:
    coordinats = input('Привет, введи координаты фигуры, например(b3) и программа покажет все возможные перемещения на шахматной доске: ')
    name = input('Также введи название фигуры: ').lower()
    if coordinats[0] in ('abcdefgh') and int(coordinats[1]) in (12345678):
        preparation = True
except TypeError:
    print('Произошла ошибка, повторите еще раз')
except ValueError:
    print('Произошла ошибка, пожалуйста введите координаты фиугры')
x = '87654321'.index(coordinats[1])
y = 'abcdefgh'.index(coordinats[0])  
    
matrix = [['.'] * 8 for i in range(8)]

if name == 'ладья':
    for i in range(8):
        for j in range(8):
            if x == i or y ==j:
                matrix[i][j] = '*'
    matrix[x][y] = 'R'
    for i in matrix:
        print(*i)

elif name == 'ферзь':
    for i in range(8):
        for j in range(8):
            if abs(x-i) == abs(y-j) or x == i or y == j:
                matrix[i][j] = '*'
    matrix[x][y] = 'Q'
    for row in matrix:
        print(*row)

elif name == 'конь':
    for i in range(8):
        for j in range(8):
            if (x-j)*(y-i) == 2 or (x-j)*(y-i) == -2:
                matrix[j][i] = '*'
    matrix[x][y] = 'N'
    for row in matrix:
        print(' '.join(row))

elif name == 'слон':
    for i in range(8):
        for j in range(8):
            if abs(x-i) == abs(y-j):
                matrix[i][j] = '*'
    matrix[x][y] = 'E'
    for row in matrix:
        print(*row)

elif name == 'король':
    for i in range(8):
        for j in range(8):
            if x - 1 <= i <= x + 1 and y - 1 <= j <= y + 1:
                matrix[i][j] = '*'
    matrix[x][y] = 'K'
    for row in matrix:
        print(*row)
    
