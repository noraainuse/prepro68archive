'''Calculator'''
import math
operator = int(input())
def main():
    '''to print the result'''
    match operator:
        case 1:
            x = int(input())
            y = int(input())
            print(f"Result: {x} + {y} = {x + y}")
        case 2:
            x = int(input())
            y = int(input())
            print(f"Result: {x} - {y} = {x - y}")
        case 3:
            x = int(input())
            y = int(input())
            print(f"Result: {x} x {y} = {x*y}")
        case 4:
            x = int(input())
            y = int(input())
            if y:
                print(f"Result: {x} / {y} = {x/y}")
            else:
                print("Error")
        case 5:
            x = int(input())
            y = int(input())
            print(f"Result: {x}^{y} = {math.pow(x,y)}")
        case 6:
            x = int(input())
            if x >= 0:
                print(f"Result: √{x} = {math.sqrt(x)}")
            else:
                print("Error")
        case 7 :
            x = int(input())
            y = int(input())
            if x > 0 and y > 0 and y != 1:
                print(f"log base {y} of {x} is: {math.log(x,y)}")
            else:
                print("Error")
        case 8:
            x = int(input())
            if x >= 0:
                print(f"Result: {x}! = {math.factorial(x)}")
            else:
                print("Error")
        case _:
            print("Invalid choice.")
main()
