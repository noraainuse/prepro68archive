'''discount'''
def discount(p):
    '''discount'''
    return p * 0.80
def get_regular_price():
    '''regular'''
    print(f'The sale price is ${discount(float(input())):.2f}')
get_regular_price()
