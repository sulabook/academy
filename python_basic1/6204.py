import sys
sys.stdin = open('ex_6204_input.txt', 'r')
inch = float(input())

def inch_to_cm(inch):
    return inch * 2.54

print(f'{inch:.2f} inch => {inch_to_cm(inch):.2f} cm')
