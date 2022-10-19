data = []
while True:
    data.append(input().upper())
    if data[len(data) - 1] == '':
        data.pop()
        break

for s in data:
    print(f'>> {s}')
