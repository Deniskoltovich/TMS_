# ============== EXCEPTIONS ==================
try:
    k = 1 / 0
    oinvo
except ZeroDivisionError:
    print(' catch dev by 0')
except NameError as ne:
    print('name error')
except Exception:
    print('all other exceptions')
else:
    print('no errors')
finally:
    print('we will get there anyway')
##################
try:
    k = 1 / 0
    k = 0
except (ZeroDivisionError, NameError):
    pass

#############################
items = [1, 2, 0, 4]
try:
    for x in items:
        if x == 4:
            raise Exception('We have zero value', 10)
        print(10 / x)
except Exception as e:
    pass
    print(e.args)