l1 = list(input())
result = {'UPPER CASE':0, 'LOWER CASE':0}
for e in l1:
    if ord('a') <= ord(e) <= ord('z'):
        result['LOWER CASE'] += 1
    elif ord('A') <= ord(e) <= ord('Z'):
        result['UPPER CASE'] += 1
for k, v in result.items():
    print(k, v)
