scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
i = 0
while i < len(scores):
    if scores[i] >= 80:
        sum += scores.pop(i)
        continue
    i += 1
print(sum)
