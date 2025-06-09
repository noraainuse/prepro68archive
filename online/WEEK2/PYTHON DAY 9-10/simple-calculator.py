'''sim_cal'''

A = float(input())
B = float(input())
OP = str(input())
def calculator(a, b, op):
    '''op'''
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if not b:
                return "Error: Division by zero"
            return f'{a / b}'
        case _:
            return "Invalid operator"

def main():
    '''main'''
    print(calculator(A, B, OP))
main()
