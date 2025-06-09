'''water-dispenser'''

def main():
    '''main'''
    total = 0
    print("")
    while True:
        insert_coin = int(input())
        match insert_coin:
            case 1:
                total += insert_coin
                if total >= 10:
                    print(f'Current total: {total} baht')
                    print('Payment complete! Dispensing your drink now...')
                else:
                    print(f'Current total: {total} baht')
            case 2:
                total += insert_coin
                if total >= 10:
                    print(f'Current total: {total} baht')
                    print('Payment complete! Dispensing your drink now...')
                else:
                    print(f'Current total: {total} baht')
            case 5:
                total += insert_coin
                if total >= 10:
                    print(f'Current total: {total} baht')
                    print('Payment complete! Dispensing your drink now...')
                else:
                    print(f'Current total: {total} baht')
            case _:
                print('Invalid coin. Please insert 1, 2, or 5 Baht only')

        if total >= 10:
            break

main()
