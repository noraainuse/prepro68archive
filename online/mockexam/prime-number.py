'''prime'''
def finder(a, b):
    '''find prime'''
    prime = ''
    debug = 0
    for num in range(a,b+1):
        if num > 1:
            for i in range(2, num):
                if not num % i:
                    break
            else:
                if not debug:
                    debug += 1
                    prime += f'{num}'
                else:
                    debug += 1
                    prime += f' ,{num}'
    print(prime)
    return debug
def main():
    '''main'''
    a = int(input())
    b = int(input())
    if a < 0 and b < 0:
        print(f"There haven't any prime number in the interval [{a},{b}].")
        print('0')
    else:
        print(finder(a, b))
main()
