bloodTypes = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
typeCounter = {'A':0, 'O':0, 'B':0, 'AB':0}

for bloodType in bloodTypes:
    typeCounter[bloodType] += 1

print(typeCounter)
