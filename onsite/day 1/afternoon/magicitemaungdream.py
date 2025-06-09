'''magic'''
def magic():
    '''magic'''
    sasan = str(input())
    thing = str(input())
    rou = int(input())
    op = ''
    for i in range(1,rou+1):
        if i == rou:
            op += thing
        else:
            op += f'{thing} -> '
    print(f'{sasan} -> {op}')
magic()
