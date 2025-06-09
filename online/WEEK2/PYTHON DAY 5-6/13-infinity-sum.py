"""sum"""

def main():
    """main"""
    soom_in_sum = int(input())
    x = 0
    for i in range(1, soom_in_sum + 1):
        if not i % 5:
            x += i
        elif not i % 3:
            x += i
    print(f'total: {x}')


main()
