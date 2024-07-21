import math
a = 9
print(math.sqrt(a))

def square_root(x):
    return math.sqrt(x)

print(square_root(9))

def square(x):
    a = x ** 2
    print(locals())
    return a

print(square(9))

a = 5
b = square(4)
print(a)
print(b)
print(globals())

def square(x):
    global a
    a = x ** 3
    print(locals())
    return a

a = 5
b = square(4)
print(a)
print(b)
print(globals())

print(a == b)
print(a is b)
print(id(a))
print(id(b))
#True
#True
#140733177790872
#140733177790872

def square(x):
    return a ** 2

a = 5
b = square(4)
print(a)
print(b)
print(globals())

"""
Область видимости-это, по сути, та часть кода, где у нас переменная доступна, и мы можем её использовать. 
Существует всего 4 области видимости:
- глобальная
- локальная
- объемлющая
- встроенная """

d = 5
def square(x):
    d = x ** 2
    print(d)                    # 9
    def even(x):
        d = x * 2
        print(d)                # 6 - локальное для функции even
        if d % 2 == 0:
            print('Четное')     # Четное - так как 6
        else:
            print('Нечетное')
    even(x)
    return d

a = 5
b = square(3)
print(a)                        # 5 - глобальное пр-во
print(b)                        # 9 - глобальное пр-во из функции square
print(d)                        # 5 - глобальное пр-во

"""
Приоритет - идем изнутри наружу:
- ищем переменную в локальной области видимости функции even - локальная
- если интерпретатор не находит переменную поднимаемся выше - объемлющая область видимости
- если не нашли перемещаемся выше в глобальную область видимости - глобальная
- если и там нет, идем в встроенную область видимости
"""

d = 1
def square(x):
    print(d)                    # 1
    def even(x):
        print(d)                # 1 - локальное для функции even
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')   # нечетное - так как 1
    even(x)
    return d

a = 3
b = square(5)
print(a)                        # 3 - глобальное пр-во
print(b)                        # 1 - глобальное пр-во из функции square
print(d)                        # 1 - глобальное пр-во

print('Nonlocal')
d = 7
def square(x):
    d = x ** 2
    print(d)                    # 16
    def even(x):
        nonlocal d
        print(d)                # 16
        d = x / 2
        print(d)                # 2 - локальное для функции even 4 / 2. Если бы выше d = x / 2, поимели бы 8 - взяли бы d из функции square
        if d % 2 == 0:
            print('Четное')     # Четное
        else:
            print('Нечетное')   # нечетное - так как 1
    even(x)
    return d

a = 3
b = square(4)
print(a)                        # 3 - глобальное пр-во
print(b)                        # 2 - глобальное пр-во из функции square. Если бы выше d = x / 2, поимели бы 8
print(d)                        # 7 - глобальное пр-во