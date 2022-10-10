def _factorial(num):
    if num > 1:
        return num *  _factorial(num - 1)
    else:
        return 1

print(_factorial(int(input())))
