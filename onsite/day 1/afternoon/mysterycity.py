'''kranow'''
def krapow(kin):
    '''krapow'''
    print("Customer: Excuse me, how much is the basil pork with fried egg?")
    print("Vendor: The price of basil pork with fried egg is 40 baht per plate.")
    print(f'Customer: Then I\'d like {kin} plate(s) of basil pork with fried egg, please.')
    print(f'Vendor: That will be {kin * 40} baht.')
    print(f'Customer: (hands over {kin * 40} baht)')
    print("Vendor: Thank you for your purchase!")
krapow(int(input()))
