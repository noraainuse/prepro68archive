'''alpha_or_num'''

def alp_or_num(inp):
    '''sub-function'''
    alp_count = 0
    num_count = 0
    for i in inp:
        if i.isalpha() is True:
            alp_count += 1
            print(f'"{i}" is Alphabet.')
        if i.isnumeric() is True:
            num_count += 1
            print(f'"{i}" is Numeric.')
    if alp_count > 1:
        print(f'The Alphabet has {alp_count} letters.')
    else:
        print(f'The Alphabet has {alp_count} letter.')
    if num_count > 1:
        print(f'The Numeric has {num_count} numbers.')
    else:
        print(f'The Numeric has {num_count} number.')

def main():
    '''main'''
    inp = input()
    alp_or_num(inp)

main()
