'''phone'''

def num_check(number):
    '''nom'''
    return len(number)

def among(much, number):
    '''spliter'''
    match much:
        case 9:
            return f'{number[:2]}-{number[2:5]}-{number[5:9]}'
        case 10:
            return f'{number[:3]}-{number[3:6]}-{number[6:10]}'
def main():
    '''main'''
    number = input()
    much = num_check(number)
    print(among(much, number))
main()
