a = [[1, 2], [3, 4]]
c = [j for i in a for j in i]
# print(c)


#######################################
# документирование кода


def count_elements(list_of_items: list) -> dict:
    """возращает словарь, где ключи - слова, а значения - кол-во раз, которое они встретились в тексте"""

    amount_of_elements = {}
    for item in list_of_items:
        amount_of_elements[item] = amount_of_elements.get(item, 0) + 1

    return amount_of_elements

#print(count_elements.__doc__)

# использовать reST style


####################################################
# lambda functions

lst = list(map(lambda x: x*x, [4, 5, 6]))
# print(x)

print((lambda x, y, z: x+z+y)(1, 2, 3))
print((lambda x, y, z=3: x+z+y)(1, 3))
print((lambda *args: sum(args))(1, 3, 2))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=3, three=2))


#####################################################
# HOF (функции высшего порядка)
# map(func, [...]), filter(func,[...]), reduce(func, init, [...])

def map_func(x):
    return x**2


square_list = map(lambda x: x**2, [1, 2, 3])
print(list(square_list))

square_list = map(map_func, [1, 2, 3])
print(list(square_list))

filtered_list = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(filtered_list))

items = [{'name': 'Johan'}, {'name': 'Silvia'}, {'name': 'Julia'}]
print(list(filter(lambda item: item['name'].startswith('J'), items)))
print(list(filter(lambda item: item['name'], items)))

from functools import reduce


print(a)
print(reduce(lambda x, y: x*y, [1, 2, 3, 4], 0))  # 0 - начальное значение, т.е. (0*1)*2 ...
print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))  # ((1*2)*3)*4

def custom_func(name: str, age: int) ->dict:
    """
    Build dict with provide arguments
    :param name: user's name
    :param age: user's age
    :return: dict with provide params
    """
    pass

# print('custom_func:', custom_func.__doc__)
# help(custom_func)


from lib import module

# help(module)

############################################################
# декоратор


def full_name(first_name: str, last_name: str) -> str:
    return f'{first_name} {last_name}'


print(full_name('John', 'Wick'))


def capitalize(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


decorated_full_name = capitalize(full_name)
print(decorated_full_name("John", "Wick"))

@capitalize
def new_full_name(first_name: str, last_name: str):
    return f'{first_name} {last_name}'


print(new_full_name('Klark', 'Kent'))

def custom_f():
    def summ(*args):
        return sum(args)
    return summ


print(custom_f()(1,2,3,4))

def custom_f():
    def summ(*args):
        def one_more(*args):
            return len(args)
        return one_more
    return summ


print(custom_f()(1,2,3,4))