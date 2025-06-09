"""homeland"""

def main():
    """main"""
    total = int(input())
    if total >= 50000:
        total *= 0.80
    elif total >= 10000:
        total *= 0.85
    elif total >= 1000:
        total *= 0.90
    print(f"{total}")


main()
