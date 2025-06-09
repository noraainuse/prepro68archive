"""store"""

def main():
    """main"""
    name = str(input())
    amount = int(input())
    price = float(input())
    fprice = amount * price
    print(f'Thank you {name}')
    print(f'Price per item: {price:.2f} baht')
    print(f'Total amount: {fprice:,.2f} baht')


main()
