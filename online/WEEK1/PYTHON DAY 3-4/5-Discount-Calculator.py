"""Discount Docstring"""


def main():
    """main"""
    name = str(input())
    price = float(input())
    disprice = price * 0.80
    print(f"---------------Promotion {name}---------------")
    print(
        f"{name} is discounted from the original price of {price:.1f} baht to {disprice:.1f} baht."
    )


main()
