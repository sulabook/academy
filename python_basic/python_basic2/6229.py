class Person():
    def __init__(self, sex):
        self.__sex = sex

    @property
    def sex(self):
        return self.__sex

    @classmethod
    def getGender(self):
        return 'Unknown'

class Male(Person):
    def __init__(self, sex = 'Male'):
        super().__init__(sex)

    @classmethod
    def getGender(self):
        return 'Male'

class Female(Person):
    def __init__(self, sex = 'Female'):
        super().__init__(sex)

    @classmethod
    def getGender(self):
        return 'Female'

if __name__ == '__main__':
    print(Male.getGender())
    print(Female.getGender())
