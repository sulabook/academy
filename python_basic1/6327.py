def _square(list1):
    for e in list1:
        print(f'square({e}) => {e*e}')

list1 = map(int, input().split(', '))
_square(list1)
