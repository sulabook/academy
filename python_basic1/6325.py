def _is_num_in_list(list1, num):
    return num in list1

list1 = [2, 4, 6, 8, 10]
print(list1)
print('5 => {}'.format(_is_num_in_list(list1, 5)))
print('10 => {}'.format(_is_num_in_list(list1, 10)))
