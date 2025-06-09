'''projectile'''
from math import sin, cos, sqrt, radians

def main():
    '''main'''
    #input
    u = float(input())
    zeta = radians(float(input()))
    h = float(input())

    #fml
    big_high =  h + (pow((u * sin(zeta)), 2) / (2 * 9.8))
    total_time = (u * sin(zeta)) / 9.8 + sqrt((2 * big_high) / 9.8)
    total_displacement = (u * cos(zeta)) * total_time

    # Total air time
    print(f'Total air time = {total_time:.2f}')
    # Total displacement
    print(f'Total displacement = {total_displacement:.2f}')

main()
