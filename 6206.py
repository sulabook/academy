import sys
sys.stdin = open('ex_6206_input.txt', 'r')

kg = float(input())

def kg_to_lb(kg):
    return kg * 2.2046

print(f'{kg:.2f} kg => {kg_to_lb(kg):.2f} lb')
