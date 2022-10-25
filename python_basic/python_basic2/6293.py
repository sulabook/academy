import math
r_list = list(map(float, input().split(', ')))
circumferences = []
for r in r_list:
    circumferences.append(2 * math.pi * r)
for i in range(len(circumferences)):
    if i == len(circumferences) - 1:
        print(f'{circumferences[i]:.2f}')
    else:
        print(f'{circumferences[i]:.2f}, ', end='')
