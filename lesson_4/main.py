# ФУНКЦИИ И АРГУМЕНТЫ



def add(a, b):
    return a + b


# print(add(1, 3), add('fsfd', 'dfgdfg'), sep='\n')


def welcome(name):
    return f'Hello, {name}'


def print_list(*args): # сбор аргументов в список
    print(args)


# print_list(1, 2, 3, 4)


def full_func(*args, **kwargs): #обобщенное определение функции
    print(args)  # typle
    print(kwargs) # dict


# full_func(1, 2, 3, a=4, b=5, c=6)


def my_pow(number, power):
    return number ** power + 1


result = my_pow(power=2, number=4) # именованные агрументы


def my_fun(**kwargs):  # сбор аргументов в словарь
    keys, values =[], []
    for key, value in kwargs.items():
        keys.append(key)
        values.append(value)
    return keys, values


keys, values = my_fun(a=5)

################################################################################

def print_name(name):
    print(f'Hello {name}')


print_name('John')


def output(*args, new_line=False):
    print(*args, sep='\n' if new_line else '')


output(1, 2, 3, 4, 5, new_line=True)


def test_args(*args, **kwargs):
    print(args, kwargs)


test_args(1, 2, True, x=10, y=15)


def func(a, b=10):
    return a + b, a - b, a * b, a / b


x = func(5, 18)
print(x)
sum, diff, mul, div = x


# ОБЛАСТЬ ВИДИМОСТИ
# АННОТАЦИИ

def hello(name: str = 'world') -> str:
    return 'Hello' + name


def add_int(a: int, b: int) -> int:
    return a + b


from typing import Optional


def create_obj(obj: Optional[int] = None):
    pass


create_obj()
create_obj('a') # подсказывает, что либо инт, либо ничего
create_obj(5)



# ГЕНЕРАТОРЫ СПИСКОВ
random_list = [i for i in range(1,16)]
my_gen = (i for i in range(1, 16)) # это будет генератор
my_dict = {arg: arg**2 for arg in random_list}

lst = [i**2 for i in range(15) if i % 2 == 0]


def x(*args):
    return [arg**2 for arg in args]



