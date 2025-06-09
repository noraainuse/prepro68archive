'''box'''

def box(length):
    '''box'''
    length_but_neg = length - 2
    mid = ' ' * length_but_neg
    print(f'{'*' * length}')
    print(f'*{mid}*')
    print(f'{'*' * length}')
box(int(input()))
