import datetime

today = datetime.date.today()

name = input()
age = int(input())
year = today.year
print('{0}(은)는 {1}년에 100세가 될 것입니다.'.format(name, year + 100 - age))
