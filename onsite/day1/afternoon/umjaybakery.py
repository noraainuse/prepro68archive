'''umjay'''
def bakery(cake, bread, milk, money):
    '''bakery'''
    cake_b = cake * 45
    bread_b = bread * 15
    milk_b = milk * 20
    amount = cake_b + bread_b + milk_b
    print(f'Total amount due: {amount:.0f} baht')
    print(f'Change: {(money - amount):.0f} baht')
    print(f'Total number of items purchased: {cake + bread + milk}')
bakery(int(input()), int(input()), int(input()), float(input()))
