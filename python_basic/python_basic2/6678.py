data = []
while True:
    try:
        data.append(input().upper())
    except EOFError:
        break
    if data[len(data) - 1] == '':
        data.pop()
        break

for s in data:
    print(f'>> {s}')
