nums_squared_ls = [num ** 2 for num in range(10000)]
num_squared_gc = (num ** 2 for num in range(1000))


import sys
print(sys.getsizeof(nums_squared_ls))
print(sys.getsizeof(num_squared_gc))

# смотрим производительность
import  cProfile
cProfile.run('sum([num ** 2 for num in range(10000)])')
cProfile.run('sum((num ** 2 for num in range(10000)))')

def gen_1(n):
    for  i in range(n):
        yield f'g1={i}'

def gen_2(n, m):
    for j in range(n, m):
        yield f'g2= {j}'

def gen_3(n, m):
    yield from gen_1(n)
    yield from gen_2(n, m)
    yield from gen_2(n, m + 5)

g = gen_3(4, 10)
for i in g:
    print(i)