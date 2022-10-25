str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
list1 = list('aeiou')
list2 = list(str)
for e in list1:
    while e in list2:
        list2.remove(e)
print(''.join(list2))
