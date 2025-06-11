'''main'''
import math as m
def main(candy, friend):
    '''main'''
    print(f'Each friend will get: {m.floor(candy / friend)} candies')
main(int(input()), int(input()))
