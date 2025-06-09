"""quadraticequation"""


def main():
    """main"""
    #input
    a = int(input())
    b = int(input())
    c = int(input())
    #formula
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    #output
    print(f"x1 = {x1:.1f}")
    print(f"x2 = {x2:.1f}")


main()
