'''pool'''
from math import pi
def main(pansonkrang, deepdown):
    '''main'''
    if pansonkrang <= 0 or deepdown <= 0:
        print("The values must be positive numbers only.")
    else:
        r = pansonkrang / 2
        pt = pi * pow(r, 2)
        cb = pt * deepdown
        lt = cb * 1000
        print(f'This circular pool has a surface area of {pt:,.2f} square meters.')
        print(f'It requires about {cb:,.2f} cubic meters of water.')
        print(f'Which is approximately {lt:,.0f} liters.')
main(int(input()), int(input()))
