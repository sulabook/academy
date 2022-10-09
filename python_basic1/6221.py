list1 = ["가위", "바위", "보"]
Man1 = input()
Man2 = input()
win = {(list1[0], list1[2]), (list1[1], list1[0]), (list1[2], list1[1])}
    
if (Man1, Man2) in win:
    print('Result : Man1 Win!')
elif Man1 == Man2:
    print('Result : Draw')
else:
    print('Result : Man2 Win!')
