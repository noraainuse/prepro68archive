'''sinewive'''
from math import sin, pi
def main():
    '''main'''
    a = float(input())
    f = float(input())
    rd_corner = 2 * pi * f
    x = round(a * sin(rd_corner))
    angle_degree = rd_corner * (180/pi)
    print(x)
    print(f'{angle_degree:.2f}')

main()
