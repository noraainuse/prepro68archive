'''prime'''
def add_comma(num):
    '''commy'''
    num_str = str(num)
    result = ""
    length = len(num_str)

    for i, digit in enumerate(num_str):
        result += digit
        if i != length - 1 and (length - i - 1) % 3 == 0:
            result += ","

    return result

def finder(n):
    '''find nth prime'''
    count = 0
    num = 2

    while count < n:
        is_prime = True
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False

        if is_prime:
            count += 1
            if count == n:
                n_with_comma = add_comma(n)
                prime_with_comma = add_comma(num)
                return f'The {n_with_comma}th of prime number is {prime_with_comma}.'

        num += 1

    return ""

def main():
    '''main'''
    b = int(input())
    print(finder(b))

main()
