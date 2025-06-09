"""decoder"""


def main():
    """main"""
    #input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(str(a) + str(c))
    f = int(str(d) + str(a))
    g = int(str(b) + str(d))
    h = int(str(c) + str(b))
    #formula
    sum1 = str(e + f)
    sum2 = str(g + h)
    sum3 = sum1 + sum2
    #output
    print(f"{sum3}")

main()
