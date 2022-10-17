inputs = list()
for _ in range(5):
    inputs.append(int(input()))

print('입력된 값 {0}의 평균은 {1:0.1f}입니다.'.format(inputs, sum(inputs)/5))
