# .send(value)

def gen_num(n):
    number = yield
    while number < n:
        number = yield number
        number += 1


g = gen_num(10)
g.send(None)
print(g.send(5))
print(next(g))
# .throw(exc)
# .close()


def add_to_database(connection_strong: str):
    #db.connect(connection_string)
    #session = db.get_session()

    try:
        while True:
            row = yield
            print('insert into table values({},{},{})'.format(row))
    except CommitException:
        print('commit')
    except AbortException:
        print('abort')

    finally:
        print('abort')
        #db.close()


session = add_to_database('user:pass@local.host/dbname')
session.send((1, 2, 3)) # кидаем в yeild
session.throw(CommitException) # вызывает исключение в генераторе
session.close()
