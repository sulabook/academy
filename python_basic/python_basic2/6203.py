class Student():
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def get_sum(self):
        return self.__kor + self.__eng + self.__math

if __name__ == '__main__':
    kor, eng, math = map(int, input().split(', '))
    student1 = Student(kor, eng, math)
    print(f'국어, 영어, 수학의 총점: {student1.get_sum()}')
