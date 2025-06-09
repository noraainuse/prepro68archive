'''taste-dish.py'''

def salty_aom(taste):
    '''salty_aom'''
    print(f'sweet = {taste.count('sweet')}')
    print(f'sour = {taste.count('sour')}')
    print(f'spicy = {taste.count('spicy')}')
    print(f'salty = {taste.count('salty')}')

def gordon_ramsey(taste):
    '''gordon'''
    sweet_count = taste.count('sweet')
    sour_count = taste.count('sour')
    spicy_count = taste.count('spicy')
    salty_count = taste.count('salty')
    if sweet_count > sour_count and sweet_count > spicy_count and sweet_count > salty_count:
        return 'This dish tastes sweet!'
    if sour_count > sweet_count and sour_count > spicy_count and sour_count > salty_count:
        return 'This dish has a sour kick!'
    if spicy_count > sweet_count and spicy_count > sour_count and spicy_count > salty_count:
        return 'This dish is going to be spicy!'
    if salty_count > sweet_count and salty_count > sour_count and salty_count > spicy_count:
        return 'This dish is salty!'
    if sweet_count > 0 and sweet_count == sour_count == spicy_count == salty_count:
        return 'This dish has a balanced flavor with multiple dominant tastes!'
    return 'This dish has no dominant flavor!'

def main():
    '''main'''
    ip = str(input())
    salty_aom(ip)
    print(gordon_ramsey(ip))
main()
