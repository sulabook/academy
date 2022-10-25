class Korean():
    __nationality = "대한민국"
    def __init__(self):
        pass

    @classmethod
    def printNationality(cls):
        print(cls.__nationality)
        print(cls.__nationality)

if __name__ == "__main__":
    Korean.printNationality()
