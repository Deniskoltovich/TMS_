def func():
    # пытаемся подключится к базе данных
    raise ConnectionError

try:
    func()
except ConnectionError as e:
    # raise RuntimeError('Failed to connect to db')
    # чтобы прервать цепочку
    raise RuntimeError('Failed to connect to db') from None