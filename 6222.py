ch = input()
diff = ord('a') - ord('A')

if ord('a') <= ord(ch) <= ord('z'):
    print(f'{ch}(ASCII: {ord(ch)}) => {chr(ord(ch) - diff)}(ASCII: {ord(ch) - diff})')
elif ord('A') <= ord(ch) <= ord('Z'):
    print(f'{ch}(ASCII: {ord(ch)}) => {chr(ord(ch) + diff)}(ASCII: {ord(ch) + diff})')
else:
    print(ch)
