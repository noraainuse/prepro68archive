'''distance'''
import math as m
def dis(x1, y1, x2, y2):
    '''distance'''
    print(f'{(m.sqrt((pow(x2 - x1, 2)) + (pow(y2 - y1, 2)))):.3f}')
dis(float(input()), float(input()), float(input()), float(input()))
