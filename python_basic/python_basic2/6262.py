s1 = input()
d1 = {k:0 for k in s1}
for e in s1:
    d1[e] += 1
for k, v in d1.items():
    print(f'{k},{v}')
