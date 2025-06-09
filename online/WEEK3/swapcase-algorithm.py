'''swapcase'''
def swap(letter, x):
    '''triple'''
    for i in letter:
        if i.isupper() is True:
            x += i.lower()
        elif i.islower() is True:
            x += i.upper()
        else:
            x += i
    return x


def main():
    '''main'''
    letter = input()
    complete_letter = ''
    y = swap(letter, complete_letter)
    print(y)
main()
