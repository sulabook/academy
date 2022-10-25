l1 = list(input())
result = {'LETTERS':0, 'DIGITS':0}
for e in l1:
    if ord('a') <= ord(e) <= ord('z') or ord('A') <= ord(e) <= ord('Z'):
        result['LETTERS'] += 1
    elif ord('0') <= ord(e) <= ord('9'):
        result['DIGITS'] += 1
for k, v in result.items():
    print(k, v)
