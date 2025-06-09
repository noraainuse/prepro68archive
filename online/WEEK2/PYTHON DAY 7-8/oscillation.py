'''Oscillation'''
from math import pi, sqrt, floor

def main():
    '''main'''
    l = float(input()) / 100
    x = float(input())
    n = floor(x / (2 * pi * sqrt(l / 9.81)))
    if n >= 1:
        print(n)
    else:
        print('Partial swing')

main()
