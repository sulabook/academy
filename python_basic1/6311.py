str1 = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
dict1 = {'A':4, 'B':3, 'C':2, 'D':1}
list1 = list(str1)
answer = map(lambda x: dict1[x], list1)
print(sum(answer))
