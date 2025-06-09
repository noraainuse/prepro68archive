"""Coffee"""


def main():
    """main"""
    name = str(input())
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    pdt = p1 + p2 + p3
    pdisc = pdt * (1 - 0.075)
    pdiscr = round(pdisc, 2)
    print(f"{name}, total before discount is {pdt} THB")
    print(f"After 7.5% discount, the amount to pay is {pdiscr} THB")


main()
