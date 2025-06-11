'''gcd'''
import math as m
def find_lcm(one, two):
    '''lcm'''
    return m.lcm(one, two)
def find_gcd(one, two):
    '''gcd'''
    return m.gcd(one, two)
def main():
    '''main'''
    text = input()
    match text:
        case "lcm":
            one = int(input())
            two = int(input())
            print(find_lcm(one, two))
        case "gcd":
            one = int(input())
            two = int(input())
            print(find_gcd(one, two))
        case _:
            print("Invalid input. Please enter 'gcd' or 'lcm'.")
main()
