def _max_len(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    else:
        print(str2)

str1, str2 = map(str, input().split(', '))
_max_len(str1, str2)
