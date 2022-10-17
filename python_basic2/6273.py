students = [(90, 80), (85, 75), (90, 100)]
for i in range(len(students)):
    sum = 0
    for j in range(len(students[i])):
        sum += students[i][j]
    print('{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.'.format(i + 1, sum, sum / len(students[i])))
