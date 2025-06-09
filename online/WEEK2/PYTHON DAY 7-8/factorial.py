'''factorial'''
from math import factorial
def main():
    '''main'''
    num1 = int(input())
    if num1 < 0:
        print('Factorial of a negative number is not defined.')
    else:
        result = factorial(num1)
        print(f'{num1}! = {result}')

main()
