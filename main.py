from stringprep import map_table_b3  # Пункты задачи:
def get_matrix(n, m, value):    #  Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    matrix = []                 # Создайте пустой список matrix внутри функции get_matrix.
    for i in range(n):                 # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([])         # В первом цикле добавляйте пустой список в список matrix.
    for j in range(m):      # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
        matrix[i].append(value)   # Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    print(matrix)
    return matrix               # После всех циклов верните значение переменной matrix.

n = int(input('Задайте количество строк матрицы    :'))
m = int(input('Задайте количество столбцов матрицы :'))
value = input(f'Задайте значения матрицы : ')
#n = int(input(2, 3, 4))
#m = int(input(2, 5, 2))
#value = input(10,42,13)
print('-------' * m)
matrix = get_matrix(n, m, value)                 # Выведите на экран(консоль) результат работы функции get_matix.

if n <= 0:
    print("Матрица пуста, задано неверное количество строк:", n)
elif m <=0:
    print("Матрица пуста, задано невернoе количество столбцов:" ,m)
else:
    print("Матрица воплоти:")
    for i in matrix:

        print(*i)
