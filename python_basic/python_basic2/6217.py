class Student():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"이름: {self.name}"

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return f"이름: {self.name}, 전공: {self.major}"

if __name__ == "__main__":
    s1 = Student('홍길동')
    gs1 = GraduateStudent('이순신', '컴퓨터')
    print(s1)
    print(gs1)
        
