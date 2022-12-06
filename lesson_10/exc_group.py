excs = []
try:
    for x in [1, 0, 1, 0 , 3]:
        if x == 0:
            excs.append(Exception('Zero division'))
        k = 10 / x
    raise ExceptionGroup('Message', excs)
except ExceptionGroup as e:
    print(e)
