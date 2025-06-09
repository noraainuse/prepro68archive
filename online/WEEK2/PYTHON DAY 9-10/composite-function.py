'''composite-function'''
import math
N = float(input())
A = float(input())
B = float(input())

def composite(n, a, b):
    '''composite'''
    func1 = math.cos(math.pow(a, math.exp(math.sqrt(a * b))))
    func2 = math.pow(a, b)
    func3 = math.pow(a, math.pow(a * math.log(b, a), 1/n))
    func4 = math.pow(a, math.log(b, a))
    func5 = 4 * math.sqrt(math.pow(a * b, 1/n))
    return n + func1 + func2 - func3 + func4 + func5

def main():
    '''main'''
    print(round(composite(N, A, B), 2))
main()
