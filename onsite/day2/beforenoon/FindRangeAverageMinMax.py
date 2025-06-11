'''find'''
def find():
    '''find'''
    current_lowest = 0
    current_highest = 0
    su_all = 0
    num_val = 0
    for i in range(5):
        num = float(input())
        su_all += num
        num_val += 1
        if not i:
            current_lowest = num
            current_highest = num
        if num < current_lowest:
            current_lowest = num
        if num > current_highest:
            current_highest = num
    print(f'Max = {current_highest}')
    print(f'Min = {current_lowest}')
    print(f'Range = {(current_highest - current_lowest):,}')
    print(f'Average = {(su_all / num_val):,.2f}')
find()
