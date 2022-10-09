answer = ""
for i in range(100, 300):
    if i % 2 == 0 and (i // 10) % 2 == 0 and (i // 100) % 2 == 0:
        answer += str(i) + ','
print(answer.rstrip(','))
