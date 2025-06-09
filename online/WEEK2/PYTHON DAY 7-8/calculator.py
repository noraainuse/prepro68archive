'''calculator'''
import math

def main():
    '''main'''
    operators = int(input())
    code = 0
    x = 0
    y = 0
    if 1 <= operators <= 8:
        x = int(input())
        if operators not in (6, 8):
            y = int(input())
    else:
        code = 4
    show = ''
    result = 0
    match operators:
        case 1:# บวก
            result = x + y
            show = str(f'{x} + {y}')
            code = 1
        case 2:# ลบ
            result = x - y
            show = str(f'{x} - {y}')
            code = 1
        case 3:# คูณ
            result = x * y
            show = str(f'{x} x {y}')
            code = 1
        case 4:# หาร
            if y:
                result = float(x / y)
                show = str(f'{x} / {y}')
                code = 1
            else:
                code = 3
        case 5:# ยกกำลัง
            result = float(math.pow(x, y))
            show = str(f'{x}^{y}')
            code = 1
        case 6:# รากที่สอง
            if x >= 0:
                result = float(math.sqrt(x))
                show = str(f'√{x}')
                code = 1
            else:
                code = 3
        case 7:# log.y
            if x > 0 and y > 0 and y != 1:
                result = float(math.log(x, y))
                show = str(f'{y} of {16}')
                code = 2
            else:
                code = 3
        case 8:# factorial
            if x >= 0:
                result = math.factorial(x)
                show = str(f'{x}!')
                code = 1
        case _:
            code = 4
    match code:
        case 1:
            print(f'Result: {show} = {result}')
        case 2:#log
            print(f'log base {show} is: {result}')
        case 3:
            print("Error")
        case 4:
            print("Invalid choice.")

main()
