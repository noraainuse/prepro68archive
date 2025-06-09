'''moneysavingsummary'''

def main():
    '''moneycal'''
    day = int(input())
    n = 0
    total = 0.0
    while True:
        n += 1
        saving_this_day = float(input())
        if saving_this_day > 0:
            print(f'Day {n}: Saved {saving_this_day}')
            total += saving_this_day
        else:
            print("Amount must be greater than 0.")
            n -= 1
        if not n % 5:
            print(f'Summary at day {n}: Total savings so far is {total}')
        elif day == n:
            print(f'Summary at day {n}: Total savings so far is {total}')
        if day == n:
            break
main()
