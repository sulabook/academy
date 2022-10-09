class User:
    def __init__(self):
        self._name = ''
        self._value = ''

    def __str__(self):
        return f'name = {self._name}, value = {self._value}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

def make_win(user1, user2):
    global win
    if (user1.value, user2.value) in win:
        print(f'{user1.value}가 이겼습니다!')
    elif user1.value == user2.value:
        print('비겼습니다!')
    else:
        print(f'{user2.value}가 이겼습니다!')

user1 = User()
user2 = User()
user1.name = input()
user2.name = input()
user1.value = input()
user2.value = input()

list1 = ["가위", "바위", "보"]
win = {(list1[0], list1[2]), (list1[1], list1[0]), (list1[2], list1[1])}

make_win(user1, user2)
