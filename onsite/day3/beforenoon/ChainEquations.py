'''main'''
import math
def main(a, b):
    '''main'''
    w = abs(a ** b) + abs(b ** a) + 4
    x = abs((math.sin((math.pi * w))) + ((math.cos(w)) ** b)) + w
    y = math.log(x, w) + math.log(x)
    z = math.sqrt(w) + math.exp(x) + (y ** (1 / 8))
    r = (z ** 3) + math.e
    print(f'{r:,.4f}')
main(float(input()), float(input()))
